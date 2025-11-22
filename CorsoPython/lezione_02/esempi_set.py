set_ingredienti = {"sale", "pepe", "uova", "zucchero",
                   "latte", "mele", "cannella"}
# set con ingredienti in dispensa

set_torta_mele = {
    "uova" , "zucchero" , "latte" , "mele", "vaniglia"
} # ingredienti necessari per torta di mele

#capiamo se ci sono ingredienti che non abbiamo per fare torta di mele
ingredienti_mancanti = set_torta_mele - set_ingredienti
print(f" ingredienti mancanti per torta di mele: {ingredienti_mancanti}")

set_crema_pasticcera = {
    "limone", "uova" ,"zucchero", "farina"
}

# vogliamo sapere quali sono tutti gli ingredienti necessari per fare
# entrambe le ricette
ingredienti_per_entrambe = set_torta_mele | set_crema_pasticcera
# | = unisce i due insiemi
print(f"ingredienti per fare due ricette: {ingredienti_per_entrambe}")

# vogliamo sapere quali ingredienti le due ricette hanno in comune
ingredienti_comuni = set_torta_mele & set_crema_pasticcera
# & = fa intersezione degli insiemi
print(f"Ingredienti comuni: {ingredienti_comuni}")

# METODI per i set
# per aggiungere elemento alla dispesa
set_ingredienti.add("farina")

# per rimuovere elemento dalla dispensa
set_ingredienti.remove("mele") # dà erroe se non trova le mele
print(f"Ingredienti dopo aver tolto le mele remove: {set_ingredienti}")
set_ingredienti.discard("mele") # non dà errore se non trova le mele
print(f"Ingredienti dopo aver tolto le mele discard: {set_ingredienti}")

