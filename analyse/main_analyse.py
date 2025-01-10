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
        totalSum+= dataPoint["pris"]
    return totalSum


def getTotalExspenses():
    lookUpData = loadData(lookUpTablePath)

    totalSum = 0

    for reletivePath in lookUpData.values():
        totalSum +=getItemExpenses(databasePath+reletivePath)
    
    print(totalSum)



if __name__ == "__main__":
    getTotalExspenses()
    pass
