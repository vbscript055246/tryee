import random

color = ["♠", "♥", "♣", "♦"]
num = ["-1", "A", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "J", "Q", "K"]


class card:

    def __init__(self, c, n):
        self.color = c
        self.number = n

    def __str__(self):
        return color[self.color] + str(num[self.number] if num[self.number] != "-1" else self.number)


cards = []
for i in range(51):
    cards.append(i)

for i in range(51):
    index = cards[random.randint(0, 51-i)]
    cards.remove(index)
    cards.append(index)

R_cards = []
for item in cards:
    R_cards.append(card(int(item/13), item % 13 + 1))

for item in R_cards:
    print(item)
