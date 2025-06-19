import os
import json
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


maaneder = {
    1: "Januar",
    2: "Februar",
    3: "Mars",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember"
}





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

def getExpensesPerDay():
    lookUpData = loadData(lookUpTablePath)

    
    datePriceDict:dict = {} # date (string): price (float) 

    banList = ["/utgifter/annet/leie.json","/utgifter/skjult/skjult.json"]


    for reletivePath in lookUpData.values():
        if reletivePath not in banList:
            itemData = loadData(databasePath+reletivePath)
            for entry in itemData:
                dato =entry["dato"]
                price = entry["pris"]
                if price<0:
                    continue
                if dato in datePriceDict:
                    datePriceDict[dato]+=price
                else:
                    datePriceDict[dato]=price

    datePriceList = []
    for key, val in datePriceDict.items():
        # print(key)
        if key == "2024-10-0228":
            key = "2024-10-28"
        date_obj = datetime.strptime(key, "%Y-%m-%d").date()
        datePriceList.append([date_obj, val])
    datePriceList.sort(key=lambda x: x[0])
    return datePriceList

def getExpensesPerMonth():
    lookUpData = loadData(lookUpTablePath)

    
    datePriceDict:dict = {} # date (string): price (float) 

    banList = ["/utgifter/annet/leie.json","/utgifter/skjult/skjult.json"]


    for reletivePath in lookUpData.values():
        if reletivePath not in banList:
            itemData = loadData(databasePath+reletivePath)
            for entry in itemData:
                dato =entry["dato"]
                price = entry["pris"]
                if price<0:
                    continue
                if dato in datePriceDict:
                    datePriceDict[dato]+=price
                else:
                    datePriceDict[dato]=price

    datePriceList = []
    for key, val in datePriceDict.items():
        # print(key)
        if key == "2024-10-0228":
            key = "2024-10-28"
        date_obj = datetime.strptime(key, "%Y-%m-%d").date()
        datePriceList.append([date_obj, val])
    datePriceList.sort(key=lambda x: x[0])


    monthYearPriceDict = {} # year numb : month numb : price numb

    for day in datePriceList:
        date =day[0]
        price = day[1]
        year = date.year
        month = date.month
        if year in monthYearPriceDict:
            if month in monthYearPriceDict[year]:
                monthYearPriceDict[year][month]+=price
            else:
                monthYearPriceDict[year][month]=price
        else:
            monthYearPriceDict[year] = {}
            monthYearPriceDict[year][month]=price

    currentIndex = 0
    plotData = [] # x val index , text, price
    for year,months in monthYearPriceDict.items():
        for month,price in months.items():
            plotData.append([currentIndex,f"{maaneder[month]},{year}",price])
            currentIndex+=1



    return plotData


if __name__ == "__main__":
    getTotalExspenses()
    # print( getItemExpenses(databasePath+loadData(lookUpTablePath)["brus"]))

    # expspenses = getTotalExspensesAsList();
    # for value in expspenses:
    #     print(f"{value[1]}|{value[0]}")

    # dateData = np.array(getExpensesPerDay()).T
    # print(dateData)
    # plt.bar(dateData[0],dateData[1])
    # plt.show()

    data = getExpensesPerMonth()
    # Skip first two entries if needed
    data = data[2:]

    # Extract columns with correct types
    x_indexes = [int(row[0]) for row in data]
    x_labels = [row[1] for row in data]
    y_values = [float(row[2]) for row in data]
    priceAvg = np.average(y_values)
    # Plot
    plt.bar(x_indexes, y_values)
    plt.xticks(x_indexes, x_labels, rotation=45)
    plt.tight_layout()
    plt.axhline(y=priceAvg,color = "red")
    plt.show()
    pass
