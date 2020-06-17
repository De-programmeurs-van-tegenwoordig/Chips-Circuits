from code.classes import net
from code.function import check_constraints
import random

class Greedy:
    def __init__(self, grid_file):
        """
        The Greedy class looks for the cheapest possible path between two gates
        """
        self.grid_file = grid_file
        self.count = 1

    def get_netlists(self, gridfile):
        """
        Returns the netlist in random order
        """
        netlists = list(self.grid_file.get_netlists())
        random.shuffle(netlists)
        return netlists

    def run(self, output):
        """
        Greedily chooses cheapest paths to get to his destination
        """
        netlists = self.get_netlists(self.grid_file)

        while len(netlists) != 0:
            netlist = self.grid_file.get_coordinates_netlist(netlists[0])
            netlists.pop(0)
            self.cross_counter = 0
            reset = 1
            
            # if self.grid_file.cost_of_route() > best_net_score:
            #     break

            while reset <= 200:
                if reset == 200:
                    return False

                origin_x = netlist[0]
                origin_y = netlist[1]
                destination_x = netlist[2]
                destination_y = netlist[3]
                
                directions = [(0,0,1), (0,0,-1), (0,-1,0), (1,0,0), (0,1,0), (-1,0,0)]
                nets = []

                # Set the beginning and endpoint up
                coordinates_origin = (origin_x, origin_y, 0)
                coordinates_from = coordinates_origin
                coordinates_destination = (destination_x, destination_y, 0)

                # Update the variables
                current_x = origin_x
                current_y = origin_y
                destination_z = 0
                current_z = 0

                moves = 0

                # While line has not reached endpoint
                while current_x != destination_x or current_y != destination_y or current_z != destination_z:
 
                    lowest_distance = float("inf")
                    best_directions = []
                    for direction in directions:
                        coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1], coordinates_from[2] + direction[2])
                        results = check_constraints.check_constraints(self.grid_file, coordinates_from, coordinates_to, coordinates_destination, nets)

                        check = results[0]
                        cross = results[1]

                        if check:
                            distance = abs(coordinates_to[0] - coordinates_destination[0]) + abs(coordinates_to[1] - coordinates_destination[1]) + abs(coordinates_to[2] - coordinates_destination[2])
                            if cross:
                                distance += 300
                            if distance < lowest_distance:
                                best_directions.clear()
                                lowest_distance = distance
                                best_directions.append([direction, cross])
                            if distance == lowest_distance:
                                best_directions.append([direction, cross])
                    
                    if best_directions == []:
                        reset += 1
                        break
                    
                    move_direction = random.choice(best_directions)
                    while move_direction[1]:
                        ran = random.randint(0,101)
                        if ran < 10 * reset:
                            # print(f"hoi {reset}")
                            self.cross_counter += 1
                            break
                        else:
                            move_direction = random.choice(best_directions)

                    coordinates_to = (coordinates_from[0] + move_direction[0][0], coordinates_from[1] + move_direction[0][1], coordinates_from[2] + move_direction[0][2])

                    moves += 1
                    new_netlist = net.Net(coordinates_from, coordinates_to)
                    nets.append(new_netlist)

                    coordinates_from = coordinates_to 
                    current_x = coordinates_to[0]
                    current_y = coordinates_to[1]
                    current_z = coordinates_to[2]

                if coordinates_to == coordinates_destination:
                    break
            
            self.grid_file.add_route(nets, self.cross_counter)
            if self.count > 1:
                gate_a = self.grid_file.get_current_gate_number(origin_x, origin_y)
                gate_b = self.grid_file.get_current_gate_number(destination_x, destination_y)
                print(f"connected:{gate_a} to {gate_b} | Origin: {coordinates_origin}, destination: {coordinates_destination}, current: {coordinates_from}, reset: {reset}, count: {self.count}")
            self.count += 1

            # output_coordinates = []
            # for count, item in enumerate(nets, 1):
            #     print(count)
            #     if count == 1:
            #         coordinates = item.get_coordinates_from()
            #         x = coordinates[0]
            #         y = coordinates[1]
            #         gate_a = grid_file.get_current_gate_number(x, y)
            #         gate_a = self.get_current_gate_number(x, y)
            #         print(gate_a)
            #         output_coordinates.append(coordinates)
                
            #     output_coordinates.append(item.get_coordinates_to())

            # coordinates = output_coordinates[-1]
            # x = coordinates[0]
            # y = coordinates[1]
            # gate_b = self.get_current_gate_number(x, y)

            # gate = (gate_a, gate_b)

            # output.write(f'{str(gate)},"{str(output_coordinates)}"\n')

        print("The total cost of the net is: ", self.grid_file.cost_of_route())
        return True

