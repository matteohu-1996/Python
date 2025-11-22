dizionario_spese = {
    "gen": 32,
    "feb": 45,
    "mar": 69,
    "apr": 51,
    "mag": 30,
    "giu": 45,
    "lug": 74,
    "ago": 46,
    "set": 36,
    "ott": 98,
    "nov": 46,
    "dic": 51,
}

#ottendiamo le chiavi del dizionario
print(f"chiavi del dizionario: {dizionario_spese.keys()}")

#ottendiamo le valori del dizionario
print(f"valori del dizionario: {dizionario_spese.values()}")

#ottendiamo le coppie chiave-valore del dizionario
print(f"coppie chiave-valore del dizionario: {dizionario_spese.items()}")

print(f"media delle chiavi del dizionario: "
      f"{sum(dizionario_spese.values()) / len(dizionario_spese.values()):.2f}")
print(f"spesa massima: {max(dizionario_spese.values())}")
print(f"spesa minima:  {min(dizionario_spese.values())}")
