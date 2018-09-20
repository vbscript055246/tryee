import datetime

print("Hello~")
BDY = input("Birthday:year")
BDM = input("Birthday:month")
BDD = input("Birthday:date")
today = datetime.date.today().year

print(str(today - int(BDY)) + " years old")
print(datetime.date(int(BDY), int(BDM), int(BDD)).month)

