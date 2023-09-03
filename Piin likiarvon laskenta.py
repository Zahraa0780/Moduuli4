import random

pisteiden_maara = int(input("Anna arvottavien pisteiden määrä: "))

n = 0  # Ympyrän sisälle jäävien pisteiden laskuri

for _ in range(pisteiden_maara):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1

pi_likiarvo = 4 * n / pisteiden_maara
print("Piin likiarvo on noin", pi_likiarvo)
