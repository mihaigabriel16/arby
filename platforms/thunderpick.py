import requests
import json

data_array = []

def getGames():
    fetchGames()
    object = {
        "platform": "THUNDERPICK",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://thunderpick.io/api/matches"
    body = {
        "gameIds":[3],
        "competitionId":None,
        "country":None
    }
    x = requests.post(url, json = body)
    data = x.text
    return sortGames(data)


def sortGames(data):
    data = json.loads(data)
    games = data["data"]["upcoming"]
    for match in games:
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
        market = match["market"]
        if market["name"] == "Match Winner":
            object["key"] = match["name"]
            object["team1"]["name"] = market["home"]["name"]
            object["team1"]["odds"] = market["home"]["odds"]
            object["team2"]["name"] = market["away"]["name"]
            object["team2"]["odds"] = market["away"]["odds"]
            data_array.append(object)
# https://thunderpick.io/api/matches
# {"gameIds":[3],"competitionId":null,"country":null}