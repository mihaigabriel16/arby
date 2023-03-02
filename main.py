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