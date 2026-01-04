from conto_corrente import ContoCorrente
from filiale import Filiale

# 1. creiamo la filiale
filiale1= Filiale("Filiale di Torino", "Aldo Baglio")

# 2. creiamo un conto corrente all'interno della filiale
filiale1.crea_conto("Sara Neri",1_000)
print(filiale1)

# 3. creiamo un conto corrente come oggetto
mio_conto = ContoCorrente(1500,"Daniele Cerrina")

#4. trasferiamo il conto nella filiale
filiale1.trasferisci_conto(mio_conto)


if filiale1.trasferisci_conto(mio_conto):
    print("Conto trasferito")
else:
    print("il conto è già presente")
print(filiale1)
print(f"Saldo di tutti i conti correnti registrati: {filiale1.deposito_totale()}")

