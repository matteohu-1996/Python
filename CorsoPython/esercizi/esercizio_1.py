# abbiamo una partita IVA, il nostro codice ateco ci dice che l'imponibile è il 67% del fatturato
# sul imponibile paghiamo il 15% di IRPEF e il 26.07% di INPS
# calcoliamo quanto paghiamo di IRPEF e di INPS in €
# calcoliamo quale percentiael di fatturato ci rimane dopo le tasse

# suggerimento: il 17% di una variabile "numero" è numero * 0.27
fatturato = 123_123
coefficiente_imponibile = 0.67
aliquota_irpef = 0.15
aliquota_inps = 0.2607

# le tasse nel contesto non cambiano mai

# le tasse si pagano sull'immpobile
imponibile = fatturato * coefficiente_imponibile

irpef = imponibile * aliquota_irpef
inps = imponibile * aliquota_inps
tasse_totali = irpef + inps

resto_netto= fatturato - tasse_totali
percentuale_resto = resto_netto / fatturato

print(f" Risultato del calcolo fiscale")
print(f" Fatturato:  {fatturato:.2f}") # :.2f arrotonda il risultato a 2 cifre decimali
print(f" Imponibile:  {imponibile:.2f}")
print(f"Tasse pagate:")
print(f" IRPEF:  {irpef:.2f}")
print(f" INPS:  {inps:.2f}")
print(f"Tasse totali: {tasse_totali}") #.2% arrotonda la percentuale