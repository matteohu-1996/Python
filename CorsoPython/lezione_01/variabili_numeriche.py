# calcoliamo l'area di un triangolo date base e altezza
base = 22
altezza = 34.1
area = base * altezza / 2

# per stampare il risultato usiamo la funzione print
# shortcut per il terminale ctrl shift F10
print(area)

# convertiamo un tempo in secondi in ore:minuti:secondi
tempo = 45698 # tempo iniziale in secondi
ore = tempo // (60 * 60) # calcoliamo a quante ore intere corrispondono i sec
secondi = tempo % (60 * 60) # calcoliamo quanti secondi rimangono "fuori" dalle ore intere

minuti = secondi // 60 # calcoliamo a quanti minuti (interi) corrispondono i secondi rimanenti
secondi = tempo % 60

print(ore, minuti, secondi)

