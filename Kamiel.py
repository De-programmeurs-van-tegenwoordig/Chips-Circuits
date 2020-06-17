import matplotlib.pyplot as plt
from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
from code.algorithms import greedy as gr
from code.algorithms import astar as ast
from code.algorithms import hillclimber as hc
import csv
import time
import random
from mpl_toolkits import mplot3d

if __name__ == '__main__':
    # Read multiple files
    chip_number = "0"
    netlist_number = "1"
    size = 17
    test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

    output = open("chip2netlistLength.csv", "a")
    output.write("versie,cost,counter\n")

    # --------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    
    # random_solve.random_solve3D(test_grid)
   
    greedy = gr.Greedy(test_grid)
    pg.plot_grid(test_grid, chip_number, netlist_number)

    # reset = False
    # counter = 0

    # while not reset:
    #     print(counter)
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #     greedy = gr.Greedy(test_grid)
    #     reset = greedy.run(output)
    #     counter += 1

    # pop_greedy = gr.PopulationGreedy(test_grid)
    # pop_greedy.run(output)

    # while not reset:
    #     print(counter)
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #     len_greedy = gr.LengthGreedy(test_grid)
    #     reset = len_greedy.run(output)
    #     counter += 1

    # cost = test_grid.cost_of_route()

    # output.write(f"chip_{0}_net_{1},{cost},{counter}")
    # output.close()
    # x = 0
    # while x < 100:
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #     astar = ast.Astar(test_grid, False)
    #     start_time = time.time()
    #     astar.run(output)
    #     cost = test_grid.cost_of_route()
    #     Cost_csv = open("Cost.csv", "a")
    #     Time_csv = open("Time.csv", "a")
    #     print("--- %s seconds ---" % (time.time() - start_time))
    #     Time_csv.write(f"{(time.time() - start_time)}\n")
    #     Cost_csv.write(f"{cost}\n")
    #     print(cost)
    #     x += 1

    # x = 0
    # best_cost = float("inf")
    # best_netlist = 0
    # while x < 50:
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #     astar = ast.Astar(test_grid, True)
    #     start_time = time.time()
    #     astar.run(output)
    #     cost = test_grid.cost_of_route()
    #     Cost_csv = open("Cost.csv", "a")
    #     Time_csv = open("Time.csv", "a")
    #     print("--- %s seconds ---" % (time.time() - start_time))
    #     Time_csv.write(f"{(time.time() - start_time)}\n")
    #     Cost_csv.write(f"{cost}\n")
    #     print(cost)
    #     x += 1

    # # Plot the graph
    # pg.plot_grid(test_grid, chip_number, netlist_number)

    # --------------------------While loops to run till solution
    
    
    # reset = False
    # counter = 0

    # while counter != 50:
        
    #     while not reset:
    #         test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
    #         greedy = gr.Greedy(test_grid)
    #         reset = greedy.run(output)

    #     cost = test_grid.cost_of_route()
    #     output.write(f"Greedy,{cost},{counter}\n")
    #     counter += 1
    #     reset = False

    # output.write("\n\n")
    # print("normal greedy done")

    # reset = False
    # counter = 0
    
    # while counter != 50:

    #     while not reset:
    #         test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
    #         pop_greedy = gr.PopulationGreedy(test_grid)
    #         reset = pop_greedy.run(output)

    #     cost = test_grid.cost_of_route()
    #     output.write(f"GreedyPopulation,{cost},{counter}\n")
    #     counter += 1
    #     reset = False

    # output.write("\n\n")
    # print("population klaar")


    # reset = False
    # counter = 0

    # while counter != 50:

    #     while not reset:
    #         test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
    #         len_greedy = gr.LengthGreedy(test_grid)
    #         reset = len_greedy.run(output)

    #     cost = test_grid.cost_of_route()
    #     output.write(f"GreedyLength,{cost},{counter}\n")
    #     counter += 1
    #     reset = False

    # print("korste lengte eerst klaar")




# hill_climber = hc.HillClimber(chip_number, netlistfile, size)

# results = hill_climber.Climb()

# print("netlists: ",results[0], " score: ", results[1])


    # reset = False
    # counter = 0

#     output.write(f"Dit is greedy weigth 5\n")
#     while counter != 100:
        
#         while not reset:
#             test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
#             greedy = gr.Greedy(test_grid)
#             reset = greedy.run(output)

#         cost = test_grid.cost_of_route()
#         output.write(f"Greedy,{cost},{counter}\n")
#         counter += 1
#         print(counter)
#         reset = False

#     output.write("\n\n")
#     print("normal greedy done")

#         while not reset:
#             test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
#             greedy = gr.Greedy(test_grid)
#             reset = greedy.run(output)


#     reset = False
#     counter = 0
    
#     output.write(f"Dit is greedy weigth 10\n")
#     while counter != 100:

    # while not reset:
    #     print( f"reset = {counter}")
    #     counter += 1
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
    #     pop_greedy = gr.LengthGreedy(test_grid)
    #     reset = pop_greedy.run(output)
    # pg.plot_grid(test_grid)

#         cost = test_grid.cost_of_route()
#         output.write(f"GreedyPopulation,{cost},{counter}\n")
#         counter += 1
#         print(counter)
#         reset = False

#     output.write("\n\n")
#     print("population klaar")

    #     cost = test_grid.cost_of_route()
    #     output.write(f"GreedyPopulation,{cost},{counter}\n")
    #     counter += 1
    #     reset = False

    # output.write("\n\n")
    # print("population klaar")

#     reset = False
#     counter = 0

#     output.write(f"Dit is greedy weigth 20\n")
#     while counter != 100:

    # while not reset:
    #     test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
    #     len_greedy = gr.LengthGreedy(test_grid)
    #     reset = len_greedy.run(output)
    # pg.plot_grid(test_grid)

#         cost = test_grid.cost_of_route()
#         output.write(f"GreedyLength,{cost},{counter}\n")
#         counter += 1
#         print(counter)
#         reset = False

#     print("korste lengte eerst klaar")

#     output.close()

    # 
