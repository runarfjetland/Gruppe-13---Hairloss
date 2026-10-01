antall = 0
lengste = 0

start = ""
lengste_start = ""
lengste_slutt = ""

with open("sinnes_2014_2025.csv", encoding="utf-8") as fil:
    next(fil)

    for linje in fil:
        deler = linje.strip().split(";")
        dato = deler[2]
        if deler[4].strip() in ("-", ""):
            antall = 0
            continue

        nedbor = float(deler[4].replace(",", "."))

        if nedbor == 0:
            if antall == 0:
                start = dato

            antall += 1

            if antall > lengste:
                lengste = antall
                lengste_start = start
                lengste_slutt = dato
        else:
         antall = 0

print("Lengste periode uten nedbør:", lengste, "dager")
print("Startdato:", lengste_start)
print("Sluttdato:", lengste_slutt)