"""
Data una lista di [liste di] spese andiamo a calcolare un po di statistiche
"""

def calcola_media (lista_spese: list[float]) -> float:
    """
    funzione che calcola la media di una lista di numeri con la virgola.
    :param lista_spese: lista di spese di cui viene calcolata la media
    :return: media, float
    """
    media = sum(lista_spese) / len(lista_spese) # calcoliamo ala media sempre come somma ( n di elementi)
    return media # facciamo uscire la media calcolata dalla funzione
def calcola_varianza(lista_spese: list[float]) -> float:
    """
    funzione che calcola la varianza di una lista di numeri con la virgola.
    :param lista_spese: lista di spese di cui viene calcolata la varianza
    :return: varianza, float
    """
    media = calcola_media(lista_spese) # utilizziamo la funzione fatta prima per calcolare la media
    # calcoliamo lo scarto di ogni elemento della lista rispetto alla media e lo eleviamo al quadrato
    scarti = []

    for numero in lista_spese:
        scarto = (numero - media) **2
        scarti.append(scarto)

    # calcoliamo la media degli scarti (che è la varianza)
    varianza = calcola_media(scarti)
    return varianza # facciamo uscire la varianza dalla funzione -> restituiamo


def calcola_dev_standard(lista_spese: list[float]) -> float:
    """
    funzione che calcola la deviazione standard di una lista di numeri con la virgola.
    :param lista_spese: lista di spese di cui viene calcolata la deviazione standard
    :return: deviazione standard, float
    """
    #calcoliamo la varianza con la funzione appena fatta
    varianza = calcola_varianza(lista_spese)
    #calcolia la radice quadrata della varianza
    deviazione = varianza ** (1 / 2)  # radice cubica 1/3
    return  deviazione

def separatori(titolo: str, carattere="-", lunghezza=50) -> tuple[str, str]: # per dare un valore di default usiamo un <parametro> = <valore>
    """
    funzione che calcola due stringhe di separatori (intestazione e coda) lunghe uguali dato un titolo.
    :param titolo: titolo della sezione
    :param carattere: carattare utilizzato per essere ripetuto nel separatore
    :param lunghezza: numero di volte che il carattare viene ripetuto prima del titolo (tot= 2*lunghezza)
    :return: due stringhe -> separatori per print
    """
    intestazione = f"{carattere * lunghezza} {titolo} {carattere * lunghezza}"
    coda = carattere * len(intestazione)

    return intestazione, coda # restituiamo entrambe le stringhe ottenute

def analizza_lista (lista_spese: list[float], nome: str) -> str:
    """
    funzione che elabora e restituisce un'analisi completa di una lista di spese
    :param nome: nome dell'elenco di spese
    :param lista_spese: lista di spese float
    :return: report completo, str
    """
    intestazione, coda = separatori(nome) # creiamo separatori per la sezione <- otteniamo entrambe le stringhe in ORDINE DI USCITA
    media = calcola_media(lista_spese) # media della lista
    deviazione = calcola_dev_standard(lista_spese)  # calcoliamo la deviazione standard
    spesa_max = max(lista_spese)
    spesa_min = min(lista_spese)
    n_spese = len(lista_spese) # numero di spese

    output = f"{intestazione}\n" # creiamo la stringa di output inziando dall'intestazione
    output += f" * Media: {media:.2f} €\n" # aggiungiamo all'output la media
    output += f" * deviazione standard: {deviazione:.2f} €\n" # aggiungiamo all'output la deviazione standard
    output += f" * Spesa max: {spesa_max:.2f} €\n" # aggiungiamo all'output la spesa max
    output += f" * Spesa min: {spesa_min:.2f} €\n" # aggiungiamo all'output la spesa min
    output += f" * N° spese: {n_spese:.2f} €\n" # aggiungiamo all'output il numero di spese
    output += coda # aggiungiamo all'output la coda separatore finale

    return output # restituiamo la stringa output

if __name__ == "__main__": #questo blocco che usiamo per utilizzare le funzioni prende il nome di "main", si scrive sempre cosi
    # codice per usare le funzioni
    lista_prova = [12.1, 45, 98, 45.3, 4, 10.9, 45]
    media_prova =calcola_media(lista_prova)
    print(media_prova)
    varianza_prova = calcola_varianza(lista_prova)
    print(varianza_prova)
    deviazione_prova = calcola_dev_standard(lista_prova)
    print(deviazione_prova)
    print()

    diz_spese = {
        "settembre": [12, 23.2,5,6.7,10],
        "ottobre": [8.3, 12.2, 78, 6.7, 20],
        "novembre": [12.5, 8.2, 5, 63, 2.2]
    }

    for mese, lista_spese in diz_spese.items():
        report = analizza_lista(lista_spese, mese)
        print(report)