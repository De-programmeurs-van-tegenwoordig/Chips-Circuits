from code.classes import net
from code.function import check_constraints
import random

def greedy(grid_file):
    cross_counter = 0
    count = 0
    netlist = grid_file.get_new_netlist()

    greedy2(grid_file, cross_counter, netlist, count)


def greedy2(grid_file, cross_counter, netlist, count):
    while netlist is not None:
        origin_x = netlist[0]
        origin_y = netlist[1]
        destination_x = netlist[2]
        destination_y = netlist[3]
        
        directions = [(0,0,1), (0,0,-1), (0,-1,0), (1,0,0), (0,1,0), (-1,0,0)]
        nets = set()

        # Set the beginning and endpoint up
        coordinates_from = (origin_x, origin_y, 0)
        coordinates_destination = (destination_x, destination_y, 0)

        # Update the variables
        current_x = origin_x
        current_y = origin_y
        destination_z = 0
        current_z = 0

        moves = 0

        # While line has not reached endpoint
        while current_x != destination_x or current_y != destination_y or current_z != destination_z:
            lowest_distance = 1000000
            best_directions = []

            for direction in directions:

                coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1], coordinates_from[2] + direction[2])
                results = check_constraints.check_constraints(grid_file, coordinates_from, coordinates_to, coordinates_destination, nets)

                check = results[0]
                cross = results[1]

                if check:
                    distance = abs(coordinates_to[0] - coordinates_destination[0]) + abs(coordinates_to[1] - coordinates_destination[1]) + abs(coordinates_to[2] - coordinates_destination[2])
                    # if cross:
                    #     distance += 300
                    if distance < lowest_distance:
                        best_directions.clear()
                        lowest_distance = distance
                        best_directions.append([direction, cross])
                    if distance == lowest_distance:
                        best_directions.append([direction, cross])
            
            if best_directions == []:
                return greedy2(grid_file, cross_counter, netlist, count)
            
            move_direction = random.choice(best_directions)
            while move_direction[1]:
                ran = random.randint(0,101)
                if ran < 10:
                    cross_counter += 1
                    break
                else:
                    move_direction = random.choice(best_directions)

            coordinates_to = (coordinates_from[0] + move_direction[0][0], coordinates_from[1] + move_direction[0][1], coordinates_from[2] + move_direction[0][2])

            moves += 1
            new_netlist = net.Net(coordinates_from, coordinates_to)
            nets.add(new_netlist)
            coordinates_from = coordinates_to 
            current_x = coordinates_to[0]
            current_y = coordinates_to[1]
            current_z = coordinates_to[2]

            # wanneer de route klaar is doen we dit:
            # add route to list of netlists
        
        grid_file.add_netlist(nets, cross_counter)
        netlist = grid_file.get_new_netlist()
        coordinates_origin = (origin_x, origin_y, 0)
        print("route connected:", coordinates_origin, coordinates_destination, count)
        count += 1
    
    print("The total cost of the net is: ", grid_file.cost_of_route())

        # Returns the list with lines and the amount of moves
        # return moves, cross_counter
        
            
            
