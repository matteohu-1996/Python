# facciamo un programma che controlli l'età del cliente e l'orario del giorno
# per verificare se possiamo o no vendergli alcolici

# definiamo le regole:
# - dopo le 21 non si vendono alcolici a nessuno
# - si vendono alcolici solo chi ha almeno 18 anni
MAGGIOREETA = 18 # età a cui diamo alcolici
ORARIO_CONSENTITO = 21 # orario prima che diamo alcoli

eta_cliente = 19
orario = (0, 40) #tupla orario (ore, minuti)

if orario[0] < ORARIO_CONSENTITO:
    if eta_cliente >= MAGGIOREETA:
        print("serviamo alcolici al cliente")
    else:
        print("non serviamo alcoli ai minorenni")
else:
    print("dopo le 21 non serviamo alcolici")
print()

# versione 2
# lo stato ha deciso che l'orario massimo di servizio degli alcolici è di 21:30
print("-" * 50)

# orario_rispettato = orario[0] < 21 or (orario[0] == 21 and orario[1] < 30 )
ORARIO_DA_RISPETTARE = 21 * 60 + 30 # ore convertite in minuti(*60) + minuti
# dell'orario
orario_convertito = orario[0] * 60 + orario[1]

orario_rispettato = orario_convertito < ORARIO_DA_RISPETTARE
if orario_rispettato:
    if eta_cliente >= MAGGIOREETA:
            print("serviamo alcolici al cliente")
    else:
            print("non serviamo alcoli ai minorenni")
else:
        print("dopo le 21:30 non serviamo alcolici")

print("-" * 50)
# todo: aggiustiamo il programma per fornire alcolici solamente dalle 8:30
#  alle 21:30

# variabili/costati
ORARIO_MASSIMO_DA_RISPETTARE = 21 * 60 + 30 # ore convertite in minuti(*60) +
# minuti
ORARIO_MINIMO_DA_RISPETTARE = 8 * 60 + 30

# ci chiediamo se l'orario convertito è compreso tra i due consentiti
orario_rispettato = (ORARIO_MINIMO_DA_RISPETTARE <= orario_convertito <
                     ORARIO_MASSIMO_DA_RISPETTARE)
# orario_rispettato = (orario_convertito >= ORARIO_MINIMO_DA_RISPETTARE and
# orario_convertito)) < ORARIO_MASSIMO_DA_RISPETTARE)
if orario_rispettato:
    if eta_cliente >= MAGGIOREETA:
            print("serviamo alcolici al cliente")
    else:
            print("non serviamo alcoli ai minorenni")
else:
        print(f"Sono le {orario[0]}:{orario[1]}. Fornniamo alcol solo dalle 8:30 alle 21:30")