import matplotlib.pyplot as plt
from code.function import plot_grid
from code.classes import chip
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
from code.algorithms import greedy
import csv
import random
from mpl_toolkits import mplot3d


if __name__ == '__main__':
    
    # Read multiple files
    chip_number = "1"
    netlistfile = "netlist_4.csv"
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}")
    
    # Declare global variables
    size = 17
    checkpoint = 0
    tries = 0
    counter = 0
    
    # Get coordinates chips
    chips = test_grid.get_chips()
    
    # Declare global lists
    list_of_coordinates = []
    x = []
    y = []

    # Get netlist from the file
    netlists = test_grid.get_netlists()
    net_needed = 0
    list_of_nets = {}

    # All coordinates in multiple lists
    for item in chips:
        coordinates = chips[item].get_coordinates()
        
        x_coordinate = int(coordinates[0])
        y_coordinate = int(coordinates[1])
        coordinates = (x_coordinate, y_coordinate, 0)

        list_of_coordinates.append(coordinates)
        x.append(x_coordinate)
        y.append(y_coordinate)

    # For every netlist form the connections
    for netlist in netlists:
        
        # Get local variables
        origin = int(netlist[0])
        destination = int(netlist[1])
        
        chip_origin = chips[origin]
        chip_destination = chips[destination]

        coordinates_origin = chip_origin.get_coordinates()
        coordinates_destination = chip_destination.get_coordinates()

        origin_x = int(coordinates_origin[0])
        origin_y = int(coordinates_origin[1])

        destination_x = int(coordinates_destination[0])
        destination_y = int(coordinates_destination[1])
         
        # Perform the desired algoritm
        # result = random_solve.random_solve3D(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter, list_of_coordinates, 0)
        result = greedy.greedy(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, list_of_coordinates, counter)

        # Calculate the amount of tries and net_needed
        list_of_nets[counter] = result[0]
        counter += 1
        net_needed += result[1] + 300 * result[2]

        checkpoint += 1
        if checkpoint == 28:
            break

    # Plot the graph
    plot_grid.plot_grid(x, y, size, list_of_nets)

    # Show the net_needed
    print("Cost of routes", net_needed)

    plt.show()