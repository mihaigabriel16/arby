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
    url = "https://sportservice.inplaynet.tech/api/prematch/getprematchgameall/en/28/?games=,27534785,27659013,27659024,27688072,27703473,27703474,27703476,27706452,27754980,27759863,27800709,27804784,27805394,27806634,27806635,27806636,27806637,27806638,27808203,27808204,27808205,27808208,27808315,27808316,27808317,27808456,27808458,27808459,27808460,27808461,27808462,27808463,27809841,27809842,27814482,27814483,27814484,27816192,27816491,27817671,"
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

