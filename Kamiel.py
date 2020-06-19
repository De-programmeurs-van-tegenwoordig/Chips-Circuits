import matplotlib.pyplot as plt
from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
import time
from code.algorithms import random_solve as rs
from code.algorithms import greedy as gr
from code.algorithms import astar as ast
import csv
import time
import random

if __name__ == '__main__':
    # Read multiple files
    chip_number = "1"
    netlist_number = "4"
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

    output = open("chip2netlistLength.csv", "a")

    counter = 0

    # start_time = time.time()
    # rs.random_solve3D(test_grid)
    # print("--- %s seconds ---" % (time.time() - start_time))
    # while counter <= 50:

    #     reset = False
    #     counter += 1
    #     while not reset:
    #         test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #         astar = ast.PopAstar(test_grid)
    #         reset = astar.run(output)
            
    #     cost = test_grid.cost_of_route()    
    #     print(cost)
    #     pg.plot_grid(test_grid, chip_number, netlist_number, cost)
    
    open_GrAs = open("GrAs.csv", "a")
    
    while counter <= 50:
        reset = False
        while not reset:
            print("hoi")
            start_time = time.time()
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
            greedy = gr.LengthGreedy(test_grid)
            reset = greedy.run(output)
            print(reset)
            times = (time.time() - start_time)

        print(f"--- {times }seconds ---")
        cost = test_grid.cost_of_route()
        open_GrAs.write(f"Greedy, {times}, {cost} \n")
        reset = False
        
        while not reset:
            st_time = time.time()
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
            astar = ast.LengthAstar(test_grid)
            reset = astar.run(output)
            times = (time.time() - st_time)

        print("--- %s seconds ---" % (times))
        cost = test_grid.cost_of_route()
        open_GrAs.write(f"Astar, {times}, {cost} \n")
        counter += 1
 