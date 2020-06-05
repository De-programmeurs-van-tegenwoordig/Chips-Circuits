import csv
from .chip import Chip


class Grid():
    def __init__(self, chip_file, netlist_file):
        self.chips = self.load_chips(chip_file)
        self.netlists = self.load_netlist(netlist_file)

    def load_chips(self, chip_file):
        """ Reads the file """
        chips={}

        with open(chip_file, 'r') as input_file:
            reader = csv.DictReader(input_file)
            
            for count, row in enumerate(reader, 1):
                new_chip = Chip(count, row['x'], row['y'])
                chips[int(count)] = new_chip
        return chips

    def load_netlist(self, netlist_file):
        netlists=[]
        
        with open(netlist_file, 'r') as input_file:
            reader = csv.DictReader(input_file)
        
            for count, row in enumerate(reader, 1):
                new_connection = [row['chip_a'], row['chip_b']]
                netlists.append(new_connection)
        return netlists
