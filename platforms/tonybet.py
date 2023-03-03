import requests
import json

data_array = []

def getGames():
    fetchGames()
    object = {
        "platform": "TONYBET",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://platform.tonybet.com/api/event/list?sportId_eq=1067&competitor2Id_neq=&competitor1Id_neq=&oddsExists_eq=1&limit=100&main=1&status_in[]=0&relations[]=odds&relations[]=withMarketsCount&relations[]=result&relations[]=league&relations[]=competitors&relations[]=sportCategories&relations[]=tips&period=7&lang=en"
    x = requests.get(url)
    data = x.text  
    filterGames(data)

def fetchTranslations(): # WE ARE NOT USING THIS ONE
    url = "https://tonybet.com/api/translation/get?locale=en_GB"
    x = requests.get(url)
    data = x.text

def filterGames(data):
    data = json.loads(data)
    for item in data["data"]["items"]:
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
        id = item["id"]
        leagueId = item["leagueId"]
        engslug = item["translationSlug"]
        teamNames = getTeamNames(leagueId, id, engslug)
        object["key"] = teamNames["key"]
        object["team1"]["name"] = teamNames["team1"]
        object["team2"]["name"] = teamNames["team2"]
        for odd in data["data"]["relations"]["odds"]:
            if odd == id:
                for od in odd:
                    if od["id"] == 910:
                        object["team1"]["odds"] = od["outcomes"][0]["odds"]
                        object["team2"]["odds"] = od["outcomes"][1]["odds"]
        data_array.append(object)

def getTeamNames(leagueId, gameId, engslug):
    url = "https://tonybet.com/en/api/seo/get-data?pageUrl=/en/prematch/league-of-legends/"+str(leagueId)+"/"+str(gameId)+"-"+engslug
    x = requests.get(url)
    data = json.loads(x.text)
    object = {
        "key": None,
        "team1": None,
        "team2": None
    }
    item = data["data"]["structuredData"]
    teams = item[4]
    object["key"] = teams["organizer"]["name"]
    object["team1"] = teams["homeTeam"]["name"]
    object["team2"] = teams["awayTeam"]["name"]
    return object
