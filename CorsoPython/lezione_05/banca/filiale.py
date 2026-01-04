from lezione_05.banca.conto_corrente import ContoCorrente


class Filiale:
    def __init__(self, nome: str, direttore: str):
        self.nome = nome
        self.direttore = direttore
        self.conti_correnti = [] # lista vuota che conterrà tutti i conti
        # correnti registrati alla filiale

    def crea_conto(self, titolare: str, importo_iniziale: int):
         conto_nuovo = ContoCorrente(importo_iniziale, titolare) # creiamo il
         # nuovo conto
         self.conti_correnti.append(conto_nuovo) #aggiungiamo alla lista il
         # conto appena creato

    def trasferisci_conto(self, conto_corrente: ContoCorrente) -> bool:
        # 1. ci chiediamo se l'iban del conto esiste già
        for conto in self.conti_correnti:
            if conto_corrente.iban == conto.iban:
                return False

        # 2. se non siamo usciti dal for, l'iban non è presente nella lista,
        # quindi aggiungere il nuovo conto corrente
        self.conti_correnti.append(conto_corrente)
        return True

    def deposito_totale(self):
        totale = 0
        for conto in self.conti_correnti:
            totale += conto.importo
        return totale


    def __str__(self):
        output = f"Nome filiale: {self.nome}\n"
        output += f"Direttore: {self.direttore}\n"
        output += f"Conti: \n"
        for conto in self.conti_correnti:
            output += str(conto) + "\n"

        return output