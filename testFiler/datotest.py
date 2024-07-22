import datetime
#https://realpython.com/python-datetime/


# print(datetime.date(year=2020, month=1, day=31))
# print(datetime.time(hour=13, minute=14, second=31))
# print(datetime.datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31))

print("test med hente ut dato")
print("")
datoIdag =datetime.date.today() 
print(datoIdag)
print("-"*20)
print(datoIdag.strftime("%d"))
print(datoIdag.strftime("%m"))
print(datoIdag.strftime("%y")+"/"+datoIdag.strftime("%Y"))
print("-"*20)
print(datoIdag.isocalendar())
print("Ukenummer"+":"+str(datoIdag.isocalendar()[1]))
print("-"*20)




print("\n"*2)
print("test med str som dato")
print("")
datoStr = "2024-07-23"
datoStr = datetime.date.fromisoformat(datoStr) #må brukes for å gjøre string til datetime obkjekt
print(datoStr)
print("-"*20)
print(datoStr.strftime("%d"))
print(datoStr.strftime("%m"))
print(datoStr.strftime("%y")+"/"+datoStr.strftime("%Y"))
print("-"*20)
print(datoStr.isocalendar())
print("Ukenummer"+":"+str(datoStr.isocalendar()[1]))
