filnavn = "sinnes_2014_2025.csv"

datodag= input("Skriv inn årstall: ")
try:
    fil=open(filnavn)
except FileNotFoundError:
    print ("Fil finnes ikke")
    exit()

fil.readline()

dagerski=0

for linjenr, linje in enumerate(fil,start=2):
    if linjenr > 4294:
        break
    deler=linje.strip().split(";")
    if len(deler)> 6 and deler[2][-4:] == datodag:

        try:
            sum_snødybde = int(deler[6])
            if sum_snødybde >= 20:
                dagerski += 1
        except ValueError:
            continue
print (f"{dagerski} dager med godkjent skiføre")


    
    
    
    
    

    



