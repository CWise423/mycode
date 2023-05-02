#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://github.com/toddrob99/MLB-StatsAPI/wiki

import requests
import statsapi

MLB = "https://pypi.org/project/MLB-StatsAPI/"

def main():

    favPlayer = input("Who's your favorite player?\n> ")
    ## Send HTTPS GET to MLB-StatsAPI
    player = statsapi.lookup_player(favPlayer)
    playerId = player[0]['id']
    print(playerId)

    favTeam = input("Who's your favorite team?\n>")
    team = statsapi.lookup_team(favTeam)
    teamId = team[0]['id']

    for player in statsapi.lookup_player(playerId):
        print('Full name: {}, Position: {}'.format(player['fullName'], player['primaryPosition']['abbreviation']))

    for team in statsapi.lookup_team(teamId):
        print(statsapi.roster(teamId))

    #print(statsapi.roster(100))
    ## Decode the response
   # got_player = player.json()

    ## print the response
   # print(got_player)
    
    ## display only the keys within
    ## the dictionary by using dict.keys()
    ## great for seeing what keys are available for lookup
   # print(got_player.keys())
    
if __name__ == "__main__":
    main()

