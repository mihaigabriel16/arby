import requests
import json

data_array = []


def getGames():
    return 0

def getCompetitions():
    events_data = json.loads(getEvents())
    for competition in events_data["sports"][0]["competitions"]:
        url = "https://www.cloudbet.com/sports-api/c/v6/sports/competitions/" + competition["key"] + "/events?markets=league_of_legends.winner&markets=league_of_legends.map_handicap&locale=en"
        x = requests.get(url)
        data = x.text
        for event in json.loads(data)["events"]:
            addDataToArray(event)
    print(data_array)
        
    
def getEvents():
    url = "https://www.cloudbet.com/sports-api/c/v6/sports/events?sports=league-of-legends&markets=league_of_legends.winner&limit=3000&locale=en"
    x = requests.get(url)
    return x.text

def addDataToArray(data):
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
    try:
        object["key"] = data["key"]
        object["team1"]["name"] = data["home"]["name"]
        object["team2"]["name"] = data["away"]["name"]
        for item in data["markets"]["league_of_legends.winner"]["submarkets"]["period=default"]["selections"]:
            if item["outcome"] == "home":
                object["team1"]["odds"] = item["price"]
            else:
                object["team2"]["odds"] = item["price"]
        data_array.append(object)
    except KeyError:
        pass

