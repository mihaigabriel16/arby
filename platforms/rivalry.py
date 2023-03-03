import json
import requests

data_array = []

def getGames():
    object = {
        "platform": "RIVALRY",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://www.rivalry.com/search/match/markets"
    body = {"id":802434,"tags":["Winner"]}
    x = requests.post(url, json=body)
    data = x.text
    return sortGames(data)

def sortGames(data):
    data = json.loads(data)
    for match in data["marketBlocks"]["Winner"]:
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
        object["key"] = match["match"]["tournament"]["name"]
        competitors = match["outcomes"]
        object["team1"]["name"] = competitors[0]["name"]
        object["team1"]["odds"] = competitors[0]["odds"]
        object["team2"]["name"] = competitors[1]["name"]
        object["team2"]["odds"] = competitors[1]["odds"]
        data_array.append(object)
