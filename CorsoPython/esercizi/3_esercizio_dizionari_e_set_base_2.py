"""
Lo Chef ti ha lanciato il foglio con gli ordini del pranzo (comande)
e ti ha chiesto di preparare immediatamente la linea per la cucina;
il tuo script deve analizzare gli ordini per stampare un resoconto che dica ai
cuochi esattamente quanti piatti preparare per ogni tipo (es. "3 Carbonara"),
e contemporaneamente deve consultare il ricettario per generare una "Lista della Spesa"
contenente l'elenco di tutti gli ingredienti grezzi necessari per coprire il servizio,
assicurandosi che nella lista ogni ingrediente compaia una volta sola
(non importa se il Pecorino serve per 3 ricette diverse,
nella lista deve apparire solo come "Pecorino").
"""

ricettario = {
    "Carbonara": ["Guanciale", "Uova", "Pecorino", "Pepe"],
    "Amatriciana": ["Guanciale", "Pomodoro", "Pecorino", "Peperoncino"],
    "Cacio e Pepe": ["Pecorino", "Pepe"],
    "Gricia": ["Guanciale", "Pecorino", "Pepe"]
}

comande = [
    "Carbonara",
    "Amatriciana",
    "Carbonara",
    "Cacio e Pepe",
    "Carbonara",
    "Gricia",
    "Amatriciana"
]

# 1 prepariamo resoconto delle ricette da preparare
# definiamo un dizionario vuoto in cui metteremo le coppie piatto: numero da
# preparare
diz_resoconto = {}

for comanda in comande:
    # per ogni comanda aggiorniamo il contatore che teneva conto di quanti piatti
    # del suo tipo ci sono da fare

    # Cerchiamo di ottenere il numero di volte che il piatto attuale è già comparso facendo il for.
    # Per fare questo usiamo il metodo dei dizionari ".get()" che, se trova la chiave richiesta all'interno del
    # dizionario, restituisce il valore associato, altrimenti un valore di default.
    # Nel nostro caso, il valore di default è 0, perchè se la chiave non è presente nel dizionario, non abbiamo ancora
    # visto quel piatto.
    conteggio_piatto = diz_resoconto.get(comanda, 0)

    # siccome abbiamo trovato una nuova richiesta per il piatto attuale
    # incrementiamo di 1 il contatore
    conteggio_piatto += 1 # conteggio_piatto = conteggio_piatto + 1

    # aggiorniamo il dizionario del resoconto per tenere traccia di quante
    # volte il piatto è comparso all'interno della lista
    diz_resoconto[comanda] = conteggio_piatto # se la chiave c'era gia,
    # va a sovrascrivere il valore che c'era assegnato
    #[che quindi risulterà incrementato di 1]
    # altrimenti crea una nuova coppia "comanda": conteggio_piatto =
    # "comanda": 1

print("Resoconto dei piatti da preparare: ")
for nome_piatto, n_da_preparare in diz_resoconto.items():
    print(f" * {nome_piatto}: {n_da_preparare}")



# 2 prepariamo lista della spesa
# capiamo qual è l'elenco completo di tutti gli ingredienti
# capiamo quali ingredienti unici dobbiamo comprare
