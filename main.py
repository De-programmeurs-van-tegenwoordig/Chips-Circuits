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
    chip_number = "1"
    netlistfile = "netlist_4.csv"
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)

    # test = (1, 5, 1)
    # test2 = (1, 5, 1)
    # if test == test2:
    #     print("het kan gwn")

    # --------------------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    # random_solve.random_solve3D(test_grid)
    output = open("output.csv", "w")
    output.write("net,wires\n")

    greedy = gr.Greedy(test_grid)
    greedy.run(output)

    cost = test_grid.cost_of_route()

    output.write(f"chip_0_net_1,{cost}")
    output.close()

    # Plot the graph
    pg.plot_grid(test_grid)