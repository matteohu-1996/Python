"""
scrivere una funzione che data una lista di numeri restituisce una lista di stringhe di questo tipo:
- se il numero nella lista di input è multiplo di 3 -> al suo posto ci mette "AAAA"
- se il numero nella lista di input è multiplo di 5 -> al suo posto ci mette "BBBB"
- se il numero nella lista di input è multiplo di 15 -> al suo posto ci mette "AABB"
- altrimenti mette la stringa del numero della lista di input
"""
from lezione_01.variabili_stringhe import lunghezza


def sost_multupli(lista: list[int]) -> list[str]:

    output = []
    for elemento in lista:
        if elemento %  15 == 0:
            output.append("AABB ")
        elif elemento % 5 == 0:
            output.append("BBBB")
        elif elemento % 3 == 0:
            output.append("AAAA")
        else:
            output.append(str(elemento))
    return output
"""
scrivere una funzione data una lista di n numeri capisca quale numero da 0 a n manca al range
es: [3,0,1] -> 2
es: [1,2,5,6,3,0] -> 4 
"""

def trova_mancante(lista: list[int]) -> int:

    lunghezza = len(lista) # lunghezza lista -> qual è estremo del range di riferimento
    somma_desiderata = lunghezza * (lunghezza + 1) // 2
    somma_attuale = sum(lista)

    return somma_desiderata - somma_attuale


"""
scrivere una funzione che dato un numero >= 0 calcoli la somma dei dispari fino a quel numero (compreso)
"""

def somma_dispari(num: int) -> int:
   # n = 7
   # tot = 0
    # for numero in range(1, n+1 ,2): -> for che scorre da 0 a n + 1 facendo salti di 2
   #     tot += 1
   # return tot
    if num % 2 == 1:
        num += 1
    return (num // 2) ** 2

def somma_pari(num: int) -> int:
    if num % 2 == 1:
        num -= 1
    return (num // 2) * (num // 2 + 1 )

"""
scrivi una funzione che dato un numero restituisce true se è primo, altrimenti false
"""

def is_primo(num: int) -> bool:
   # for i in range(2,num):
   #     if num % i != 0:
   #     return True
   # return False

    if num < 2:
        return False

    for i in range (2,round(num ** (1/2)) +1):
       if num % i == 0:
           return False
    return True


if __name__ == "__main__":
    # teste delle funzioni
    lista_1 = [12,4,17,25,45,10,23,9,18] # ["AAAA", "4", "17","BBBB", "AABB", "23", "AAAA","AAAA"]
    print(sost_multupli(lista_1))

    lista_2 = [3,0,1,5,2,4]
    print(f"Numero mancante: {trova_mancante(lista_2)}")

    massimo = 7
    print(f"Somma numeri dispari da 1 a {massimo} = {somma_dispari(massimo)}")
    print(f"Somma numeri pari da 1 a {massimo} = {somma_pari(massimo)}")
    print(f"Numeri primi {is_primo(massimo)} = {is_primo(massimo)}")
