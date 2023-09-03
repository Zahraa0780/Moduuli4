import random

arvattu_luku = random.randint(1, 10)
yritykset = 0

while True:
    arvaus = int(input("Arvaa luku (1-10): "))
    yritykset += 1
    if arvaus > arvattu_luku:
        print("Liian suuri arvaus.")
    elif arvaus < arvattu_luku:
        print("Liian pieni arvaus.")
    else:
        print("Oikein! Arvasit luvun", arvattu_luku, "yrityksellä", yritykset)
        break
