class Net():
    def __init__(self, coordinate_from, coordinate_to):
        self.coordinates_from = coordinate_from
        self.coordinates_to = coordinate_to
    
    def get_coordinates_from(self):
        return self.coordinates_from

    def get_coordinatesto(self):
        return self.coordinates_to