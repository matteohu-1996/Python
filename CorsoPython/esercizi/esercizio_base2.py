"""Scenario: Il Calcolatore di Token
Stai sviluppando un modulo per un tuo cliente che monitora quanto spende per ogni risposta generata dal tuo agente AI.
Devi calcolare il costo totale di una singola interazione basandoti sul numero di token di input (il prompt)
e di output (la risposta), e generare un report leggibile.

Dati di partenza (Variabili)
Crea uno script Python e inizializza queste variabili:

nome_modello: Una stringa (es. "GPT-4-Turbo").

token_input: Un numero intero che rappresenta la lunghezza del prompt (es. 1250).

token_output: Un numero intero che rappresenta la lunghezza della risposta (es. 450).

costo_per_1k_input: Un numero decimale (float) per il costo ogni 1000 token di input (es. 0.01 dollari).

costo_per_1k_output: Un numero decimale (float) per il costo ogni 1000 token di output (es. 0.03 dollari).

tasso_cambio_usd_eur: Un float per convertire il costo in euro (es. 0.92)."""

nome_modello = "GPT-4-Turbo"
token_input = 1250
token_output = 450
costo_per_1k_input = 0.01
costo_per_1k_output = 0.03
tasso_cambio_usd_eur = 0.92
totale_token = token_input + token_output

costo_input = token_input / costo_per_1k_input
costo_output = token_output / costo_per_1k_output
costo_totale = costo_output + costo_input

print("-----------------------------------------------")
print(f"Modello AI: {nome_modello}")
print(f"Token input: {token_input}")
print(f"Token output: {token_output}")
print(f"Token totali: {totale_token}")

print()

print(f"Costo totale di token input: {costo_input:.2f}")
print(f"Costo totale di token output: {costo_output:.2f}")
print(f"Costo totale di interazioni: {costo_totale:.2f}")

