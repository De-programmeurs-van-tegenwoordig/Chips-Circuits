import random
from code.classes import net
from code.function  import check_constraints

def random_solve3D(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter, list_of_coordinates, restart):
    """ Returns a random 3d solution of the given problem (netlist and chipset) """
    
    # Declaring local variables
    tries = 0
    directions = [(0,1,0), (1,0,0), (0,-1,0), (-1,0,0), (0,0,1), (0,0,-1)]
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
    crosses = 0
    max_moves = 50
    restart += 1

    # While line has not reached endpoint
    while current_x != destination_x or current_y != destination_y or current_z != destination_z:
        
        # Update tries and if amount tries exceed treshold restart line
        tries += 1
        if tries == 2000 or moves > max_moves:
            return random_solve3D(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter, list_of_coordinates, restart)

        # Update variables
        count = 0
        check = True
        direction = random.choice(directions)
        coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1], coordinates_from[2] + direction[2])
        

        # Checks if line is good
        check = check_constraints.check_constraints(coordinates_from, coordinates_to, coordinates_destination, list_of_nets, nets, list_of_coordinates, size)

        if count == 2:
            check = False
        
        # Append the line to the list if everything checks out
        if check[0]:
            moves += 1
            new_netlist = net.Net(coordinates_from, coordinates_to)
            nets.add(new_netlist)
            coordinates_from = coordinates_to 
            current_x = coordinates_to[0]
            current_y = coordinates_to[1]
            current_z = coordinates_to[2]
            if check[1]:
                crosses += 1

    # Returns the list with lines and the amount of moves
    print(f"route {counter} needed {restart} restarts")
    return nets, moves, crosses

def random_solve(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter, list_of_coordinates):
    tries = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    nets = set()
    coordinates_from = (origin_x, origin_y)

    current_x = origin_x
    current_y = origin_y

    while current_x != destination_x or current_y != destination_y:
        tries += 1
        if tries == 2000:
            return nets, tries
        count = 0
        check = True
        direction = random.choice(directions)
        coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1])
        
        if coordinates_to[0] > size  or coordinates_to[1] > size  or coordinates_to[0] <= 0 or coordinates_to[1] <= 0:
            check = False

        for i in range(len(list_of_nets)):
            for x in list_of_nets[i]:
                net_from = x.get_coordinates_from()
                net_to = x.get_coordinates_to()

                # if (coordinates_to[0] == net_from[0] and coordinates_to[1] == net_from[1]) or (coordinates_to[0] == net_to[0] and coordinates_to[1] == net_to[1]):
                if coordinates_to == net_from or coordinates_to == net_to:
                    count += 1
                if coordinates_from == net_from and coordinates_to == net_to:
                    check = False
                    break
                if coordinates_from == net_to and coordinates_to == net_from:
                    check = False
                    break
                if coordinates_to in list_of_coordinates and coordinates_to[0] != destination_x and coordinates_to[1] != destination_y:
                    check = False
                    break
                # f.write(str(coordinates_from) + str(net_from) + str(check) + str(counter) + str(coordinates_to) + str(net_to) + "\n")
                # print(coordinates_from,net_from, check, coordinates_to, net_to)

        for i in nets:
            net_from = i.get_coordinates_from()
            net_to = i.get_coordinates_to()

            if coordinates_to == net_from or coordinates_to == net_to:
                    count += 1
            if coordinates_from == net_from and coordinates_to == net_to:
                check = False
                break
            if coordinates_from == net_to and coordinates_to == net_from:
                check = False
                break
            if coordinates_to in list_of_coordinates and coordinates_to[0] != destination_x and coordinates_to[1] != destination_y:
                check = False
                break

        if count == 2:
            check = False
        
        if check:
            new_netlist = net.Net(coordinates_from, coordinates_to)
            nets.add(new_netlist)
            coordinates_from = coordinates_to 
            current_x = coordinates_to[0]
            current_y = coordinates_to[1]

    return nets