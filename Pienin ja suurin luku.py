lukulista = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luku = float(syote)
    lukulista.append(luku)

if len(lukulista) > 0:
    pienin = min(lukulista)
    suurin = max(lukulista)
    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)
else:
    print("Et antanut yhtään lukua.")
