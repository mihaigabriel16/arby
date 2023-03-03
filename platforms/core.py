import platforms.esportsbet as EB
import platforms.cloudbet as CB
import platforms.thunderpick as TP
import platforms.luckbox as LB
import platforms.rivalry as RV
import configs

data = [CB.getGames(), 
        EB.getGames(), 
        TP.getGames(),
        LB.getGames(),
        RV.getGames()]


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
                        sap = calculateStakesAndProfit(oddsA, oddsB)
                        print("Team1: " + home + " " + str(oddsA) + " / " + i["platform"] + " / STAKE: " + str(sap["stake_a"]))
                        print("Team2: " + away + " " + str(oddsB) + " / " + j["platform"] + " / STAKE: " + str(sap["stake_b"]))
                        print("Total Profit: " + str(sap["roi"]))
                        print(str(arb) + "%")
                        print("----------------------------------------------------------")

def calculateStakesAndProfit(a, b):
    total = a + b
    stk = configs.STAKE
    arb = (1/a + 1/b)*100
    roi = 100 - arb
    object = {
        "stake_a": b * stk / total,
        "stake_b": a * stk / total,
        "roi": roi
    }
    return object

def getArb():
    loopArray(data)