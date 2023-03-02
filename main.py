import requests 


def getEsportsBetGames():
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
    return x.text

def getCloudBetGames():
    return 0
def getCloudBetEvents():
    url = "https://www.cloudbet.com/sports-api/c/v6/sports/events?sports=league-of-legends&markets=league_of_legends.winner&limit=3000&locale=en"
    x = requests.get(url)
    return x.text
def getCloudBetCompetitions():
    events_data = getCloudBetEvents()
    for competition in events_data["sports"]["competitions"]:
        object = {

            "team1": {
                "name": None,
                "odds": None
            }, 
            "team2": {
                "name": None,
                "odds": None
            }
        }
        url = "https://www.cloudbet.com/sports-api/c/v6/sports/competitions/league-of-legends-international-t673d-lck-cl-spring-season/events?markets=league_of_legends.winner&markets=league_of_legends.map_handicap&locale=en"
        x = requests.get(url)
        return x.text