class Node():
    def __init__(self, parent=None, position=None):
        """
        Node used in A*
        """
        self.parent = parent
        self.position = position
        self.cross = False

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        """
        Compares the position of two nodes
        """
        return self.position == other.position

