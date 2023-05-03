import json
import requests

data_array = []

def getGames():
    fetchGames()
    object = {
        "platform": "22BETTOP",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://22bet-top.com/LiveFeed/Get1x2_VZip?sports=40&count=50&lng=en&mode=4&country=152&partner=151&getEmpty=true"
    x = requests.get(url)
    data = x.text
    return sortGames(data)

def sortGames(data):
    data = json.loads(data)
    games = data["Value"]
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

        if match["CHIMG"] == "sub_e_sport_league_of_legends.png":
            object["key"] = match["LR"]

            object["team1"]["name"] = match["O1"]
            object["team1"]["odds"] = match["E"][0]["C"]
            object["team2"]["name"] = match["O2"]
            object["team2"]["odds"] = match["E"][1]["C"]
            data_array.append(object)
