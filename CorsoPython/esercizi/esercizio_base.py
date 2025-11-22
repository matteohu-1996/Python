"""
Stai pianificando un viaggio in auto partendo da casa tua a Torino verso una località di mare.
La destinazione scelta è la città di "Otranto", che dista esattamente 1025 chilometri.
La tua auto, una vecchia "fiat punto", ha un consumo medio dichiarato di 16.5 chilometri con un litro
di carburante. Sapendo che il prezzo attuale della benzina è di 1.829 euro al litro e che dovrai
sostenere una spesa fissa per i pedaggi autostradali pari a 74.50 euro, scrivi uno script che calcoli
la quantità di litri necessari, il costo del solo carburante e infine il costo totale del viaggio.
"""

distanza_torino_otranto = 1025 # km
consumo_medio = 16.5 # km/l
prezzo_litro = 1.829 # €/l
pedaggio = 74.50 # €

litri_necessari = distanza_torino_otranto / consumo_medio # km / (km / L) = km * ç/km = L
totale_benzina = litri_necessari * consumo_medio # L * (€ / L) = €
totale_viaggio = pedaggio + totale_benzina

print()
print(f" Distanza Torino-Otranto: {distanza_torino_otranto} km")
print(f" Pedaggio: {pedaggio} €")
print()
print(f" Quantità di litri necessari: {litri_necessari:.2f} l")
print(f" Costo totale benzina: {totale_benzina:.2f} €")
print(f" Costo totale del viaggio: {totale_viaggio:.2f} €")


