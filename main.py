import matplotlib.pyplot as plt
from code.function import plot_grid
from code.classes import chip
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
import csv
import random
from mpl_toolkits import mplot3d


if __name__ == '__main__':
    test_grid = grid.Grid("data/chip_0/print_0.csv", "data/chip_0/netlist_1.csv")
    size = 7
    checkpoint = 0
    tries = 0
    chips = test_grid.get_chips()

    list_of_coordinates = []
    x = []
    y = []

    netlists = test_grid.get_netlists()
    net_needed = 0
    list_of_nets = {}


    for i in chips:
        coordinates = chips[i].get_coordinates()
        
        x_coordinate = int(coordinates[0])
        y_coordinate = int(coordinates[1])
        coordinates = (x_coordinate, y_coordinate, 0)

        list_of_coordinates.append(coordinates)
        x.append(x_coordinate)
        y.append(y_coordinate)

    counter = 0

    for netlist in netlists:
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
         
        result = random_solve.random_solve3D(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter, list_of_coordinates, 0)

        list_of_nets[counter] = result[0]
        counter += 1
        net_needed += result[1]

        checkpoint += 1
        if checkpoint == 5:
            break

    plot_grid.plot_grid(x, y, size, list_of_nets)

    print("Cost of routes", net_needed)

    plt.show()