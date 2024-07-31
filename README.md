<div align="center">
<h1> 📅 Sports Calendar Creator </h1>
<p>Create simple calendars for your favorite teams' schedules, easily addable to most calendar apps!</p>
<img src="https://img.shields.io/badge/made_with_♡_by-silas-red">
<a href="https://github.com/silasmcnutt/sports-calendar-creator/blob/main/LICENSE.txt"><img src="https://img.shields.io/badge/License-MIT-green"></a>
</div>

## Usage

1. Go to the [Dropbox App Console](https://www.dropbox.com/developers/apps?_tk=pilot_lp&_ad=topbar4&_camp=myapps) and create a new app.
2. Choose `App folder` when Dropbox prompts you for access type.
3. Under `Generated access token` click `Generate`.
4. Copy this code under `dropbox_config.txt` in the project's working directory.
5. Open `sports_config.txt` and write the leagues and their respective teams you would like to follow. Each leagues team ID's are listed below. The format of `sports_config.txt` should look something as follows:

> **Note: F1 does not require a `Team` line.**

```
League: NFL
Team: 9
League: MLB
Team: 17
League: F1
```
6. Run `main.py`
7. If wanting to add the .ics files to something like Google Calendar, copy the link for the file from Dropbox and paste it into the URL box when creating a new calendar from URL. **Important:** Change the `dl=0` at the end of the link to `dl=1`.

Full list of supported leagues:

<ul>
<li>NFL</li>
<li>MLB</li>
<li>NBA</li>
<li>NHL</li>
<li>MLS</li>
<li>F1</li>
</ul>

## Team IDs

<details>
<summary><strong>NFL</strong></summary>
 <table>
  <tr>
    <th>Team</th>
    <th>ID</th>
  </tr>
  <tr>
    <td>Arizona Cardinals</td>
    <td>22</td>
  </tr>
    <tr>
    <td>Atlanta Falcons</td>
    <td>1</td>
  </tr>
    <tr>
    <td>Baltimore Ravens</td>
    <td>33</td>
  </tr>
    <tr>
    <td>Buffalo Bills</td>
    <td>2</td>
  </tr>
    <tr>
    <td>Carolina Panthers</td>
    <td>29</td>
  </tr>
    <tr>
    <td>Chicago Bears</td>
    <td>3</td>
  </tr>
    <tr>
    <td>Cincinnati Bengals</td>
    <td>4</td>
  </tr>
    <tr>
    <td>Cleveland Browns</td>
    <td>5</td>
  </tr>
    <tr>
    <td>Dallas Cowboys</td>
    <td>6</td>
  </tr>
    <tr>
    <td>Denver Broncos</td>
    <td>7</td>
  </tr>
    <tr>
    <td>Detroit Lions</td>
    <td>8</td>
  </tr>
    <tr>
    <td>Green Bay Packers</td>
    <td>9</td>
  </tr>
    <tr>
    <td>Houston Texans</td>
    <td>34</td>
  </tr>
    <tr>
    <td>Indianapolis Colts</td>
    <td>11</td>
  </tr>
    <tr>
    <td>Jacksonville Jaguars</td>
    <td>30</td>
  </tr>
    <tr>
    <td>Kansas City Chiefs</td>
    <td>12</td>
  </tr>
    <tr>
    <td>Las Vegas Raiders</td>
    <td>13</td>
  </tr>
    <tr>
    <td>Los Angeles Chargers</td>
    <td>24</td>
  </tr>
    <tr>
    <td>Los Angeles Rams</td>
    <td>14</td>
  </tr>
    <tr>
    <td>Miami Dolphins</td>
    <td>15</td>
  </tr>
    <tr>
    <td>Minnesota Vikings</td>
    <td>16</td>
  </tr>
    <tr>
    <td>New England Patriots</td>
    <td>17</td>
  </tr>
    <tr>
    <td>New Orleans Saints</td>
    <td>18</td>
  </tr>
    <tr>
    <td>New York Giants</td>
    <td>19</td>
  </tr>
    <tr>
    <td>New York Jets</td>
    <td>20</td>
  </tr>
    <tr>
    <td>Philadelphia Eagles</td>
    <td>21</td>
  </tr>
    <tr>
    <td>Pittsburgh Steelers</td>
    <td>23</td>
  </tr>
    <tr>
    <td>San Francisco 49ers</td>
    <td>25</td>
  </tr>
    <tr>
    <td>Seattle Seahawks</td>
    <td>26</td>
  </tr>
    <tr>
    <td>Tampa Bay Buccaneers</td>
    <td>27</td>
  </tr>
    <tr>
    <td>Tennessee Titans</td>
    <td>10</td>
  </tr>
    <tr>
    <td>Washington Commanders</td>
    <td>28</td>
  </tr>
 </table>
</details>

<br>

<details>
<summary><strong>MLB</strong></summary>
 <table>
  <tr>
    <th>Team</th>
    <th>ID</th>
  </tr>
  <tr>
    <td>Arizona Diamondbacks</td>
    <td>29</td>
  </tr>
  <tr>
    <td>Atlanta Braves</td>
    <td>15</td>
  </tr>
  <tr>
    <td>Baltimore Orioles</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Boston Red Sox</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Chicago Cubs</td>
    <td>16</td>
  </tr>
  <tr>
    <td>Chicago White Sox</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Cincinnati Reds</td>
    <td>17</td>
  </tr>
  <tr>
    <td>Cleveland Guardians</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Colorado Rockies</td>
    <td>27</td>
  </tr>
  <tr>
    <td>Detroit Tigers</td>
    <td>6</td>
  </tr>
  <tr>
    <td>Houston Astros</td>
    <td>18</td>
  </tr>
  <tr>
    <td>Kansas City Royals</td>
    <td>7</td>
  </tr>
  <tr>
    <td>Los Angeles Angels</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Los Angeles Dodgers</td>
    <td>19</td>
  </tr>
  <tr>
    <td>Miami Marlins</td>
    <td>28</td>
  </tr>
  <tr>
    <td>Milwuakee Brewers</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Minnesota Twins</td>
    <td>9</td>
  </tr>
  <tr>
    <td>New York Mets</td>
    <td>21</td>
  </tr>
  <tr>
    <td>New York Yankees</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Oakland Athletics</td>
    <td>11</td>
  </tr>
  <tr>
    <td>Phialdelphia Phillies</td>
    <td>22</td>
  </tr>
  <tr>
    <td>Pittsburgh Pirates</td>
    <td>23</td>
  </tr>
  <tr>
    <td>San Diego Padres</td>
    <td>25</td>
  </tr>
  <tr>
    <td>San Francisco Giants</td>
    <td>26</td>
  </tr>
  <tr>
    <td>Seattle Mariners</td>
    <td>12</td>
  </tr>
  <tr>
    <td>St. Louis Cardinals</td>
    <td>24</td>
  </tr>
  <tr>
    <td>Tampa Bay Rays</td>
    <td>30</td>
  </tr>
  <tr>
    <td>Texas Rangers</td>
    <td>13</td>
  </tr>
  <tr>
    <td>Toronto Blue Jays</td>
    <td>14</td>
  </tr>
  <tr>
    <td>Washington Nationals</td>
    <td>20</td>
  </tr>
</table> 
</details>

<br>

<details>
<summary><strong>NBA</strong></summary>
 <table>
  <tr>
    <th>Team</th>
    <th>ID</th>
  </tr>
  <tr>
    <td>Atlanta Hawks</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Boston Celtics</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Brooklyn Nets</td>
    <td>17</td>
  </tr>
  <tr>
    <td>Charlotte Hornets</td>
    <td>30</td>
  </tr>
  <tr>
    <td>Chicago Bulls</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Cleveland Cavaliers</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Dallas Mavericks</td>
    <td>6</td>
  </tr>
  <tr>
    <td>Denver Nuggets</td>
    <td>7</td>
  </tr>
  <tr>
    <td>Detroit Pistons</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Golden State Warriors</td>
    <td>9</td>
  </tr>
  <tr>
    <td>Houston Rockets</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Indiana Pacers</td>
    <td>11</td>
  </tr>
  <tr>
    <td>LA Clippers</td>
    <td>12</td>
  </tr>
  <tr>
    <td>Los Angeles Lakers</td>
    <td>13</td>
  </tr>
  <tr>
    <td>Memphis Grizzlies</td>
    <td>29</td>
  </tr>
  <tr>
    <td>Miami Heat</td>
    <td>14</td>
  </tr>
  <tr>
    <td>Milwaukee Bucks</td>
    <td>15</td>
  </tr>
  <tr>
    <td>Minnesota Timberwolves</td>
    <td>16</td>
  </tr>
  <tr>
    <td>New Orleans Pelicans</td>
    <td>3</td>
  </tr>
  <tr>
    <td>New York Knicks</td>
    <td>18</td>
  </tr>
  <tr>
    <td>Oklahoma City Thunder</td>
    <td>25</td>
  </tr>
  <tr>
    <td>Orlando Magic</td>
    <td>19</td>
  </tr>
  <tr>
    <td>Philadelphia 76ers</td>
    <td>20</td>
  </tr>
  <tr>
    <td>Phoenix Suns</td>
    <td>21</td>
  </tr>
  <tr>
    <td>Portland Trail Blazers</td>
    <td>22</td>
  </tr>
  <tr>
    <td>Sacramento Kings</td>
    <td>23</td>
  </tr>
  <tr>
    <td>San Antonio Spurs</td>
    <td>24</td>
  </tr>
  <tr>
    <td>Toronto Raptors</td>
    <td>28</td>
  </tr>
  <tr>
    <td>Utah Jazz</td>
    <td>26</td>
  </tr>
  <tr>
    <td>Washington Wizards</td>
    <td>27</td>
  </tr>
</table> 
</details>

<br>

<details>
<summary><strong>NHL</strong></summary>
 <table>
  <tr>
    <th>Team</th>
    <th>ID</th>
  </tr>
  <tr>
    <td>Anaheim Ducks</td>
    <td>25</td>
  </tr>
  <tr>
    <td>Boston Bruins</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Buffalo Sabres</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Calgary Flames</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Carolina Hurricanes</td>
    <td>7</td>
  </tr>
  <tr>
    <td>Chicago Blackhawks</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Colorado Avalanche</td>
    <td>17</td>
  </tr>
  <tr>
    <td>Columbus Blue Jackets</td>
    <td>29</td>
  </tr>
  <tr>
    <td>Dallas Stars</td>
    <td>9</td>
  </tr>
  <tr>
    <td>Detroit Red Wings</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Edmonton Oilers</td>
    <td>6</td>
  </tr>
  <tr>
    <td>Florida Panthers</td>
    <td>26</td>
  </tr>
  <tr>
    <td>Los Angeles Kings</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Minnesota Wild</td>
    <td>30</td>
  </tr>
  <tr>
    <td>Montreal Canadiens</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Nashville Predators</td>
    <td>27</td>
  </tr>
  <tr>
    <td>New Jersey Devils</td>
    <td>11</td>
  </tr>
  <tr>
    <td>New York Islanders</td>
    <td>12</td>
  </tr>
  <tr>
    <td>New York Rangers</td>
    <td>13</td>
  </tr>
  <tr>
    <td>Ottawa Senators</td>
    <td>14</td>
  </tr>
  <tr>
    <td>Philadelphia Flyers</td>
    <td>15</td>
  </tr>
  <tr>
    <td>Pittsburgh Penguins</td>
    <td>16</td>
  </tr>
  <tr>
    <td>San Jose Sharks</td>
    <td>18</td>
  </tr>
  <tr>
    <td>Seattle Kraken</td>
    <td>124292</td>
  </tr>
  <tr>
    <td>St. Louis Blues</td>
    <td>19</td>
  </tr>
  <tr>
    <td>Tampa Bay Lightning</td>
    <td>20</td>
  </tr>
  <tr>
    <td>Toronto Maple Leafs</td>
    <td>21</td>
  </tr>
  <tr>
    <td>Utah Hockey Club</td>
    <td>129764</td>
  </tr>
  <tr>
    <td>Vancouver Canucks</td>
    <td>22</td>
  </tr>
  <tr>
    <td>Vegas Golden Knights</td>
    <td>37</td>
  </tr>
  <tr>
    <td>Washington Capitals</td>
    <td>23</td>
  </tr>
  <tr>
    <td>Winnipeg Jets</td>
    <td>28</td>
  </tr>
 </table>
</details>

<br>

<details>
 <summary><strong>MLS</strong></summary>
  <table>
   <tr>
     <th>Team</th>
     <th>ID</th>
   </tr>
   <tr>
     <td>Atlanta United FC</td>
     <td>18418</td>
   </tr>
   <tr>
     <td>Austin FC</td>
     <td>20906</td>
   </tr>
   <tr>
     <td>CF Montréal</td>
     <td>9720</td>
   </tr>
   <tr>
     <td>Charlotte FC</td>
     <td>21300</td>
   </tr>
   <tr>
     <td>Chicago Fire FC</td>
     <td>182</td>
   </tr>
   <tr>
     <td>Colorado Rapids</td>
     <td>184</td>
   </tr>
   <tr>
     <td>Columbus Crew</td>
     <td>183</td>
   </tr>
   <tr>
     <td>D.C. United</td>
     <td>193</td>
   </tr>
   <tr>
     <td>FC Cincinnati</td>
     <td>18267</td>
   </tr>
   <tr>
     <td>FC Dallas</td>
     <td>185</td>
   </tr>
   <tr>
     <td>Houston Dynamo FC</td>
     <td>6077</td>
   </tr>
   <tr>
     <td>Inter Miami CF</td>
     <td>20232</td>
   </tr>
   <tr>
     <td>LA Galaxy</td>
     <td>187</td>
   </tr>
   <tr>
     <td>LAFC</td>
     <td>18966</td>
   </tr>
   <tr>
     <td>Minnesota United FC</td>
     <td>17362</td>
   </tr>
   <tr>
     <td>Nashville SC</td>
     <td>18986</td>
   </tr>
   <tr>
     <td>New England Revolution</td>
     <td>189</td>
   </tr>
   <tr>
     <td>New York City FC</td>
     <td>17606</td>
   </tr>
   <tr>
     <td>New York Red Bulls</td>
     <td>190</td>
   </tr>
   <tr>
     <td>Orlando City SC</td>
     <td>12011</td>
   </tr>
   <tr>
     <td>Philadelphia Union</td>
     <td>10739</td>
   </tr>
   <tr>
     <td>Portland Timbers</td>
     <td>9723</td>
   </tr>
   <tr>
     <td>Real Salt Lake</td>
     <td>4771</td>
   </tr>
   <tr>
     <td>San Jose Earthquakes</td>
     <td>191</td>
   </tr>
   <tr>
     <td>Seattle Sounders FC</td>
     <td>9726</td>
   </tr>
   <tr>
     <td>Sporting Kansas City</td>
     <td>186</td>
   </tr>
   <tr>
     <td>St. Louis CITY SC</td>
     <td>21812</td>
   </tr>
   <tr>
     <td>Toronto FC</td>
     <td>7318</td>
   </tr>
   <tr>
     <td>Vancouver Whitecaps</td>
     <td>9727</td>
   </tr>
 </table>
</details>

## Support
If you have any questions or suggestions regaerding the spreadsheet, please feel free to reach out and message me on Discord. My username is `mcsilas.` (yes, the period is included).

## License
This project is licensed under the terms of the [MIT](https://github.com/silasmcnutt/ultimate-coaster-spreadsheet/blob/main/LICENSE.txt) license.