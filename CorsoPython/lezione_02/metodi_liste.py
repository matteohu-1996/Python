lista_spese = [
    122.1, 145.2, 172.9,
    92.3, 123.2, 75.2,
    132.1, 123.2, 89.2,
    56.3, 152.2, 164.2,
]

# aggiungere un elemento
lista_spese.append(162.7)
print(f"{lista_spese}")

#rimuovere un elemento con indice
lista_spese.pop(5) # rimuove elemento indice 5, se non mettiamo niente
# rimuove ultimo elemento
print(f"{lista_spese}")

#rimuovere un elemento con valore
lista_spese.remove(122.1) # rimuove il primo elemento con valore 122.1
print(f"{lista_spese}")

lista_2 = [9, 2, 2, 9, 4, 5]
lista_2.remove(9) # [ 2, 2, 9, 4, 5]
print(f"{lista_spese}")

#ordinare la lisa
# 1 creando una versione ordinata della lista
lista_ordinata = sorted(lista_spese)
#la lista originale rimane disordinata
print(f"Lista ordinata: {lista_ordinata} \nLista spesa: {lista_spese}")

# 2 "inplace"
lista_spese.sort()
# da ora in poi la lista è ordinata
print(f"Lista spese:{lista_spese}")

#inserire un elemento a un dato indice
lista_spese.insert(5,"prova")
print(f"{lista_spese}")

#contare quante volte un elemento compare in una lista
count = lista_spese.count(123.2)
print(f"123.2 compare {count} volte")