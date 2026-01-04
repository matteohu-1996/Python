from esercizi.esercizio_1 import irpef
from fattura import Fattura
from partita_iva import PartitaIva

mia_partita_iva  = PartitaIva(0.67, 0.2627, 0.15)
mia_partita_iva.carica_da_file("fatture.json")
totale = mia_partita_iva.fatturato_totale()
inps = mia_partita_iva.calcolo_inps()
irpef = mia_partita_iva.calcolo_irpef()
netto = mia_partita_iva.calcolo_netto()


print()
print("---------------------------------------------"
      "")
print(f"Fatturato totale della partita iva: "
      f"{mia_partita_iva.fatturato_totale():.2f}")
print(f"Da pagare all'INPS: {mia_partita_iva.calcolo_inps():.2f} €")
print(f"Da pagare all'IRPEF: {mia_partita_iva.calcolo_irpef():.2f} €")
print(f"Netto dopo le tasse: {mia_partita_iva.calcolo_netto():.2f} €")

# Calcolare quanto paghiamo in percentuale complessivamente di tasse
coeff_tasse_complessivo = (irpef + inps)/ totale
print(f"Sul fatturato paghiamo il {coeff_tasse_complessivo:.2%} di tasse")

# Calcolo della % di netto
print(f"Quindi abbiamo il {(1 - coeff_tasse_complessivo):.2%} di netto")

print(mia_partita_iva.conta_fatture_per_mese())