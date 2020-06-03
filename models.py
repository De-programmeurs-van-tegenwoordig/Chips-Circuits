class Chip():
    def __init__(self, chipnumber, coordinate_x, coordinate_y):
        self.chip_number = chipnumber
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.connections = []

    # wanneer de lijn van 1 naar 2 wordt gelegd. invullen dat 2 aan die kant de connectie met 1 heeft
    def add_connection(self, direction):
        self.connections.append(direction)

    def has_connection(self, direction):
        if direction in self.connections:
            return True
        else:
            return False
