import os
import json
import datetime

current_file_directory = os.path.dirname(os.path.abspath(__file__))
databasePath = current_file_directory + "/data/dataBase"
lookUpTablePath = databasePath + "/lookup.json"
placePath = databasePath + "/steder.json"


def space(spacing=2):
    print("\n"*spacing)
    print("-"*20)
    print("\n"*spacing)
    

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


def addPlace(placeName):
    data = loadWholeFile(placePath)
    if (placeName in data["data"]) == False:
        data["data"].append(placeName)
        with open(placePath, "w") as file:
            json.dump(data, file)


def addLookUp(name, path):
    data = loadWholeFile(lookUpTablePath)
    data["data"][name] = path
    with open(lookUpTablePath, "w") as file:
        json.dump(data, file)


def addItem(folderPath, name, pris, dato, sted):
    BASEFORMATFILEPATH = databasePath + "/emptyDataSet.json"
    newFilePath = folderPath + "/" + name + ".json"
    data = loadWholeFile(BASEFORMATFILEPATH)
    nyData = {"pris": pris, "dato": dato, "sted": sted}
    data["data"].append(nyData)
    data["navn"] = name
    with open(newFilePath, "w") as file:
        json.dump(data, file)

    addLookUp(name, newFilePath.replace(databasePath, ""))
    addPlace(sted)


# Get the directory where the Python file is located

lookUpTableData = loadData(lookUpTablePath)

# space()
# print(lookUpTableData)

# print(loadData(databasePath + lookUpTableData["iste"]))
# # addPrice(databasePath + lookUpTableData["iste"],23,"24-07-2024","REMA")
# # addItem(databasePath + "/utgifter/annet/", "semesteravgift", 700, "2024-09-15", "NTNU")

# print(loadData(databasePath + lookUpTableData["iste"]))

print("Velkommen til regnskapsproggrammet :)")

dato = ""
while True:
    skriveInn = input("Hvilken dato? (idag / annnet)(i/a)")
    if skriveInn == "i":
        dato = datetime.date.today()
        break
    if skriveInn =="a":
        fail =0
        
        dag = input("hvilken dag?") 
        maande = input("hvilken mående?") 

        try:
            dag = int(dag)
            dag = str(dag)
            if len(dag)!=2:
                dag = "0"+dag
        except:
            fail +=1 
        
        try:
            maande = int(maande)
            maande = str(maande)
            if len(maande)!=2:
                maande = "0"+maande
        except:
            fail +=1 
        
        if fail==0:
            dato =f"{datetime.date.today().strftime('%Y')}-{maande}-{dag}"
            break
    print("ikke akkseptert input")

print(dato)

# space()

# while True:

    

print("slutt")
while input("") !="":
    pass
