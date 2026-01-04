import json
"""
Security Operation Center - Sistema di gestione minacce cyber

Sei il responsabile di un SOC di cybersecurity che deve gestire un'ondata di attacchi
hacker in tempo reale. Il tuo compito è smistare le minacce agli analisti corretti
prima che i sistemi crollino.
"""


class Threat:
    def __init__(self, id_threat, tipo, gravita, descrizione):
        self.id = id_threat
        self.tipo = tipo
        self.gravita = gravita
        self.stato = "In attesa"

class Analyst:
    def __init__(self, nome, specializzazione, skill,stress):
        self.nome = nome
        self.specializzazione = specializzazione
        self.skill = skill
        self.stress = 0
        self.in_burnout = False

    def gestisci_ticket(self, threat):
        if self.in_burnout:
            return False
        if self.skill >= threat.gravita:
            threat.stato = "Neutralizzata"
            self.stress += 1
        else:
            threat.stato = "Bucata"
            self.stress += 5
        if self.stress > 10:
            self.in_burnout = True
        return True

class DefenseGrid:
    def __init__(self):
        self.analisti = []
        self.minacce = []
        self.sventate = 0
        self.subite = 0

    def carica_dati(self,file_analisti, file_attacchi):
        with open(file_analisti, "r") as f:
            dati_analisti = json.load(f)
            for a in dati_analisti:
                self.analisti.append(Analyst(a["name"],
                                             a["specialization"],
                                             a["skill_level"],
                                             a["stress_level"]))
        with open(file_attacchi, "r") as f:
            dati_attacchi = json.load(f)
            for t in dati_attacchi:
                self.minacce.append(Threat(t["id"], t["type"], t["severity"],
                                           t["description"]))

    def avvia_smistamento(self):
        for threat in self.minacce:
            assegnata = False
            for analista in self.analisti:
                if (analista.specializzazione == threat.tipo and not
                analista.in_burnout):
                    if threat.stato == "Neutralizzata":
                        self.sventate +=1
                    else:
                        self.sventate += 1
                    assegnata = True
                    break

            if not assegnata:
                threat.stato = "Bucata (Nessun analista disponibile"
                self.subite += 1

    def stampa_report(self):
        print("\n" + "-"*50)
        print("Report Finale SOC")
        print(f"Minacce sventate: {self.sventate}")
        print(f"Minacce subite: {self.subite}")
        print("\n" + "-"*50)
        print("Stato salute del team:")
        for a in self.analisti:
            stato = "Burnout" if a.in_burnout else "Attivo"
            print(f"[{a.specializzazione}] {a.nome} | Stress: "
            f"{a.stress}/10 | Stato: {stato}")

if __name__== "__main__":
    soc = DefenseGrid()
    soc.carica_dati("analisti.json", "attacchi.json")
    soc.avvia_smistamento()
    soc.stampa_report()