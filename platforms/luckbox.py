import json
import requests
import configs

data_array = []

def getGames():
    fetchGames()
    object = {
        "platform": "LUCKBOX",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://api.luckbox.com/v1/match?limit=100&page=1&games[]=league-of-legends"
    headers = {"Cookie": configs.LUCKBOX_COOKIE_TOKEN}
    x = requests.get(url, headers=headers)
    data = x.text
    return sortGames(data)

def sortGames(data):
    data = json.loads(data)
    games = data["data"]["items"]
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
        object["key"] = match["tournament"]["name"]
        object["team1"]["name"] = match["sideA"]["name"]
        AID = match["sideA"]["id"]
        object["team2"]["name"] = match["sideB"]["name"]
        BID = match["sideB"]["id"]
        for item in match["primaryMarket"]["bettingOffers"]:
            if item["opponentId"] == AID:
                object["team1"]["odds"] = item["odds"]
            else:
                object["team2"]["odds"] = item["odds"]
        data_array.append(object)
