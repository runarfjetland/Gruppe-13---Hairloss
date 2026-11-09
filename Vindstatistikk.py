from statistics import median
import matplotlib.pyplot as plt
vind_per_maaned = {maaned: [] for maaned in range(1, 13)}

with open("sinnes_2014_2025.csv", encoding="utf-8") as fil:
    next(fil)

    for linje in fil:
        deler = linje.strip().split(";")
        dato = deler[2]
        vindtekst = deler[5].strip()

        if vindtekst in ("-", ""):
            continue

        vind = float(vindtekst.replace(",", "."))
        maaned = int(dato.split(".")[1])
        vind_per_maaned[maaned].append(vind)
        
maaneder = []
minimum = []
medianer = []
maksimum = []

for maaned in range(1, 13):
    maalinger = vind_per_maaned[maaned]

    if not maalinger:
        continue

    maaneder.append(maaned)
    minimum.append(min(maalinger))
    medianer.append(median(maalinger))
    maksimum.append(max(maalinger))

plt.plot(maaneder, minimum, marker="o", label="Minimum")
plt.plot(maaneder, medianer, marker="o", label="Median")
plt.plot(maaneder, maksimum, marker="o", label="Maksimum")

plt.xticks(range(1, 13))
plt.xlabel("Måned")
plt.ylabel("Vindstyrke (m/s)")
plt.title("Månedlig vindstatistikk for Sinnes")
plt.legend()
plt.show() 