import requests
import json

data_array = []

def getGames():
    fetchGames()
    object = {
        "platform": "LOOTBET",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://loot.bet/odds/api/matches?items=20000&match_type=1&match_type=2&page=1&league=00000000-0000-0000-0000-000000000cd0"
    x = requests.get(url)
    if x.status_code == 200:
        data = x.text  
        filterGames(data)

def filterGames(data):
    data = json.loads(data)
    for item in data:
        object = {
            "key": None,
            "team1": {
                "name": None,
                "odds": None
            }, 
            "team2": {
                "name": None,
                "odds": None
            }
        }
        object["key"] = item["tournament"]["Name"]
        object["team1"]["name"] = item["HomeTeamName"]
        object["team2"]["name"] = item["AwayTeamName"]
        odds = getOdds(item["Id"], object["team1"]["name"], object["team2"]["name"])
        object["team1"]["odds"] = odds["odds1"]
        object["team2"]["odds"] = odds["odds2"]
        data_array.append(object)

def getOdds(gameId, teamA, teamB):
    url = "https://loot.bet/odds/api/market?match=" + gameId + "&weight=negative"
    x = requests.get(url)
    if x.status_code == 200:
        object = {
            "odds1": None,
            "odds2": None
        }
        data = json.loads(x.text)
        for item in data:
            if item["MatchId"] == gameId:
                if item["MarketTemplateId"] == 141:
                    if len(item["odds"]) > 0:
                        object["odds1"] = item["odds"][0]["Value"]
                        object["odds2"] = item["odds"][1]["Value"]
        return object
    