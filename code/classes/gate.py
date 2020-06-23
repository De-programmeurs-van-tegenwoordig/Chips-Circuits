class Gate():
    def __init__(self, gatenumber, coordinate_x, coordinate_y):
        """ 
        Declare gate class, consists of gatenumber, coordinates of the gate and the connections made
        """

        # Declare variables
        self.gate_number = gatenumber
        self.coordinates = (coordinate_x,coordinate_y,0)
        self.connections = []

    def add_connection(self, direction):
        """
        Adds a connection to a gate
        """
        self.connections.append(direction)

    def has_connection(self, direction):
        """
        Checks if gate has a connection
        """
        if direction in self.connections:
            return True
        else:
            return False

    def get_coordinates(self):
        """
        Returns coordinates of a gate
        """
        return self.coordinates

    def get_gate_number(self):
        """
        Returns number of a gate
        """
        return self.gate_number