# Created by Asunday47 01/22/2021

import json
import requests
import urllib
import pandas as pd 

print("\n"*10)
print("Starting Blaseball stuff")

#********************************
#  MANUAL UPDATING SECTION  
#Games/Season Settings
    # Games 0-98 cover the regular season
    # Seasons are also 0 indexed (ex: Season 11 is data 10)

startDay = 0 # first day
endDay = 98 # 1 above last day

startSeason = 0 # First Season to check
endSeason = 9 # 1 above last season

fileName = "Blaseball_Database_s0_s9.csv"
#********************************



gameIDs = []
print()
print("****************************************")
print("*****  Grabbing Season / Day Data  *****")
print("****************************************")
## Grab all the game IDs per Day
for h in range(startSeason,endSeason+1):
    for i in range(startDay,endDay+1):
        print("Grabbing game data from - Season "+ str(h) + ", Day " + str(i))
        #Get Games per day/season API details
        gamesByDateURL = 'https://www.blaseball.com/database/games?day=' + str(i) + '&season=' + str(h)
        gamesByDayData = requests.get(gamesByDateURL)
        gamesByDayData = json.loads(gamesByDayData.text)

        for j in gamesByDayData:
            gameIDs = gameIDs + [j["id"]]

# Initialize Lists
day=[]
season=[]
outcomes=[]
homeTeam =[]
homeScore = []
homeOdds = []
awayTeam = []
awayScore = []
awayOdds =[]
gameCount = 1
gameCounts = len(gameIDs)
print()
print("************************************************")
print("*****  Grabbing data from each game found  *****")
print("************************************************")
print()
for i in gameIDs:
    #Get Game API details
    print("Grabbing game data from game - " + str(gameCount) +" of " + str(gameCounts))
    gameCount = gameCount+1
    gameByIDURL = 'https://www.blaseball.com/database/gameById/' + i
    gamesByID = requests.get(gameByIDURL)
    gamesByID = json.loads(gamesByID.text)
    
    #Add to lists
    day = day + [gamesByID["day"]]
    season = season + [gamesByID["season"]]
    outcomes = outcomes + [gamesByID["outcomes"]]
    homeTeam = homeTeam + [gamesByID["homeTeamNickname"]]
    homeScore = homeScore + [gamesByID["homeScore"]]
    homeOdds = homeOdds + [gamesByID["homeOdds"]]
    awayTeam = awayTeam + [gamesByID["awayTeamNickname"]]
    awayScore = awayScore+ [gamesByID["awayScore"]]
    awayOdds = awayOdds + [gamesByID["awayOdds"]]

print()
print()
print("************************************************")
print("     All data obtained")
print("     Writing data to " +fileName)
print("************************************************")
    
# dictionary of lists   
dict = {'Season': season,
        'Day': day,
        'Home Team': homeTeam,
        'Home Score': homeScore,
        'Home Odds': homeOdds,
        'Away Team': awayTeam,
        'Away Score': awayScore,
        'Away Odds': awayOdds,
        'Outcomes': outcomes}   
       
df = pd.DataFrame(dict)  
    
# saving the dataframe  
df.to_csv(fileName)  

print()
print("Woot, Finished Script!!")

