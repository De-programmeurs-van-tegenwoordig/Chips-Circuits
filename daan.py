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
    netlist_number = "5"
    size = 17
    # test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

    # --------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    
    # random_solve.random_solve3D(test_grid)

    
    # om gewoon een netlist te runnen en dan te dumpen met pickle
    # reset = False
    # while not reset:
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #     astar = ast.PopAstar(test_grid)
    #     reset = astar.run()

    # filehandler = open(f'Netlist{netlist_number}.obj', 'wb')
    # pickle.dump(test_grid, filehandler)
    # print("dumped")

    # cost = test_grid.cost_of_route()
    # print(cost)
    # simA = siman.SimulatedAnnealing(test_grid)
    # result = simA.run(cost)
    # cost = result[0]
    # print("kostte uit sima", cost)

    # filehandler = open(f'Netlist{netlist_number}Sim.obj', 'wb')
    # pickle.dump(result[2], filehandler)

    # print(result[1])
    # print(result[3])
    # plt.plot(result[1], color = "r")
    # plt.plot(result[3], color= "b")
    # plt.show()

    # dit is voor gewoon een normale run, die door de sim gooien en dan de cost te plotten
    # reset = False
    # while not reset:
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #     astar = ast.PopAstar(test_grid)
    #     reset = astar.run()

    # cost = test_grid.cost_of_route()
    # print(cost)
    # simA = siman.SimulatedAnnealing(test_grid)
    # result = simA.run(cost)
    # cost = result[0]
    # print("kostte uit sima", cost)

    # print(result[1])
    # print(result[3])
    # plt.plot(result[1], color = "r")
    # plt.plot(result[3], color= "b")
    # plt.show()


    """
    # DIT IS OM STEEDS EEN BETERE OBJECT OP TE SLAAN, maar moet je dus wel er eerst al 1 voor hebben
    counter = 0

    while counter <= 50:
        reset = False
        while not reset:
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
            astar = ast.PopAstar(test_grid)
            reset = astar.run()

        cost = test_grid.cost_of_route()
        print("cost after astar", cost)

        # to load a previously saved test grid
        filehandler = open(f'Netlist{netlist_number}.obj', 'rb')
        saved_grid = pickle.load(filehandler)
        cost_saved_grid = saved_grid.cost_of_route()

        # to save the test grid
        print(f"cost: {cost} ||| cost saved: {cost_saved_grid}")
        if cost < cost_saved_grid:
            pg.plot_grid(test_grid, chip_number, netlist_number, cost, "Astar")
            filehandler = open(f'Netlist{netlist_number}.obj', 'wb')
            pickle.dump(test_grid, filehandler)
            print("dumped")
        
        counter += 1
    """

    # to load a previously saved test grid
    # filehandler = open(f'Netlist{netlist_number}.obj', 'rb')
    # saved_grid = pickle.load(filehandler)
    # cost_saved_grid = saved_grid.cost_of_route()
    # print(cost_saved_grid)

    # cost = saved_grid.cost_of_route()
    # print("kostte voor sima", cost)
    # simA = siman.SimulatedAnnealing(saved_grid)
    # result = simA.run2(cost)
    # cost = result[0]
    # print("kostte uit sima", cost)

    # filehandler = open(f'Netlist{netlist_number}SimRun2.obj', 'wb')
    # pickle.dump(result[2], filehandler)

    # print(result[1])
    # print(result[3])
    # plt.plot(result[1], color = "r")
    # plt.plot(result[3], color= "b")
    # plt.show()
    
    # Plot the graph
    # pg.plot_grid(saved_grid, chip_number, netlist_number, cost_saved_grid, "Astar")

    
    
    # ------------------------------While loops to run till solution
    
    reset = False
    counter = 0

    while counter != 50:
        
        while not reset:
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
            greedy = gr.PopulationGreedy(test_grid)
            reset = greedy.run()

        cost = test_grid.cost_of_route()
        counter += 1
        reset = False

    print("normal greedy done")