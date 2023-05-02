import json
import requests

data_array = []

def getGames():
    fetchGames()
    object = {
        "platform": "MYSTAKE",
        "data": data_array
    }
    return object

def fetchGames():
    url = "https://sportservice.inplaynet.tech/api/prematch/getprematchgameall/en/28/?games=,22924121,22958045,22958046,22958752,22958753,22958754,22959097,22974781,22974782,22978748,22993557,22993595,22995818,22996061,22996062,22996414,23003696,23003697,23003698,23003699,23003700,23003701,23003702,23003706,23003707,23005664,23005665,23005666,23005667,23005906,"
    x = requests.get(url)
    data = x.text
    data = data.replace('\\', '')
    prevchar = None
    newdata = None
    for char in data:
        if char == '"':
            i = char.find(char)
            print(i)
            n = i + 1
            print(n)
            if data[n] == "[":
                print("found")
                for j in range(len(data)):
                    if j != i:
                        newdata = newdata + data[j]
    #print(data)
    #return sortGames(data)

def sortGames(data):
    pass

