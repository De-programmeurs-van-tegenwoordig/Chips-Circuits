import csv
import random
from .gate import Gate

class Grid():
    def __init__(self, gate_file, netlist_file, size):
        """Reads the given files"""
        self.size = size
        self.amount_of_crosses = {}
        self.coordinates_gates = []
        self.zones = {}
        self.total_zones = []
        self.total_gates = []
        
        # Read the gates file
        self.gates = self.load_gates(gate_file)
    
        # Read the netlist file
        self.netlists = self.load_netlists(netlist_file)
        self.list_of_nets = {}
        self.order_of_nets = {}
        self.key = 0
        
    def load_gates(self, gate_file):
        # Declare local variable
        gates = {}

        # Opens gate file and puts every gate in dictionary
        with open(gate_file, 'r') as input_file:
            reader = csv.DictReader(input_file)
            for count, row in enumerate(reader, 1):
                zone = []
                new_gate = Gate(count, row['x'], row['y'])
                gates[int(count)] = new_gate
                self.coordinates_gates.append([row['x'], row['y'], 0])
                
                self.total_gates.append((int(row['x']), int(row['y']), 0))

                zone.append((int(row['x']) + 1, int(row['y']), 0))
                zone.append((int(row['x']) - 1, int(row['y']), 0))
                zone.append((int(row['x']), int(row['y']) + 1, 0))
                zone.append((int(row['x']), int(row['y']) - 1, 0))
                zone.append((int(row['x']), int(row['y']), 1))

                self.total_zones.append((int(row['x']) + 1, int(row['y']), 0))
                self.total_zones.append((int(row['x']) - 1, int(row['y']), 0))
                self.total_zones.append((int(row['x']), int(row['y']) + 1, 0))
                self.total_zones.append((int(row['x']), int(row['y']) - 1, 0))
                self.total_zones.append((int(row['x']), int(row['y']), 1))

                self.zones[count] = zone
        return gates

    def load_netlists(self, netlist_file):
        # Declare local variables
        netlists = []
        
        # Opens netlist file and puts every netlist in list
        with open(netlist_file, 'r') as input_file:
            reader = csv.DictReader(input_file)
        
            for row in reader:
                new_connection = (row['chip_a'], row['chip_b'])
                netlists.append(new_connection)   
        return netlists

    def get_total_zones(self):
        return self.total_zones

    def get_total_gates(self):
        return self.total_gates

    def get_zone(self,chip_number):
        return self.zones[chip_number]

    def get_coordinates_gates(self):
        return self.coordinates_gates
        
    def get_current_gate_number(self, coordinate_x, coordinate_y):
        """
        Used for the output file to track which net is being written
        """
        gates = self.get_total_gates()

        for i in range(len(gates)):
            coordinates = gates[i]
            x = int(coordinates[0])
            y = int(coordinates[1])

            if x == coordinate_x and y == coordinate_y:
                return i + 1

    def get_netlists(self):
        # Returns all netlists
        random.shuffle(self.netlists)
        return self.netlists

    def get_new_netlist(self):
        if not self.netlists:
            return None

        netlist = self.netlists.pop()

        # Get local variables
        origin = int(netlist[0])
        destination = int(netlist[1])
        
        gate_origin = self.gates[origin]
        gate_destination = self.gates[destination]

        coordinates_origin = gate_origin.get_coordinates()
        coordinates_destination = gate_destination.get_coordinates()

        origin_x = int(coordinates_origin[0])
        origin_y = int(coordinates_origin[1])

        destination_x = int(coordinates_destination[0])
        destination_y = int(coordinates_destination[1])

        return origin_x, origin_y, destination_x, destination_y

    def get_coordinates_netlist(self, netlist):
        origin = int(netlist[0])
        destination = int(netlist[1])
        
        gate_origin = self.gates[origin]
        gate_destination = self.gates[destination]

        coordinates_origin = gate_origin.get_coordinates()
        coordinates_destination = gate_destination.get_coordinates()

        origin_x = int(coordinates_origin[0])
        origin_y = int(coordinates_origin[1])

        destination_x = int(coordinates_destination[0])
        destination_y = int(coordinates_destination[1])

        return origin_x, origin_y, destination_x, destination_y

    def add_route(self, nets, amount_of_crosses):
        self.list_of_nets[self.key] = nets
        self.amount_of_crosses[self.key] = amount_of_crosses
        self.key += 1

    def remove_route(self, key):
        key = key
        del self.list_of_nets[key]
        del self.amount_of_crosses[key]
        
    def get_list_of_routes(self):
        return self.list_of_nets

    def cost_of_route(self):
        cost = 0

        list_of_routes = self.get_list_of_routes()

        for item in list_of_routes:
            cost += len(list_of_routes[item])
        
        for item in self.amount_of_crosses:
            cost += (300 * self.amount_of_crosses[item])
        
        return cost

    def get_size(self):
        return self.size


