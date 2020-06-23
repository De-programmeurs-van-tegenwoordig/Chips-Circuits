from code.classes import net
from code.function import check_constraints
import random

class Greedy:
    def __init__(self, grid_file):
        """
        The Greedy class looks for the cheapest possible path between two gates
        """
        self.grid_file = grid_file

    def get_netlists(self, grid_file):
        """
        Returns the netlist in random order
        """
        netlists = list(self.grid_file.get_netlists())
        random.shuffle(netlists)
        return netlists

    def run(self):
        """
        Greedily chooses cheapest paths to get to his destination
        """
        netlists = self.get_netlists(self.grid_file)
        count = 0

        while len(netlists) != 0:
            netlist = self.grid_file.get_coordinates_netlist(netlists[0])
            netlists.pop(0)

            cross_counter = []
            reset = 1

            # Greedy resets up to a 100 times if it gets stuck
            while reset <= 100:
                if reset == 100:
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

                    # Look at every direction 
                    for direction in directions:
                        coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1], coordinates_from[2] + direction[2])
                        
                        # Check if the line is possible
                        results = check_constraints.check_constraints(self.grid_file, coordinates_from, coordinates_to, coordinates_destination, nets)
                        check = results[0]
                        cross = results[1]

                        # Selects the best direction
                        if check:
                            distance = abs(coordinates_to[0] - coordinates_destination[0]) + abs(coordinates_to[1] - coordinates_destination[1]) + abs(coordinates_to[2] - coordinates_destination[2])
                            if cross is not None:
                                distance += 300
                            if distance < lowest_distance:
                                best_directions.clear()
                                lowest_distance = distance
                                best_directions.append([direction, cross])
                            if distance == lowest_distance:
                                best_directions.append([direction, cross])
                    
                    # If there is no direction, break
                    if best_directions == []:
                        reset += 1
                        break
                    
                    # Randomly choose a best direction
                    move_direction = random.choice(best_directions)
                    while move_direction[1] is not None:
                        ran = random.randint(0,101)
                        if ran < 5 * reset:
                            cross_counter.append(move_direction[1])
                            break
                        else:
                            move_direction = random.choice(best_directions)

                    # Move in direction
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
            
            # Puts line into grid
            self.grid_file.add_route(nets, cross_counter)
            count += 1
            if count % 10 == 0:
                print(f"Route connected: {coordinates_origin}, {coordinates_destination}. Crosses: {cross_counter}. Nummer: {count}")

        # print("The total cost of the net is: ", self.grid_file.cost_of_route())
        return True

class PopulationGreedy(Greedy):
    """
    The PopulationGreedy Class sorts the gates by amount of connections
    The gates with the most connections come first
    """
    def get_netlists(self, grid_file):
        """
        Counts how many connections each chip has and returns the order from high to low.
        """
        netlists = list(grid_file.get_netlists())
        counting = {}

        # Counts the amount of connections
        for item in netlists:
            counting[int(item[0])] = 0
            counting[int(item[1])] = 0
        for item in netlists:
            counting[int(item[0])] += 1
            counting[int(item[1])] += 1

        populated_netlists = []

        # Appends in the right order the netlist
        while len(counting) != 0:
            gate_max = max(counting, key=lambda key: counting[key])
            del counting[gate_max]

            for item in netlists:
                if int(item[0]) == gate_max or int(item[1]) == gate_max:
                    populated_netlists.append(item)
                    netlists.remove(item)

        return populated_netlists

class LengthGreedy(Greedy):
    """
    Returns netlists ordered by length
    """
    def get_netlists(self, grid_file):
        netlists = list(grid_file.get_netlists())

        netlist_distance = {}

        # Calculate distance of all netlists
        for item in netlists:
            coordinates_gates = grid_file.get_coordinates_netlist(item)
            distance = abs(coordinates_gates[0] - coordinates_gates[2]) + abs(coordinates_gates[1] - coordinates_gates[3])
            netlist_distance[item] = distance

        length_netlists = []

        # Sort netlists from shortest to longest
        while len(netlist_distance) != 0:
            min_distance = min(netlist_distance, key=lambda key: netlist_distance[key])
            length_netlists.append(min_distance)
            del netlist_distance[min_distance]
        
        return length_netlists






