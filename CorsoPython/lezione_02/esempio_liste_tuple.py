lista_spese = [
    122.1, 145.2, 172.9,
    92.3, 123.2, 75.2,
    132.1, 123.2, 89.2,
    56.3, 152.2, 164.2,
]

print(f"Lunghezza lista: {len(lista_spese)}")
print(f"Somma della lista: {sum(lista_spese)}") # calcola somma della lista
print(f"Media della lista: {sum(lista_spese) / len(lista_spese):.3f}")
print(f"Massima e minimo della lista: {max(lista_spese)} e {min(lista_spese)}")

# prendiamo le spese da febbraio a giugno compresi
print(f"Spese da Febbraio a giugno compresi: {lista_spese[1:6]}")

# prendiamo le spese da gennaio a marzo compresi
print(f"Spese da gennaio a marzo compresi: {lista_spese[:3]}")

# prendiamo le spese da settembre a dicembre compresi
print(f"Spese da settembre a dicembre compresi: {lista_spese[8:]}")

# prendiamo le spese da giugno a dicembre in ordine inverso
print(f"Spese da giugno a dicembre in ordine inverso: "
      f"{lista_spese[5:][::-1]}") # inverte la lista
# todo: provar a prendere le spese da giugno a dicembre con una sola
#  indicizzaione [partenza:fine::-1]

# prendiamo le spese da gennaio a dicembre solo dei mesi con posto pari
print(f"Spese dei mesi pari: {lista_spese[::2]}")

# prendiamo le spese da gennaio a dicembre solo dei mesi con posto dispari
print(f"Spese dei mesi dispari: {lista_spese[1::2]}")

#prendiamo l'ultimo
print(f"ultimo elemento:  {lista_spese[-1]}")

lista_spese[9] = "ottobre"
print(lista_spese)
tupla_mesi = ("gen","feb","mar","apr","mag","giu","lug","ago","set","ott",
              "nov","dic",
              )
print(f"lunghezza della tupla: {len(tupla_mesi)}")