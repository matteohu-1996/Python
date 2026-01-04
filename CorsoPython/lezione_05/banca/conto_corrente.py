import random
from multiprocessing.util import is_abstract_socket_namespace

from lezione_01.esercizi_num_stringhe import numero_persone_servizio

# definiamo il seed di random
random.seed(42) # facciamo questa cosa per rendere riproducibili i nostri
# test e non avere ad ogni esecuzioni dei valori diversi

class ContoCorrente: # dichiariamo una nuova classe chiamata ContoCorrente
    # definiamo metodo costruttore
    def __init__(self, importo_iniziale: float, titolare: str): # unico metodo
# per definire il costruttore
        """
        inizializza un oggetto "ContoCorrente" con un importo iniziale e il
        nome completo del titolare
        :param importo_iniziale: importo di deposito iniziale in €
        :param titolare: nome e cognome del titolare es: "Daniele Cerrina"
"""

        self.importo = importo_iniziale # creiamo un attributo importo della
# nostra classe e ci assegniamo il valore passato dall'esterno dell'importo
# iniziale
        self.titolare = titolare # creiamo un attributo titolare della
# nostra classe e ci assegniamo il valore passato dall'esterno del nome del
# titolare
        self.iban = self.calcola_IBAN() # possiamo anche creare attributi da zero,
# senza input esterni
    def deposito(self, importo_da_depositare: float):
        """
        Prende un importo in € e lo aggiunge al saldo del conto corrente
        :param importo_da_depositare: Importo in €
        """
        self.importo += importo_da_depositare # aggiungiamo all'attributo
        # importo della nostra classe i soldi dell'importo da depositare

    def prelievo(self, importo_da_prelevare: float) -> bool:
        """
        dato un importo da prelevare, se possibile, lo toglie dal saldo del
        conto
        :param importo_da_prelevare: importo in €
        :return: True se riuscito, False altrimenti
        """
        if importo_da_prelevare > self.importo: # controlliamo che si possa
            # fare il prelievo
            return False # se non si può fare, interrompiamo la funzione
            # restituendo false
        # Se non abbiamo interrotto la funzione, vuol dire che il prelievo si
        # può fare, quindi scaliamo i soldi dal saldo del conto
        self.importo -= importo_da_prelevare
        return True

    def calcola_IBAN(self):
        iban = "IT"
        numero = random.randint(
            1_000_000_000_000_000_000_000_000,
                       9_999_999_999_999_999_999_999_999)
        return  f"{iban} {numero}"

    def __str__(self):
        #  NON METTIAMO MAI PRINT ALL'INTERNO DI QUESTO METODO
        output ="-" * 50 +"\n"
        output+= f"Titolare: {self.titolare}\n"
        output+= f"Importo: {self.importo}\n"
        output+= f"IBAN: {self.iban}\n"
        output += "-" * 50
        return output

    def __add__(self, other):
        #todo: implementare la variante della funzione per far funzionare  la
        # funzione

        # ci possiamo chiedere se other è un conto corrente
        # questo metodo spiega all'interprete come gestire la somma di due
# oggetti della nostra classe
        return self.importo + other.importo

        # altrimenti dobbiamo sommare l'importo attuale + il numero int/float

if __name__ == "__main__":
    # Rapido test della classe
    # 1. dobbiamo istanziare un oggetto della classe
    conto_personale = ContoCorrente(100, "Daniele Cerrina")
    print(conto_personale)
    # 2. Possiamo provare a fare un deposito
    conto_personale.deposito(340.23)
    print(conto_personale)
    # 3. Proviamo a eseguire un prelievo
    if conto_personale.prelievo(120):
        print("il prelievo è andato a buon fine")
    else:
        print("non hai abbastanza soldi nel conto")
    print(conto_personale)
    conto2 =  ContoCorrente(674, "Giacomo Terri")
    print(f"Importo totale: {conto_personale + conto2}")
    print(sum(conto_personale, conto2))