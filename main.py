import os
import json
import datetime

current_file_directory = os.path.dirname(os.path.abspath(__file__))
databasePath = current_file_directory + "/data/dataBase"
lookUpTablePath = databasePath + "/lookup.json"
placePath = databasePath + "/steder.json"


def finnPath():
    newItemPath = databasePath + "/utgifter"
    directories = [
        d
        for d in os.listdir(newItemPath)
        if os.path.isdir(os.path.join(newItemPath, d))
    ]
    while len(directories) != 0:
        valg = 0
        for i in range(len(directories)):
            print(f"{i}:{directories[i]}")
        while True:
            valg = input(f"Skriv inn hvor den skal ligge(0-{len(directories)-1}) ")
            try:
                valg = int(valg)
                if 0 <= valg <= (len(directories) - 1):
                    break
            except:
                print(
                    "Ser ut som du ikke skrev inn et tall eller tallet var for stort :("
                )
        newItemPath += "/" + directories[valg]
        directories = [
            d
            for d in os.listdir(newItemPath)
            if os.path.isdir(os.path.join(newItemPath, d))
        ]
    print(newItemPath)
    return newItemPath


def space(spacing=1):
    print("\n" * spacing)
    print("-" * 20)
    print("\n" * spacing)


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


# print(finnPath())

# overide mode:
# overide = True
# overidePlace = "REMA"
# normal mode:
overide = False
overidePlace = "REMA"



if __name__ == "__main__":

    print("Velkommen til regnskapsproggrammet :)")

    dato = ""
    while True:
        skriveInn = "a"
        if  not overide:
            skriveInn = input("Hvilken dato? (idag / annnet)(i/a)")
        if skriveInn == "i":
            dato = datetime.date.today().strftime('%Y-%m-%d')
            break
        if (skriveInn == "a") or (skriveInn ==""):
            fail = 0

            dag = input("hvilken dag?")
            maande = input("hvilken mående?")

            try:
                dag = int(dag)
                dag = str(dag)
                if len(dag) != 2:
                    dag = "0" + dag
            except:
                fail += 1

            try:
                maande = int(maande)
                maande = str(maande)
                if len(maande) != 2:
                    maande = "0" + maande
            except:
                fail += 1

            if fail == 0:
                dato = f"{datetime.date.today().strftime('%Y')}-{maande}-{dag}"
                break
        print("ikke akkseptert input")
    
    # *dato, = dato
    # dato[3] = "4"
    # dato = "".join(dato)
    print(dato)

    space()

    sted = ""
    if not overide:
        while True:
            print("Her er en liste med steder")
            placedata = loadData(placePath)
            while True:
                for place in placedata:
                    print(place)
                sted = input("skriv inn sted: ")
                if (sted in placedata) == False:
                    rett = input("Du skrev inn nytt sted, er dette rett?(y/n) ")
                    if rett == "y":
                        addPlace(sted)
                        break
                if sted in placedata:
                    break
            break
    else:
        sted = overidePlace

    space()
    print("den er grei")
    prissum = 0
    isExiting = False
    while isExiting == False:
        while True:
            pris = ""
            ting = input("Prissum "+str(prissum)+"kr. Skriv inn varenavn eller n for å avlsutte: ")
            if ting == "n":
                isExiting = True
                break
            if ting == "":
                isExiting = True
                break
            skip = False
            if (ting in lookUpTableData) == False:
                rett = input(
                    "ser ut som du skrev et produkt som ikke er lagt inn. Er dette rett?(y/n): "
                )
                skip = True
                if rett == "y":
                    nyPath = finnPath()
                    while True:
                        pris = input("Skriv inn pris: ")
                        try:
                            pris = pris.replace(",",".")
                            pris = float(pris)
                            prissum+=pris
                            break
                        except:
                            print("Ser ut som du ikke skrev inn et tall :(")
                    addItem(nyPath, ting, pris, dato, sted)
                    lookUpTableData = loadData(lookUpTablePath)

            if skip == False:
                while True:
                    pris = input("Skriv inn pris: ")
                    try:
                        pris = pris.replace(",",".")
                        pris = float(pris)
                        prissum+=pris
                        break
                    except:
                        print("Ser ut som du ikke skrev inn et tall :(")
                addPrice(databasePath+lookUpTableData[ting], pris, dato, sted)


    print(dato)
    print(sted)

    print("slutt")
    while input("") != "":
        pass
