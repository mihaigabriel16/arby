import requests
import json

data_array = []

def getGames():
    fetchGames()
    object = {
        "platform": "ESPORTSBET",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://esbdjt.esportsbet.io/api/GetIndexMatch"
    body = {
        "GameCat": 1,
        "SportId": -99,
        "BaseLGIds": [
            -99
        ],
        "EventMarket": -99,
        "MatchCnt": 200000,
        "SortType": 1,
        "HasLive": False,
        "Token": None,
        "Language": "eng",
        "BettingChannel": 1,
        "MatchFilter": -99,
        "Timestamp": "",
        "PHash": "",
        "Stats": ""
    }

    x = requests.post(url, json = body)
    data = x.text  
    filterGames(data)

def filterGames(data):
    data = json.loads(data)
    for sport in data["Sport"]:
        if sport["SportName"] == "LEAGUE OF LEGENDS":
            LG = sport["LG"]
            for league in LG:
                if len(league["ParentMatch"]) > 0:
                    for match in league["ParentMatch"]:
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
                            object["key"] = league["LGName"]
                            object["team1"]["name"] = match["PHTName"]
                            object["team2"]["name"] = match["PATName"]
                            if len(match["Match"]) > 0:
                                object["team1"]["odds"] = match["Match"][0]["Odds"][0]["SEL"][0]["Odds"]
                                object["team2"]["odds"] = match["Match"][0]["Odds"][0]["SEL"][1]["Odds"]
                            data_array.append(object)