

class DroneTrip:
    """
    Rappresenta un singolo decollo.
    Gestisce il limite fisico della capacità (100)kg e tiene traccia di cosa
    c'e a bordo
    """
    MAX_CAPACITY = 100.0

    def __init__(self, trip_id):
        self.trip_id= trip_id
        self.packages = []
        self.current_weight = 0

    def add_package(self, package):
        """
        tenta di caricare il pacco
        restituisce True se l'operazione riesce, False se il drone è pieno
        :param package:
        :return:
        """
        if self.current_weight + package.weight <= self.MAX_CAPACITY:
            self.packages.append(package)
            self.current_weight += package.weight
            return True
        return False

    def get_total_value(self):
        """Calcola la somma dei valori di tutti i pacchi nel drone"""
        return sum(p.value for p in self.packages)


    def get_waste_percentage(self):
        """Calcola quanto spazio vuoto (in %) stiamo sprecando"""
        return ((self.MAX_CAPACITY - self.current_weight) /
                self.MAX_CAPACITY) *id