import matplotlib.pyplot as plt
from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
from code.algorithms import greedy as gr
import csv
import random
from mpl_toolkits import mplot3d

if __name__ == '__main__':
    # Read multiple files
    chip_number = "2"
    netlistfile = "netlist_9.csv"
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)

    # --------------------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    # random_solve.random_solve3D(test_grid)
    output = open("output.csv", "w")
    output.write("net,wires\n")

    greedy = gr.Greedy(test_grid)
    greedy.run(output)

    cost = test_grid.cost_of_route()

    output.write(f"chip_{0}_net_{1},{cost}")
    output.close()

    # Plot the graph
    pg.plot_grid(test_grid)