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

def run():
    # Read multiple files
    chip_number = "1"
    netlist_number = "5"
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

    output = open("chip2netlistLength.csv", "a")

    counter = 0

    while counter <= 2:

        reset = False
        counter += 1
        while not reset:
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
            astar = gr.LengthGreedy(test_grid)
            reset = astar.run(0)
            
        cost = test_grid.cost_of_route()    
        print(cost, counter)
        pg.plot_grid(test_grid, chip_number, netlist_number, cost)
    
    # chip_number = "0"
    # netlist_number = "2"
    # size = 17
    # test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

    # output = open("chip2netlistLength.csv", "a")

    # counter = 0

    # while counter <= 2:

    #     reset = False
    #     counter += 1
    #     while not reset:
    #         test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #         astar = ast.PopAstar(test_grid)
    #         reset = astar.run(output)
            
    #     cost = test_grid.cost_of_route()    
    #     print(cost, counter)
    #     pg.plot_grid(test_grid, chip_number, netlist_number, cost)
    
    # chip_number = "0"
    # netlist_number = "3"
    # size = 17
    # test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

    # output = open("chip2netlistLength.csv", "a")

    # counter = 0

    # while counter <= 2:

    #     reset = False
    #     counter += 1
    #     while not reset:
    #         test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #         astar = ast.PopAstar(test_grid)
    #         reset = astar.run(output)
            
    #     cost = test_grid.cost_of_route()    
    #     print(cost, counter)
    #     pg.plot_grid(test_grid, chip_number, netlist_number, cost)


    # Plot the graph
    # pg.plot_grid(test_grid, chip_number, netlist_number, cost)