import matplotlib.pyplot as plt
from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
from code.algorithms import greedy as gr
from code.algorithms import astar as ast
import csv
import random

if __name__ == '__main__':
    # Read multiple files
    chip_number = "2"
    netlist_number = "7"
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

    output = open("chip2netlistLength.csv", "a")

    counter = 0

    while counter <= 50:

        reset = False
        counter += 1
        while not reset:
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
            astar = ast.PopAstar(test_grid)
            reset = astar.run(output)
            
        cost = test_grid.cost_of_route()    
        print(cost)
        pg.plot_grid(test_grid, chip_number, netlist_number, cost)

    # Plot the graph
    # pg.plot_grid(test_grid, chip_number, netlist_number, cost)