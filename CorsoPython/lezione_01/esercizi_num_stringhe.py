# scriviamo il totale di una lista di oggetti che abbiamo comprato e ne stampi un resoconto
from random import vonmisesvariate

tavolo = 230
sedia = 45
n_sedia = 4
piatto_fondo = 3.4
piatto_piano = 4.2
numero_persone_servizio = 6

costo_sedie = sedia * n_sedia
costo_piatti = (piatto_fondo + piatto_piano) * numero_persone_servizio

costo_totale = tavolo + costo_sedie + costo_piatti


print("riepilogo dei costi: ")
print(f" - Tavolo: {tavolo}")
print(f" - Piatti: {costo_piatti}")
print(f" - Sedie: {costo_sedie}")
print(f" - Totale: {costo_totale}")

# creiamo un sistema che date 3 dimensioini di un parallelepipedo restituisca:
# area di base: base * profondita
# volume totale: base * altezza * profondita
# diagonale: (base ** 2 + altezza ** 2 + profondita **2) ** 1/2

base = 24
profondita = 15.3
area_di_base = base * profondita
altezza = 30
volume_totale = base * altezza * profondita
diagonale = (base ** 2 + altezza ** 2 + profondita **2) ** (1/2)

print("---------------------------------------------")
print(f" Base = {base}")
print(f" Altezza = {altezza}")
print(f" Profondità = {profondita}\n")
print(f" L'area di base è: {area_di_base}")
print(f" Volume totale è: {volume_totale}")
print(f" Diagonale è: {diagonale}")