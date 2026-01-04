from idlelib.debugobj import dispatch

from package import  Package
from drone_trip import DroneTrip
from fleet_manager import FleetManager


if __name__ == "__main__":
    dispatcher = FleetManager()

    # acquisizione dati
    pacchi_in_attesa = dispatcher.load_data("dati.json")

    if pacchi_in_attesa:
        # esecuzione algoritmo di incastro
        dispatcher.optimize(pacchi_in_attesa)
        # presentazione risultati
        dispatcher.print_report()