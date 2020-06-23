import random
from code.classes import net
from code.function  import check_constraints

def random_solve3D(grid_file):
    """
    Sets variables to begin value and runs the random algorithm
    """
    cross_counter = []
    count = 0
    netlist = grid_file.get_new_netlist()
    
    random_solve3D2(grid_file, cross_counter, netlist, count)
    return True

def random_solve3D2(grid_file, cross_counter, netlist, count):
    """ 
    Returns a random 3d solution of the given problem (netlist and chipset)
    """
    cross_counter = []

    # Loops till netlist is empty
    while netlist is not None:
        origin_x = netlist[0]
        origin_y = netlist[1]
        destination_x = netlist[2]
        destination_y = netlist[3]
        nets = []

        # Declaring local variables
        tries = 0
        directions = [(0,1,0), (1,0,0), (0,-1,0), (-1,0,0), (0,0,1), (0,0,-1)]
        
        # Set the beginning and endpoint up
        coordinates_from = (origin_x, origin_y, 0)
        coordinates_destination = (destination_x, destination_y, 0)
 
        # Update the variables
        current_x = origin_x
        current_y = origin_y
        destination_z = 0
        current_z = 0

        moves = 0
        max_moves = 50

        # Loops while line has not reached endpoint
        while current_x != destination_x or current_y != destination_y or current_z != destination_z:
            
            # Update tries and if amount tries exceed treshold restart line
            tries += 1
            if tries == 2000 or moves > max_moves:
                return random_solve3D2(grid_file, cross_counter, netlist, count)

            # Update variables
            check = True
            direction = random.choice(directions)
            coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1], coordinates_from[2] + direction[2])
            
            # Checks if line is good
            check = check_constraints.check_constraints(grid_file, coordinates_from, coordinates_to, coordinates_destination, nets)
            
            # Append the line to the list if everything checks out
            if check[0]:
                moves += 1
                new_netlist = net.Net(coordinates_from, coordinates_to)
                nets.append(new_netlist)
                coordinates_from = coordinates_to 
                current_x = coordinates_to[0]
                current_y = coordinates_to[1]
                current_z = coordinates_to[2]
                if check[1] is not None:
                    cross_counter.append(check[1])

        grid_file.add_route(nets, cross_counter)
        netlist = grid_file.get_new_netlist()
        coordinates_origin = (origin_x, origin_y, 0)
        print("route connected:", coordinates_origin, coordinates_destination, count)
        count += 1
        
    print("The total cost of the net is: ", grid_file.cost_of_route())
    return grid_file.cost_of_route()


def random_solve(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter, list_of_coordinates, grid_file):
    """ 
    Returns a random 3d solution of the given problem (netlist and chipset)
    """

    # Declares begin variables to begin values
    tries = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    nets = set()
    coordinates_from = (origin_x, origin_y)
    coordinates_destination = (destination_x, destination_y)

    current_x = origin_x
    current_y = origin_y

    # While line has not reached endpoint
    while current_x != destination_x or current_y != destination_y:
        tries += 1
        if tries == 2000:
            return nets, tries
        count = 0
        check = True
        direction = random.choice(directions)
        coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1])
        
        # Checks constraint for a 2D grid
        check = check_constraints.check_constraints(grid_file, coordinates_from, coordinates_to, coordinates_destination, nets)

        if count == 2:
            check = False
        
        # Append the line to the list if everything checks out
        if check[0]:
            new_netlist = net.Net(coordinates_from, coordinates_to)
            nets.add(new_netlist)
            coordinates_from = coordinates_to 
            current_x = coordinates_to[0]
            current_y = coordinates_to[1]

    return nets