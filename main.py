import os
import json


def loadData(path):
    data = open(path, "r")
    data = json.load(data)["data"]
    return data


def loadWholeFile(path):
    data = open(path, "r")
    data = json.load(data)
    return data


def addPrice(path, pris, dato, sted):
    data = loadWholeFile(path)
    nyData = {"pris": pris, "dato": dato, "sted": sted}
    data["data"].append(nyData)
    with open(path, "w") as file: 
        json.dump(data, file)


# Get the directory where the Python file is located
current_file_directory = os.path.dirname(os.path.abspath(__file__))
databasePath = current_file_directory + "/data/dataBase"
lookUpTablePath = databasePath + "/lookup.json"

lookUpTableData = loadData(lookUpTablePath)

print(lookUpTableData)

print(loadData(databasePath + lookUpTableData["iste"]))
# addPrice(databasePath + lookUpTableData["iste"],23,"24-07-2024","REMA")


# print(loadData(databasePath + lookUpTableData["iste"]))

