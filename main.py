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

    output = open("chip1netlist6weigth.csv", "a")
    output.write("versie,cost,counter\n")

    # --------------------------------------------Perform the desired algoritm--------------------------------------------------------------
    
    # random_solve.random_solve3D(test_grid)

    # greedy = gr.Greedy(test_grid)
    # greedy.run(output)

    # pop_greedy = gr.PopulationGreedy(test_grid)
    # pop_greedy.run(output)

    # len_greedy = gr.LengthGreedy(test_grid)
    # len_greedy.run(output)

    # cost = test_grid.cost_of_route()

    # output.write(f"chip_{0}_net_{1},{cost},{counter}")
    # output.close()

    # Plot the graph
    # pg.plot_grid(test_grid)

    # --------------------------While loops to run till solution
    
    
    reset = False
    counter = 0

    output.write(f"Dit is greedy weigth 5\n")
    while counter != 10:
        
        while not reset:
            weigth = 5
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
            len_greedy = gr.LengthGreedy(test_grid)
            reset = len_greedy.run(output, weigth)

        cost = test_grid.cost_of_route()
        output.write(f"{cost}\n")
        counter += 1
        reset = False

    output.write("\n\n")
    print("Weigth 5 done")



    reset = False
    counter = 0
    
    output.write(f"Dit is greedy weigth 10\n")
    while counter != 10:

        while not reset:
            weigth = 10
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
            len_greedy = gr.LengthGreedy(test_grid)
            reset = len_greedy.run(output, weigth)

        cost = test_grid.cost_of_route()
        output.write(f"{cost}\n")
        counter += 1
        reset = False

    output.write("\n\n")
    print("Weigth 10 done")


    reset = False
    counter = 0

    output.write(f"Dit is greedy weigth 20\n")
    while counter != 10:

        while not reset:
            weigth = 20
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/{netlistfile}", size)
            len_greedy = gr.LengthGreedy(test_grid)
            reset = len_greedy.run(output, weigth)

        cost = test_grid.cost_of_route()
        output.write(f"{cost}\n")
        counter += 1
        reset = False

    print("Weigth 20 Done")

    output.close()


    