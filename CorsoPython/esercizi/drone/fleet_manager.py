import json
import os.path
from package import Package
from drone_trip import DroneTrip


class FleetManager:
    """
    il cervello logistico.
    Legge i dati, applica l'algoritmo e genera il report
    """
    def __init__(self):
        self.trips =[]

    def load_data(self ,filename):
        """Carica il json e istanzia gli oggetti Package"""
        if not os.path.exists(filename):
            print(f"Errore: file {filename} non trovato.")
            return []

        with open(filename, "r") as f:
            data = json.load(f)
            return [Package(p["id"], p.get["content"], p["weight"],
                            p["value"]) for p in data]

    def optimize(self,packages):
        """
        ALGORITMO FIRST FIT
        ordinare i pachci dal più pesante al più leggero
        per ogni pacco, cerchiamo il primo drone disponibile che ha spazio
        se non esiste si crea uno nuovo
        :param packages:
        :return:
        """
        packages.sort(key=lambda x: x.weight, reverse=True)

        for pkg in packages:
            placed = False
            for trip in self.trips:
                if trip.add_package(pkg):
                    placed = True
                    break

            if not placed:
                new_trip = DroneTrip(len(self.trips) + 1)
                new_trip.add_package(pkg)
                self.trips.append(new_trip)


    def print_report(self):
        print("=" * 60)
        print("         NEO-TOKYO LOGISTICS - AI DISPATCHER REPORT         ")
        print("=" * 60)
        print(f"Stato Flotta: {len(self.trips)} Viaggi pianificati. \n")

        for t in self.trips:
            print(f"Drone #{t.trip_id:02d}")
            print(f" > Carico: {t.current_weight:6.2f} / 100kg")
            print(f" > Valore: {t.get_total_value():10,}")
            print(f" > Spreco: {t.get_waste_percentage():6.2f %}")
            print(f" > Pacchi: {', '.join([p.id for p in t.packages])}")
            print("=" * 60)
