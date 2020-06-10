class Gate():
    def __init__(self, gatenumber, coordinate_x, coordinate_y):
        """ Declare gate class, consists of gatenumber, coordinates of the gate and the connections made"""

        # Declare variables
        self.gate_number = gatenumber
        self.coordinates = (coordinate_x, coordinate_y, 0)
        self.connections = []

    # hier doen we nog niks mee, zouden we mee bij kunnen houden vanaf welke kant een chip al een connectie heeft
    def add_connection(self, direction):
        self.connections.append(direction)

    def has_connection(self, direction):
        if direction in self.connections:
            return True
        else:
            return False

    def get_coordinates(self):
        return self.coordinates