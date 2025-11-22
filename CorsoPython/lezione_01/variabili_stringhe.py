persona1 = "Aldo"
persona2 = "Giovanni"
persona3 = "Giacomo"

print(f"Ciao {persona1}, {persona2} e {persona3}")

# facciamo separatorie di sezioni
titolo = "calcolo dell'area"
separatore = f"{"-" * 50} {titolo} {"-" * 50}"
print(separatore)

# esempi di informazioni che possiamo ottenere sulle stringhe
titolo = "calcolo area"
lunghezza = len(titolo) # len lunghezza della stringa
print(f"la lunghezza della parola '{titolo}' è: {lunghezza}")

titolo = "ricerca del minimo"
#vogliamo stampare le lettere che compongono la stringa dalla seconda all'ultima
print(titolo[1:])
# (esclusa)
print(titolo[3:])
# (inclusa)
print(titolo[2:-1])
