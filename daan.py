import matplotlib.pyplot as plt
from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
from code.algorithms import greedy as gr
from code.algorithms import astar as ast
from code.algorithms import simannealing as siman
from code.algorithms import hillclimber as hc
import csv
import pickle
import random

if __name__ == '__main__':
    # Read multiple files
    chip_number = "1"
    netlist_number = "4"
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

    # --------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    
    # random_solve.random_solve3D(test_grid)

    # reset = False

    # while not reset:
    #     print("ik ben gereset")
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #     greedy = gr.PopulationGreedy(test_grid)
    #     reset = greedy.run()
        
    # cost = test_grid.cost_of_route()
    # pg.plot_grid(test_grid, chip_number, netlist_number, cost, "greedy")

    reset = False
    while not reset:
        test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
        astar = ast.PopAstar(test_grid)
        reset = astar.run()

    cost = test_grid.cost_of_route()
    print("cost after astar", cost)
    filehandler = open(f'Netlist{netlist_number}.obj', 'wb')
    pickle.dump(test_grid, filehandler)
    print("dumped")

    filehandler = open(f'Netlist{netlist_number}.obj', 'rb')
    test_grid = pickle.load(filehandler)
    cost = test_grid.cost_of_route()
    print("kostte voor sima", cost)
    simA = siman.SimulatedAnnealing(test_grid)
    result = simA.run(cost)
    cost = result[0]
    print("kostte uit sima", cost)
    
    print(result[1])
    plt.plot(result[1])
    plt.show()
    
    # Plot the graph
    pg.plot_grid(test_grid, chip_number, netlist_number, cost, "Astar")

    # --------------------------While loops to run till solution
    
    # reset = False
    # counter = 0

    # while counter != 50:
        
    #     while not reset:
    #         test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
    #         greedy = gr.Greedy(test_grid)
    #         reset = greedy.run()

    #     cost = test_grid.cost_of_route()
    #     output.write(f"Greedy,{cost},{counter}\n")
    #     counter += 1
    #     reset = False

    # output.write("\n\n")
    # print("normal greedy done")