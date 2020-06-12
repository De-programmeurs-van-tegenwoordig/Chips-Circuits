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
    netlistfile = "netlist_6.csv"
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)

    output = open("output.csv", "w")
    output.write("net,wires\n")

    # --------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    
    # random_solve.random_solve3D(test_grid)

    greedy = gr.Greedy(test_grid)
    greedy.run(output)

    # pop_greedy = gr.PopulationGreedy(test_grid)
    # pop_greedy.run(output)

    # reset = False

    # while not reset:
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
    #     greedy = gr.Greedy(test_grid)
    #     reset = greedy.run(output)
    #     print("dit gaat lang duren")

    # while not reset:
    #     print("dit gaat lang duren")
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
    #     pop_greedy = gr.PopulationGreedy(test_grid)
    #     pop_greedy.run(output)

    cost = test_grid.cost_of_route()

    output.write(f"chip_{0}_net_{1},{cost}")
    output.close()

    # Plot the graph
    pg.plot_grid(test_grid)