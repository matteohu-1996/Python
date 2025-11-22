"""
La segreteria dell'evento ti ha passato l'export delle registrazioni web (lista registrazioni)
lamentandosi che il form ha permesso invii multipli creando dei duplicati;
il tuo compito è stampare a video la lista pulita dei partecipanti unici
(basandoti sulle loro email per distinguerli) per preparare i badge e, successivamente,
generare un piccolo report statistico che indichi quante persone partecipano per
ogni singola azienda, così da sapere chi sono i partner principali.
"""

registrazioni = [
    {"nome": "Alice", "azienda": "Google", "email": "alice@google.com"},
    {"nome": "Bob", "azienda": "Amazon", "email": "bob@amazon.com"},
    {"nome": "Alice", "azienda": "Google", "email": "alice@google.com"}, # Duplicato
    {"nome": "Charlie", "azienda": "Microsoft", "email": "charlie@ms.com"},
    {"nome": "David", "azienda": "Amazon", "email": "david@amazon.com"},
    {"nome": "Eve", "azienda": "Google", "email": "eve@google.com"},
    {"nome": "Bob", "azienda": "Amazon", "email": "bob@amazon.com"}, # Duplicato
    {"nome": "Frank", "azienda": "Facebook", "email": "frank@fb.com"}
]

# 1 creiamo un elenco di persone uniche che partecipano all'evento
# creiamo un set vuoto
set_partecipanti = set() # non usiamo {} per fare un set vuoto perchè per
# python sarebbe un dizionario vuoto
lista_partecipanti = [] # creiamo lista vuota in cui mettiamo partecipanti

# facciamo un ciclo attraverso le registrazioni
for registrazione in registrazioni:
    # se non abbiamo gia salvato la persona la salviamo
    if registrazione["email"] not in set_partecipanti: # ci chiediamo se la
        # mail non è all'interno con le mail presenti
        set_partecipanti.add(registrazione["email"]) # salviamo la mail per
        # prossimi controlli
        lista_partecipanti.append(registrazione) # salviamo tutti i dati del
        # nuovo partecipante
for indice, partecipazione in enumerate(lista_partecipanti):
    print(f"Partecipante {indice + 1}:")
    print(f"- Nome: {partecipazione["nome"]}")
    print(f"- Azienda: {partecipazione["azienda"]}")
    print(f"- Email: {partecipazione["email"]}")

print("----------------------------------------")

# 2 creiamo l'elenco di aziende con il numero partecipanti

# creiamo un dizionario vuoto in cui salviamo le coppie "azienda:
diz_affluenza_aziende = {} # creiamo dizionario vuoto che salviamo i conteggi
# per ogni azienda
# n:partecipanti_azienda"

# per ogni persona unica, aggiorniamo il contatore associato alla sua azienda
# nel dizionario
for partecipazione in lista_partecipanti:
    # se abbiamo gia visto l'azienda, prendiamo il dizionario alla chiave
# nome_azienda e incrementiamo il conteggio di 1
    # se non abbiamo mai visto l'azienda (all'interno di questo for), creiamo
# la coppia nome_azienda: 1
    nome_azienda = partecipazione["azienda"] # mettiamo nome dell'azienda in
    # una variabile

    #cerchiamo di ottenere il numero di persone viste finora che lavorano per
    # l'azienda attuale
    # se troviamo questa azienda nel dizionario, otteniamo il numero,
    # altrimenti, non avevamo ancora trovato nessuna persona che lavora per
    # questa azienda, quindi il contatore vale 0
    contatore_azienda = diz_affluenza_aziende.get(nome_azienda, 0)

    # siccome abbiamo trovato ora una persona in più che lavora per questa
    # azienda aumentiamo il contatore + 1
    contatore_azienda += 1 # contatore_azienda + 1

    # aggiorniamo il valore all'interno del dizionario
    diz_affluenza_aziende[nome_azienda] = contatore_azienda

# stampiamo il resoconto con le aziende partecipanti
for azienda, n_persone in diz_affluenza_aziende.items():

    print(f"per l'azienda {azienda} verrano {n_persone} persone")

