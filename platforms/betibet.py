import requests
import json

data_array = []

def getGames():
    fetchGames()
    object = {
        "platform": "BETIBET",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://www.betibet.com/api/v2/matches?bettable=true&limit=500&match_status=0&sort_by=tournament.priority:asc&sort_by=start_time:asc&sort_by=bets_count:desc&sport_key=lol&start_from=2023-03-05T13:26:24.010Z&start_to=2099-03-08T13:26:24.010Z"
    x = requests.get(url)
    data = x.text  
    filterGames(data)

def filterGames(data):
    data = json.loads(data)
    for match in data["data"]:
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
            object["team1"]["name"] = match["competitors"]["home"]["name"]
            object["team2"]["name"] = match["competitors"]["away"]["name"]
            
            if "main_market" in match:
                mm = match["main_market"]
                if "outcomes" in mm:
                    if len(mm["outcomes"]) > 0:
                        for oc in mm["outcomes"]:
                            if oc["name"] == object["team1"]["name"]:
                                object["team1"]["odds"] = formatOdd(oc["odds"])
                            else:
                                object["team2"]["odds"] = formatOdd(oc["odds"])
                        data_array.append(object)
        except (KeyError, TypeError) as error:
            pass

def formatOdd(value):
    value = str(value)
    arr = []
    size = 0
    for char in range(0, len(value)):
        arr.append(value[char])
        size += 1
    if size >= 4:
        dec = [arr[size - 3], arr[size - 2], arr[size - 1]]
        print(dec)
        del arr[size - 3]
        del arr[size - 2]
        del arr[-1]
        odd = ""
        for item in arr:
            odd = odd + item
        odd = odd + "."
        for item in dec:
            odd = odd + item
        return float(odd)