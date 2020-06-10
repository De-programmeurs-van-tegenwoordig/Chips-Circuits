import matplotlib.pyplot as plt
from code.function import plot_grid
from code.classes import gate
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
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)


    # --------------------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    # result = random_solve.random_solve3D(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter, list_of_coordinates, 0)

    greedy.greedy(test_grid)


    # Plot the graph
    plot_grid.plot_grid(test_grid)