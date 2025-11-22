# ripetiamo un blocco di codice 5 volte
from statistics import median

from lezione_02.esempi_dizionari import dizionario_spese

for i in range(5):
    print(f"il contatore 'i' vale {i}")

# creiamo una lista
lista_mesi = ["gen", "feb","mar","apr","mag","giu","lug",]

#stampiamo un elenco numerato
for i in range(len(lista_mesi)): # da 0 alla lista lunghezza della lista (-1)
    print(f"{i + 1}: {lista_mesi[i]}")

lista_costi = [
    [12, 23, 10], # elemento della lista
    [45, 12, 7],
    [34, 75, 3],
]

# per ogni lista di costi calcoliamo la media
for lista_mensile in lista_costi: # per ogni elemento della lista costi
    print(f"media: {sum(lista_mensile) / len(lista_mensile):.2f}")

for indice, lista_mensile in enumerate(lista_costi):
    print(f"media elemento alla posizione {indice + 1}:"
          f" {sum(lista_mensile) / len(lista_mensile):.2f}")
print("\n")
# -------------------------------------------------------------------

# definiamo un dizionario di spese
dizionario_spese = {
    "gen" : [23, 54, 23, 6],
    "feb": [56, 12, 23],
    "mar": [10, 54, 245, 45],
    "apr": [69],
    "mag": [78, 54, 12, 6, 7 ,9],
    "giu": [18, 120, 3, 45],
}

# stampiamo elenco mesi che fanno parte del dizionario
for mese in dizionario_spese.keys():
    print(f"* {mese}")
print()
# stampiamo elenco delle spese che fanno parte del dizionario
for spese in dizionario_spese.values():
    print(f"* {spese}")

#calcoliamo per ogni mese la spesa totale e spesa media
for mese, spese in dizionario_spese.items():
    tot = sum(spese)
    media = tot / len(spese)
    spesa_max = max(spese)
    spese_min = min(spese)
    print(f" * massima: {spesa_max:.2f}")
    print(f" * minima: {spese_min:.2f}")
    print(f"spese di {mese}")
    print(f" * media: {media:.2f}")
    print(f" * totale: {tot:.2f}")
