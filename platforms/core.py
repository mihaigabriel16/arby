import platforms.esportsbet as EB
import platforms.cloudbet as CB
import platforms.thunderpick as TP
import platforms.luckbox as LBX
import platforms.rivalry as RV
import platforms.lootbet as LBT
import platforms.tonybet as TB
import platforms.betibet as BB
import configs
import requests
import base64
import json
import validators
from pathlib import Path
from datetime import datetime



data = [BB.getGames(),
        CB.getGames(), 
        EB.getGames(), 
        TP.getGames(),
        RV.getGames(),
        LBX.getGames(),
        LBT.getGames()]


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
                    if arb < configs.MINARB:
                        sap = calculateStakesAndProfit(oddsA, oddsB)
                        L = ["Team1: " + home + " " + str(oddsA) + " / " + i["platform"] + " / STAKE: $" + str(sap["stake_a"]) + "\n",
                             "Team2: " + away + " " + str(oddsB) + " / " + j["platform"] + " / STAKE: $" + str(sap["stake_b"]) + "\n",
                             "Total Profit: " + str(sap["roi"]) + "% -> $" + str(float(sap["roi"])*float(configs.STAKE)/100) + "\n",
                             str(formatDec(arb)) + "%"  + "\n",
                             "---------------------------------------------------------- \n"]
                        for line in L:
                            configs.TXTARRAY.append(line)
                            print(line)

def printData(text_data):
    path = "runs/" + str(configs.TXTNAME) + ".txt"
    f = open(path, "w")
    f.writelines(text_data)
    f.close()

def getDateTime():
    now = datetime.now()
    txtname = now.strftime("%d-%m-%Y %H-%M-%S")
    return txtname
def formatDec(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')
def calculateStakesAndProfit(a, b):
    total = a + b
    stk = configs.STAKE
    arb = (1/a + 1/b)*100
    roi = 100 - arb
    object = {
        "stake_a": formatDec(b * stk / total),
        "stake_b": formatDec(a * stk / total),
        "roi": formatDec(roi)
    }
    return object



def getArb():
    configs.TXTNAME = getDateTime()
    loopArray(data)
    printData(configs.TXTARRAY)
    sendDiscordNotif()

def sendDiscordNotif():
    list = getWebhooks()
    for item in list:
        valid = validators.url(item)
        if valid:
            body = {
                "embeds": [{
                    "description": formatText(configs.TXTARRAY)
                    }]
                }
            requests.post(item, json=body)

def getWebhooks():
    url = "https://frjcaqhnfgsyzdwyvszc.functions.supabase.co/arby-webhooks"
    x = requests.post(url)
    list = []
    data = json.loads(base64.b64decode(x.text).decode('utf-8'))
    for item in data["data"]:
        list.append(item["url"])
    return list

def verifyWebhook():
    pass

def formatText(data):
    text = ""
    for line in data:
        text += line
    return text