class PopulationGreedy(Greedy):
    """
    The PopulationGreedy Class sorts the gates by most connections,
    The gate with the most connections is first.
    """
    def get_netlists(self, grid_file):
        """
        Counts how many connections each chip has and returns the order from high to low.
        """
        netlists = list(grid_file.get_netlists())
        counting = {}

        for item in netlists:
            counting[int(item[0])] = 0
            counting[int(item[1])] = 0
        for item in netlists:
            counting[int(item[0])] += 1
            counting[int(item[1])] += 1

        populated_netlists = []

        while len(counting) != 0:
            gate_max = max(counting, key=lambda key: counting[key])
            del counting[gate_max]

            for item in netlists:
                if int(item[0]) == gate_max or int(item[1]) == gate_max:
                    populated_netlists.append(item)
                    netlists.remove(item)

        # print(populated_netlists)
        # print(len(populated_netlists))
        return populated_netlists

class LengthGreedy(Greedy):
    def get_netlists(self, grid_file):
        netlists = list(grid_file.get_netlists())

        netlist_distance = {}

        for item in netlists:
            coordinates_gates = grid_file.get_coordinates_netlist(item)
            distance = abs(coordinates_gates[0] - coordinates_gates[2]) + abs(coordinates_gates[1] - coordinates_gates[3])
            netlist_distance[item] = distance

        length_netlists = []

        while len(netlist_distance) != 0:
            min_distance = min(netlist_distance, key=lambda key: netlist_distance[key])
            length_netlists.append(min_distance)
            del netlist_distance[min_distance]
        
        return length_netlists

class BestScoreGreedy(Greedy):
    def best_netlist(self):
        best_netlist = [('15', '44'), ('13', '6'), ('31', '41'), ('22', '34'), ('25', '30'), ('22', '43'), ('4', '15'), ('15', '35'), ('35', '20'), ('31', '33'), ('40', '4'), ('9', '5'), ('50', '29'), ('38', '41'), ('34', '32'), ('4', '11'), ('35', '3'), ('1', '4'), ('27', '42'), ('39', '50'), ('28', '39'), ('2', '21'), ('45', '29'), ('31', '8'), ('17', '9'), ('47', '30'), ('30', '38'), ('19', '43'), ('45', '35'), ('6', '18'), ('33', '26'), ('41', '48'), ('48', '45'), ('14', '46'), ('34', '8'), ('50', '13'), ('17', '11'), ('28', '37'), ('6', '42'), ('49', '3'), ('47', '1'), ('13', '10'), ('38', '44'), ('12', '11'), ('37', '21'), ('38', '3'), ('15', '17'), ('28', '48'), ('46', '39'), ('27', '40'), ('40', '39'), 
        ('7', '34'), ('44', '32'), ('23', '45'), ('2', '12'), ('16', '23'), ('2', '14'), ('13', '37'), ('26', '7'), ('2', '38'), ('4', '22'), ('18', '36'), ('12', '46'), ('15', '47'), ('39', '8'), ('1', '40'), ('49', '35'), ('33', '3'), ('6', '40'), ('26', '18')]
        return best_netlist





