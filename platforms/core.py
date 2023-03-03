import platforms.esportsbet as EB
import platforms.cloudbet as CB
import platforms.thunderpick as TP
import platforms.luckbox as LB

data = [CB.getGames(), 
        EB.getGames(), 
        TP.getGames(),
        LB.getGames()]


def loopArray(arr):
    for i in arr:
        for j in arr:
            if i["platform"] != j["platform"]:
                runArb(i, j)

def runArb(i, j):
    a = i["data"]
    b = j["data"]
    for m in a:
        home = m["team1"]["name"]
        away = m["team2"]["name"]
        for n in b:
            if n["team1"]["name"] == home and n["team2"]["name"] == away:
                oddsA = m["team1"]["odds"]
                oddsB = n["team2"]["odds"]
                if oddsA != None and oddsB != None:
                    arb = (1/oddsA + 1/oddsB)*100
                    if arb < 100:
                        print("Team1: " + home + " " + str(oddsA) + " / " + i["platform"] )
                        print("Team2: " + away + " " + str(oddsB) + " / " + j["platform"])
                        print(str(arb) + "%")
                        print("----------------------------------------------------------")

def getArb(stake):
    loopArray(data)