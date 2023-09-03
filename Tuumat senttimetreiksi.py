while True:
    tuumat = float(input("Anna tuumat (negatiivinen luku lopettaa): "))
    if tuumat < 0:
        break
    senttimetrit = tuumat * 2.54
    print(tuumat, "tuumaa on", senttimetrit, "senttimetriä.")
