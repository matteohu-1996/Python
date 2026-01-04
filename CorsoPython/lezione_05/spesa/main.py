from prodotto import Prodotto
from carrello import Carrello
import json
import random

with open("prodotti.json") as file_in: # apriamo il nostro file e chiamiamo
# il collegamento con il file "file_in"
    prodotti_raw = json.load(file_in) # usiamo la libreria JSON per leggere
# il contenuto del file e convertirlo in dizionario, in risultato lo mettiamo
# in "prodotti_raw"

# creiamo l'elenco dei prodotti di classe "Prodotto"
elenco_prodotti = [Prodotto.from_dict(prod) for prod in prodotti_raw] # List
# comprehension
#for prod in prodotti_raw:
#    elenco_prodotti.append(Prodotto.from_dict(prod))
#for prod in elenco_prodotti:
#    print(prod)

# 1. scegliere casualmente un numero n di prodotti da aggiungere al carrello
n = random.randint(1, len(elenco_prodotti))
print(f"Cercheremo di prendere {n} prodotti")

# 2. scegliere casualmente n prodotti dalla lista e metterli nel carrello
prodotti_scelti = random.sample(elenco_prodotti, n) # per sceglierli tutti
# diversi
#prodotti_scelti = random.choices(elenco_prodotti, k=n) # per sceglierli a
# caso con possibili duplicati

mio_carrello= Carrello(24) # todo: scegliere casualmente il budget (float)

for prod in prodotti_scelti:
    aggiunto = mio_carrello.aggiungi(prod)
    if aggiunto: # todo: gestire all'interno della classe carrello tutti i
        # possibili errori
        print(f"Il prodotto {prod.nome} è stato aggiunto al carrello")
    else:
        print(f"Il prodotto {prod.nome} non è stato aggiunto al carrello")

# 3. stampare il carrello risultato
print(mio_carrello)
