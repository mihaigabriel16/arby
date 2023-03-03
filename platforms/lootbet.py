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
        if len(item["top_market"]) > 0:
            object["key"] = item["tournament"]["Name"]
            object["team1"]["name"] = item["HomeTeamName"]
            object["team2"]["name"] = item["AwayTeamName"]
            for market in item["top_market"]:
                for odd in market["odds"]:
                    if odd["Name"] == object["team1"]["name"]:
                        object["team1"]["odds"] = odd["Value"]
                    else:
                        object["team2"]["odds"] = odd["Value"]
            data_array.append(object)