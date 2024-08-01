import ntpath
import os
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

import dropbox
import pytz
import requests
from icalendar import Calendar, Event


# Function to fetch and create an iCal file for a given team or league
def create_ical_for_team_or_league(url, timezone, output_filename, is_league=False):
    response = requests.get(url)
    if response.status_code == 200:
        if is_league:  # Special handling for league-based data like F1

            root = ET.fromstring(response.content)
            # Register namespace to handle namespace-aware queries
            namespaces = {"ns": "http://ergast.com/mrd/1.5"}
            races = root.findall(".//ns:Race", namespaces)

            cal = Calendar()
            cal.add("prodid", "-//F1 Schedule//example.com//")
            cal.add("version", "2.0")

            for race in races:
                race_name = race.find("ns:RaceName", namespaces).text
                date_str = race.find("ns:Date", namespaces).text
                time_str = (
                    race.find("ns:Time", namespaces).text
                    if race.find("ns:Time", namespaces) is not None
                    else "00:00:00Z"
                )

                try:
                    # Parse date and time separately
                    event_datetime_str = f"{date_str}T{time_str.rstrip('Z')}"
                    # Convert event time to naive datetime in UTC
                    event_date_utc = datetime.fromisoformat(event_datetime_str)
                    # Convert naive UTC datetime to aware datetime in local timezone
                    event_date_local = event_date_utc.replace(
                        tzinfo=pytz.utc
                    ).astimezone(timezone)
                except ValueError as e:
                    print(f"Error parsing date/time for race '{race_name}': {e}")
                    continue

                ical_event = Event()
                ical_event.add("summary", race_name)
                ical_event.add("dtstart", event_date_local)
                ical_event.add("dtend", event_date_local + timedelta(hours=2))
                ical_event.add("dtstamp", datetime.now(timezone))

                cal.add_component(ical_event)

        else:  # Standard processing for team-based sports
            data = response.json()
            cal = Calendar()
            cal.add("prodid", "-//My Team Schedule//example.com//")
            cal.add("version", "2.0")

            for event in data.get("events", []):
                date_str = event.get("date")
                opponents = event.get("name")
                event_date = datetime.fromisoformat(date_str).astimezone(timezone)

                ical_event = Event()
                ical_event.add("summary", opponents)
                ical_event.add("dtstart", event_date)
                ical_event.add("dtend", event_date + timedelta(hours=3))
                ical_event.add("dtstamp", datetime.now(timezone))

                cal.add_component(ical_event)

        # Save the calendar to a .ics file
        schedules_dir = "schedules"
        os.makedirs(schedules_dir, exist_ok=True)
        file_path = os.path.join(schedules_dir, output_filename)
        with open(file_path, "wb") as f:
            f.write(cal.to_ical())

        print(
            f"iCal file '{output_filename}' created successfully in '{schedules_dir}' directory."
        )
    else:
        print(f"Failed to fetch data from {url}: {response.status_code}")


# Function to upload a file to Dropbox
def upload_to_dropbox(file_path, dbx):
    if os.path.exists(file_path):
        dropbox_path = f"/{ntpath.basename(file_path)}"
        with open(file_path, "rb") as f:
            dbx.files_upload(
                f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite")
            )
        print(f"Uploaded '{file_path}' to Dropbox at '{dropbox_path}'.")
    else:
        print(f"File '{file_path}' does not exist.")


# Read the leagues and teams from the configuration file
config_file = "sports_config.txt"
dropbox_config_file = "dropbox_config.txt"
base_url = "https://site.api.espn.com/apis/site/v2/sports/"
league_urls = {
    "MLB": "baseball/mlb",
    "NFL": "football/nfl",
    "NHL": "hockey/nhl",
    "F1": "http://ergast.com/api/f1/current",
    "NBA": "basketball/nba",
    "MLS": "soccer/usa.1",
    # Add more leagues here if necessary
}

# Timezone for the events (modify as needed)
timezone = pytz.timezone("America/New_York")

# Read Dropbox configuration
with open(dropbox_config_file, "r") as dbx_config:
    access_token = None
    for line in dbx_config:
        if line.startswith("AccessToken:"):
            access_token = line.split(":")[1].strip()

# Initialize Dropbox client
dbx = dropbox.Dropbox(access_token)

# Process each line in the configuration file
with open(config_file, "r") as file:
    current_league = None
    team_id = None
    for line in file:
        if line.startswith("League:"):
            current_league = line.split(":")[1].strip()
            league_path = league_urls.get(current_league)
            team_id = None  # Reset team_id when a new league is encountered
            if league_path:
                is_league = current_league == "F1"
                if is_league:
                    url = league_path
                    output_filename = f"{current_league.lower()}_schedule.ics"
                    create_ical_for_team_or_league(
                        url, timezone, output_filename, is_league
                    )
                    # Upload the file to Dropbox
                    upload_to_dropbox(os.path.join("schedules", output_filename), dbx)
            else:
                print(f"Unsupported league: {current_league}")
        elif line.startswith("Team:") and current_league and current_league != "F1":
            team_id = line.split(":")[1].strip()
            if team_id:
                url = f"{base_url}{league_path}/teams/{team_id}/schedule"
                output_filename = f"{current_league.lower()}_team_{team_id}.ics"
                create_ical_for_team_or_league(url, timezone, output_filename)
                # Upload the file to Dropbox
                upload_to_dropbox(os.path.join("schedules", output_filename), dbx)
