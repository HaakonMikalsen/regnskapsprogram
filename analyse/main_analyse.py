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

    for reletivePath in lookUpData.values():
        # print(reletivePath)
        exspensValue =getItemExpenses(databasePath+reletivePath)
        if exspensValue >0:
            if reletivePath!= "/utgifter/annet/leie.json":
                totalSum +=exspensValue
    
    print(totalSum)



if __name__ == "__main__":
    getTotalExspenses()
    print( getItemExpenses(databasePath+loadData(lookUpTablePath)["leie"]))
    pass
