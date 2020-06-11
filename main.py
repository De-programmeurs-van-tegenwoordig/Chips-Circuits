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
    chip_number = "0"
    netlistfile = "netlist_1.csv"
    size = 7
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)


    # --------------------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    # random_solve.random_solve3D(test_grid)

    greedy.greedy(test_grid)

    # Plot the graph
    plot_grid.plot_grid(test_grid)