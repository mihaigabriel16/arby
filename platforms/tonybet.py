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

def fetchTranslations():
    url = "https://tonybet.com/api/translation/get?locale=en_GB"
    x = requests.get(url)
    data = x.text

def filterGames(data):
    data = json.loads(data)
    for item in data["items"]:
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

def getTeamNames(leagueId, gameId, engslug):
    url = "https://tonybet.com/en/api/seo/get-data?pageUrl=/en/prematch/league-of-legends/"+leagueId+"/"+gameId+"-"+engslug
    x = requests.get(url)
    object = {
        "team1": None,
        "team2": None
    }
