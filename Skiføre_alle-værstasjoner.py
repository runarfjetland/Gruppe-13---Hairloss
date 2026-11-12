
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filer = [
    "oslo_blindern_1954_2025_med_makstemperatur.csv",
    "roeros_1954_2025_med_makstemperatur.csv",
    "tromsoe_1954_2025_med_makstemperatur.csv",
    "vaernes_1954_2025_med_makstemperatur.csv",
    "venabu_1954_2025_med_makstemperatur.csv",
    "sinnes_2014_2025_med_makstemperatur.csv"
]

plt.figure(figsize=(12, 6))

for filnavn in filer:
    data = {}

    with open(filnavn, encoding="utf-8-sig") as fil:
        leser = csv.DictReader(fil, delimiter=";")
        navn = None

        for rad in leser:
            datotekst = rad["Tid(norsk normaltid)"]

            if not datotekst:
                continue

            try:
                dato = datetime.strptime(datotekst, "%d.%m.%Y")
            except ValueError:
                continue

            if navn is None:
                navn = rad["Navn"]

            if dato.month not in (11, 12, 1, 2, 3, 4):
                continue

            if dato.month >= 11:
                sesong = dato.year
            else:
                sesong = dato.year - 1

            if sesong not in data:
                data[sesong] = [0, 0]

          
            try:
                sno = float(rad["Snødybde"].replace(",", "."))
            except ValueError:
                continue

            data[sesong][0] += 1

            if sno >= 20:
                data[sesong][1] += 1

    godkjent = {}

    for sesong, tall in data.items():
        start = datetime(sesong, 11, 1)
        slutt = datetime(sesong + 1, 5, 1)
        antall_dager = (slutt - start).days

        if tall[0] >= antall_dager / 2:
            godkjent[sesong] = tall[1]

    if not godkjent:
        continue

    aar = list(range(min(godkjent), max(godkjent) + 1))
    skidager = [godkjent.get(a, float("nan")) for a in aar]

    plt.plot(aar, skidager, label=navn)

plt.xlabel("Skisesong (startår)")
plt.ylabel("Antall dager med skiføre")
plt.title("Antall dager med skiføre per skisesong")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()