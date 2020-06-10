class Net():
    def __init__(self, coordinates_from, coordinates_to):
        """The Net class consist of two coordinates, where the line starts and where it ends"""
        # Declare both coordinates
        self.coordinates_from = coordinates_from
        self.coordinates_to = coordinates_to
    
    def get_coordinates_from(self):
        # Returns the start coordinate of line
        return self.coordinates_from

    def get_coordinates_to(self):
        # Returns the end coordinate of line
        return self.coordinates_to
