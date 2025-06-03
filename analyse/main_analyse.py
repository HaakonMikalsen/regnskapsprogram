import os
import json
import datetime

main_dir_path = os.path.dirname(os.path.abspath(__file__))+"/../"
databasePath = main_dir_path + "/data/dataBase"
lookUpTablePath = databasePath + "/lookup.json"
placePath = databasePath + "/steder.json"


def loadData(path):
    data = open(path, "r")
    data = json.load(data)["data"]
    return data


def loadWholeFile(path):
    data = open(path, "r")
    data = json.load(data)
    return data

def getItemExpenses(path,betweenDateStart="",betweenDateEnd=""):
    data = loadData(path)
    
    totalSum = 0

    for dataPoint in data:
        # print(dataPoint)
        totalSum+= dataPoint["pris"]
    # print(totalSum)
    return totalSum


def getTotalExspenses():
    lookUpData = loadData(lookUpTablePath)

    totalSum = 0
    banList = ["/utgifter/annet/leie.json","/utgifter/skjult/skjult.json"]
    for reletivePath in lookUpData.values():
        # print(reletivePath)
        exspensValue =getItemExpenses(databasePath+reletivePath)
        if exspensValue >0:
            if (reletivePath in banList) == False:
                totalSum +=exspensValue
    
    print(totalSum)

def getTotalExspensesAsList():
    lookUpData = loadData(lookUpTablePath)

    exspensList = []

    banList = ["/utgifter/annet/leie.json","/utgifter/skjult/skjult.json"]

    for reletivePath in lookUpData.values():
        # print(reletivePath)
        exspensValue =getItemExpenses(databasePath+reletivePath)
        if exspensValue >0:
            if reletivePath not in banList:
                name = reletivePath.split("/")[-1].replace(".json", "")
                exspensList.append([exspensValue,name])
    exspensList = sorted(exspensList, key=lambda x: x[0], reverse=True)
    return exspensList

if __name__ == "__main__":
    getTotalExspenses()
    # print( getItemExpenses(databasePath+loadData(lookUpTablePath)["brus"]))

    expspenses = getTotalExspensesAsList();
    for value in expspenses:
        print(f"{value[1]}|{value[0]}")
    pass
