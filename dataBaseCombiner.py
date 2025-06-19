"""



 DONTT RUN!









"""




# import os
# import json
# import datetime
# import main as dbFunctions


main_db_current_file_directory = os.path.dirname(os.path.abspath(__file__))
main_db_databasePath = main_db_current_file_directory + "/data/dataBase"
main_db_lookUpTablePath = main_db_databasePath + "/lookup.json"
main_db_placePath = main_db_databasePath + "/steder.json"


secondary_db_current_file_directory = os.path.dirname(os.path.abspath(__file__))
secondary_db_databasePath = secondary_db_current_file_directory + "/dataBaseMergeConflicFolder/dataBase"
secondary_db_lookUpTablePath = secondary_db_databasePath + "/lookup.json"
secondary_db_placePath = secondary_db_databasePath + "/steder.json"

new_db_current_file_directory = os.path.dirname(os.path.abspath(__file__))
new_db_databasePath = new_db_current_file_directory + "/newDataBase/dataBase"
new_db_lookUpTablePath = new_db_databasePath + "/lookup.json"
new_db_placePath = new_db_databasePath + "/steder.json"


main_lookUpData = dbFunctions.loadData(main_db_lookUpTablePath)
secondary_lookUpData = dbFunctions.loadData(secondary_db_lookUpTablePath)


addedItems = []


# newLookUpList = []
# itemList =[]


# print(dbFunctions.loadData(main_db_lookUpTablePath))


# #combine lookUps
# lookUpDataMain : dict = dbFunctions.loadData(main_db_lookUpTablePath) 

# for key,value in lookUpDataMain.items():
#     listing = [key,value]
#     if listing != newLookUpList:
#         newLookUpList.append(listing)

# lookUpDataSecondary : dict = dbFunctions.loadData(secondary_db_lookUpTablePath) 
# for key,value in lookUpDataSecondary.items():
#     listing = [key,value]
#     if listing != newLookUpList:
#         newLookUpList.append(listing)


# # clear data for new database
# data = dbFunctions.loadWholeFile(new_db_lookUpTablePath)
# data["data"] = {}
# with open(new_db_lookUpTablePath, "w") as file:
#     json.dump(data, file)


lookUpDataMain : dict = dbFunctions.loadData(main_db_lookUpTablePath) 

for name,basePath in lookUpDataMain.items():
    basePath = basePath.replace("/home/hakmik/Documents/programmering/python/regnskapsprogram/newDataBase/dataBase","")
    oldItemPath = main_db_databasePath+basePath
    newItemPath = new_db_databasePath+basePath
    # print(basePath)
    # print(oldItemPath)
    # print(newItemPath)
    # print(newItemPath.replace(f"{name}.json",""))
    itemData = dbFunctions.loadData(oldItemPath)
    if (name in addedItems) == False:
        # print("new item 1")
        addedItems.append(name)
        dbFunctions.addItem(newItemPath.replace(f"{name}.json",""),name,itemData[0]["pris"],itemData[0]["dato"],itemData[0]["sted"],new_db_databasePath)
        for item in itemData[1:]:
            dbFunctions.addPrice(newItemPath,item["pris"],item["dato"],item["sted"])
    else:
        for item in itemData:
            dbFunctions.addPrice(newItemPath,item["pris"],item["dato"],item["sted"])


lookUpDataSecondary : dict = dbFunctions.loadData(secondary_db_lookUpTablePath) 

for name,basePath in lookUpDataSecondary.items():
    # basePath = basePath.replace("/home/hakmik/Documents/programmering/python/regnskapsprogram/newDataBase/dataBase","")
    oldItemPath = secondary_db_databasePath+basePath
    newItemPath = new_db_databasePath+basePath
    # print(basePath)
    # print(oldItemPath)
    # print(newItemPath)
    # break
    itemData = dbFunctions.loadData(oldItemPath)
    if (name in addedItems) == False:
        addedItems.append(name)
        dbFunctions.addItem(newItemPath.replace(f"{name}.json",""),name,itemData[0]["pris"],itemData[0]["dato"],itemData[0]["sted"],new_db_databasePath)
        # print("new item 2")
        for item in itemData[1:]:
            dbFunctions.addPrice(newItemPath,item["pris"],item["dato"],item["sted"])
    else:
        for item in itemData:
            dbFunctions.addPrice(newItemPath,item["pris"],item["dato"],item["sted"])


lookUpDataNew : dict = dbFunctions.loadData(new_db_lookUpTablePath)
print(addedItems)
print(len(addedItems))
print(len(lookUpDataMain))
print(len(lookUpDataSecondary))
print(len(lookUpDataNew))



for name, lookupPath in lookUpDataNew.items():
    itemPath = new_db_databasePath+lookupPath
    wholeItemFile = dbFunctions.loadWholeFile(new_db_databasePath+lookupPath)
    itemData = wholeItemFile["data"]
    # print(itemData)
    # print(new_db_databasePath+ lookupPath)
    # break
    dateList = []
    newItemData = []
    for dataPoint in itemData:
        if dataPoint["dato"] not in dateList:
            dateList.append(dataPoint["dato"])
            newItemData.append(dataPoint)
    wholeItemFile["data"] = newItemData
    with open(itemPath, "w") as file:
        json.dump(wholeItemFile, file)
    