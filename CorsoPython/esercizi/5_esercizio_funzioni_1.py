"""
Hai appena chiuso il mese per un grosso cliente ("MegaCorp") a cui stai sviluppando un portale interno.
Il contratto prevede tariffe orarie differenziate in base alla tecnologia usata: lo sviluppo Frontend (React)
viene pagato 50€/h, il Backend (Python) 60€/h, mentre le ore dedicate all'AI (Modelli/RAG) valgono 100€/h.
C'è però una complicazione (il "twist"): se il cliente ha richiesto un intervento con flag "urgente",
quella specifica sessione di lavoro subisce una maggiorazione del 30% sulla tariffa base.
Il tuo obiettivo è processare il registro delle ore grezzo e calcolare quanto devi fatturare per
ogni singola voce, senza impazzire con calcolatrice e fogli Excel se le tariffe dovessero
cambiare mese prossimo.
"""

def genera_fattura(log_ore):
    # Configurazione tariffe (facilmente modificabile)
    TARIFFE_BASE = {
        "React": 50,
        "Python": 60,
        "AI_RAG": 100,
        "DEFAULT": 50  # Gestione per tipi non previsti come DevOps
    }

    MAGGIORAZIONE_URGENTE = 0.30  # +30%

    totale_generale = 0
    report_dettagliato = []

    print(
        f"{'ID':<10} | {'Tipo':<10} | {'Ore':<5} | {'Urgente':<8} | {'Totale Voce'}")
    print("-" * 60)

    for record in log_ore:
        tipo = record.get("tipo")
        ore = record.get("ore", 0)
        is_urgente = record.get("urgente", False)

        # Recupero tariffa base (con fallback su DEFAULT)
        tariffa_base = TARIFFE_BASE.get(tipo, TARIFFE_BASE["DEFAULT"])

        # Calcolo prezzo finale della singola voce
        prezzo_orario_effettivo = tariffa_base
        if is_urgente:
            prezzo_orario_effettivo += (tariffa_base * MAGGIORAZIONE_URGENTE)

        totale_voce = ore * prezzo_orario_effettivo
        totale_generale += totale_voce

        # Formattazione stringa per il terminale
        urg_str = "SÌ" if is_urgente else "NO"
        print(
            f"{record['id']:<10} | {tipo:<10} | {ore:<5} | {urg_str:<8} | €{totale_voce:>8.2f}")

    print("-" * 60)
    print(f"TOTALE DA FATTURARE A MEGACORP: €{totale_generale:.2f}")


if __name__ == "__main__":
    timesheet = [
        {"id": "LOG-001", "data": "2025-11-01", "tipo": "React", "ore": 4.5,
         "descrizione": "Setup...", "urgente": False},
        {"id": "LOG-002", "data": "2025-11-02", "tipo": "Python", "ore": 3.0,
         "descrizione": "API...", "urgente": False},
        {"id": "LOG-003", "data": "2025-11-03", "tipo": "AI_RAG", "ore": 5.0,
         "descrizione": "Studio...", "urgente": False},
        {"id": "LOG-004", "data": "2025-11-05", "tipo": "React", "ore": 2.0,
         "descrizione": "Hotfix...", "urgente": True},
        {"id": "LOG-005", "data": "2025-11-07", "tipo": "Python", "ore": 6.5,
         "descrizione": "Logic...", "urgente": False},
        {"id": "LOG-006", "data": "2025-11-08", "tipo": "AI_RAG", "ore": 2.0,
         "descrizione": "Debug...", "urgente": True},
        {"id": "LOG-007", "data": "2025-11-10", "tipo": "DevOps", "ore": 1.5,
         "descrizione": "Docker...", "urgente": False},
        {"id": "LOG-008", "data": "2025-11-12", "tipo": "React", "ore": 4.0,
         "descrizione": "Dash...", "urgente": False},
        {"id": "LOG-009", "data": "2025-11-15", "tipo": "Python", "ore": 1.0,
         "descrizione": "Fix...", "urgente": True},
        {"id": "LOG-010", "data": "2025-11-18", "tipo": "AI_RAG", "ore": 3.5,
         "descrizione": "Embed...", "urgente": False},
    ]

    genera_fattura(timesheet)