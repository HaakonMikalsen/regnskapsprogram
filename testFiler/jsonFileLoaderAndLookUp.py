import json
import os

# Get the directory where the Python file is located
current_file_directory = os.path.dirname(os.path.abspath(__file__))

path = current_file_directory +"/../"+"data/testData/dataEksempel1.json"

data = open(path, "r")
data = json.load(data)

lookUpData = data["lookup"]

def printLookUpList(lookUpData):
    index = 0
    for key in lookUpData.keys():
        print(f"{index} : {key}")
        index+=1
        
def lookUp(data,lookUpData,keyLookUp):
    prisData = data.copy()
    for key in lookUpData[keyLookUp]:
        prisData = prisData[key]
    return prisData

printLookUpList(lookUpData)

lookupInput = str(input("skriv inn det du vil skrive ut(str): "))

print(lookUp(data,lookUpData,lookupInput))

