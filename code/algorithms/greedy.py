from code.classes import net
from code.function import check_constraints
import random

class Greedy:
    def __init__(self, grid_file):
        """
        The Greedy class looks for the cheapest possible path between two gates
        """
        self.grid_file = grid_file
        self.cross_counter = 0
        self.count = 1

    def get_netlists(self, gridfile):
        """
        Returns the netlist in random order
        """
        netlists = list(self.grid_file.get_netlists())
        return netlists

    def get_current_gate_number(self, coordinate_x, coordinate_y):
        """
        Used for the output file to track which net is being written
        """
        gates = self.grid_file.get_gates()

        for i in range(1, len(gates)+1):
            coordinates = gates[i].get_coordinates()
            x = int(coordinates[0])
            y = int(coordinates[1])

            if x == coordinate_x and y == coordinate_y:
                return gates[i].get_gate_number()

    def run(self, output):
        """
        Greedily chooses cheapest paths to get to his destination
        """
        netlists = self.get_netlists(self.grid_file)

        while len(netlists) != 0:
            netlist = self.grid_file.get_coordinates_netlist(netlists[0])
            netlists.pop(0)
            reset = 1

            while reset != 20:
                origin_x = netlist[0]
                origin_y = netlist[1]
                destination_x = netlist[2]
                destination_y = netlist[3]
                
                directions = [(0,0,1), (0,0,-1), (0,-1,0), (1,0,0), (0,1,0), (-1,0,0)]
                nets = []

                # Set the beginning and endpoint up
                coordinates_from = (origin_x, origin_y, 0)
                coordinates_destination = (destination_x, destination_y, 0)

                # Update the variables
                current_x = origin_x
                current_y = origin_y
                destination_z = 0
                current_z = 0

                moves = 0
                # max_moves = 70
                # move_reset = 0

                # While line has not reached endpoint
                while current_x != destination_x or current_y != destination_y or current_z != destination_z:
                    # werkt nog niet maar snap niet hoezo
                    # if moves > max_moves:
                    #     move_reset += 1
                    #     nets = []
                    #     current_x = origin_x
                    #     current_y = origin_y
                    #     current_z = 0
                    #     moves = 0

                    lowest_distance = 10000000
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
                        # print(f"reset {reset}")
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
                
                self.grid_file.add_route(nets, self.cross_counter)

                coordinates_origin = (origin_x, origin_y, 0)
                # print("route connected:", coordinates_origin, coordinates_destination, self.count)
                self.count += 1
                break

            # output_coordinates = []
            # for count, item in enumerate(nets, 1):
            #     if count == 1:
            #         coordinates = item.get_coordinates_from()
            #         x = coordinates[0]
            #         y = coordinates[1]

            #         gate_a = self.get_current_gate_number(x, y)
            #         output_coordinates.append(coordinates)
                
            #     output_coordinates.append(item.get_coordinates_to())

            # coordinates = output_coordinates[-1]
            # x = coordinates[0]
            # y = coordinates[1]
            # gate_b = self.get_current_gate_number(x, y)

            # gate = (gate_a, gate_b)

            # output.write(f'{str(gate)},"{str(output_coordinates)}"\n')

        print("The total cost of the net is: ", self.grid_file.cost_of_route())

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

        print(populated_netlists)
        return populated_netlists
