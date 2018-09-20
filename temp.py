import datetime


def get_month(num):
    return num if num > 0 else (12 + num)


print("Hello~")
BDY = input("Birthday:year")
BDM = input("Birthday:month")
BDD = input("Birthday:date")
today = datetime.date.today()
print(str(today.year - int(BDY)) + " years old")

print(get_month(datetime.date(int(BDY), int(BDM), int(BDD)).month - today.month))

