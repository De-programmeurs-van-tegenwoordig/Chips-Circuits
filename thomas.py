import matplotlib.pyplot as plt
from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
from code.algorithms import greedy as gr
from code.algorithms import astar as ast
import pickle
import csv
import random


# Read multiple files
chip_number = "2"
netlist_number = "8"
size = 17
test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
counter = 0

while counter != 25:
    reset = False
    while not reset:
        test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
        astar = ast.PopAstar(test_grid)
        reset = astar.run()

    cost = test_grid.cost_of_route()
    print("cost after astar", cost)

    # # to load a previously saved test grid
    filehandler = open(f'Netlist{netlist_number}.obj', 'rb')
    saved_grid = pickle.load(filehandler)
    cost_saved_grid = saved_grid.cost_of_route()

    # # print(cost_saved_grid)
    # # to save the test grid
    if cost < cost_saved_grid:
        filehandler = open(f'Netlist{netlist_number}.obj', 'wb')
        pickle.dump(test_grid, filehandler)
        pg.plot_grid(test_grid, chip_number, netlist_number, cost, "Astar")
        print("dumped")
    
    counter += 1
    print(counter)
    
    # cost = test_grid.cost_of_route()
    # print("kostte voor sima", cost)
    # simA = siman.SimulatedAnnealing(test_grid)
    # result = simA.run(cost)
    # cost = result[0]
    # print("kostte uit sima", cost)
    
    # plt.plot(result[1])
    # plt.show()
    
    
    
    
    
    # counter = 0

    # while counter <= 2:

    #     reset = False
    #     counter += 1
    #     while not reset:
    #         test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #         astar = gr.LengthGreedy(test_grid)
    #         reset = astar.run(0)
            
    #     cost = test_grid.cost_of_route()    
    #     print(cost, counter)
    #     pg.plot_grid(test_grid, chip_number, netlist_number, cost)
    
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