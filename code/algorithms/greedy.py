from code.classes import net
from code.function import check_constraints
import random

def greedy(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, list_of_coordinates, counter):
    if counter == 5:
        f = open(f"output{counter}.txt", "w") 
    cross_counter = 0
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

        # random.shuffle(directions)

        for direction in directions:
            print(direction)
            coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1], coordinates_from[2] + direction[2])
            results = check_constraints.check_constraints(coordinates_from, coordinates_to, coordinates_destination, list_of_nets, nets, list_of_coordinates, size)
            check = results[0]
            cross = results[1]

            if check:
                distance = abs(coordinates_to[0] - coordinates_destination[0]) + abs(coordinates_to[1] - coordinates_destination[1]) + abs(coordinates_to[2] - coordinates_destination[2])
                # print("Dit is de distance:", distance, coordinates_to)
                if counter == 5:
                    f.write("distance:" + str(distance) + "  cross" + str(cross) + "  from" + str(coordinates_from) + "  to" + str(coordinates_to) + "\n")

                if cross:
                    distance += 300
                if distance < lowest_distance:
                    best_directions.clear()
                    lowest_distance = distance
                    move_direction = direction
                    cross_lowest = cross
                if distance == lowest_distance:
                    best_directions.append(direction)
        
        coordinates_to = (coordinates_from[0] + move_direction[0], coordinates_from[1] + move_direction[1], coordinates_from[2] + move_direction[2])
        if cross_lowest:
            cross_counter += 1

        print("beweging", coordinates_to, lowest_distance)
        if counter == 5:
            f.write("beweging" + "  from" + str(coordinates_from) + "  to" + str(coordinates_to) + "  lowest" + str(lowest_distance) + "\n\n")
        moves += 1
        new_netlist = net.Net(coordinates_from, coordinates_to)
        nets.add(new_netlist)
        coordinates_from = coordinates_to 
        current_x = coordinates_to[0]
        current_y = coordinates_to[1]
        current_z = coordinates_to[2]

    # Returns the list with lines and the amount of moves
    return nets, moves, cross_counter
        
        
        
            
            