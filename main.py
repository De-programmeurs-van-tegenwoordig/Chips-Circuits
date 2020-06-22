import matplotlib.pyplot as plt
from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve as rs
from code.algorithms import greedy as gr
from code.algorithms import astar as ast
from code.algorithms import simannealing as siman
import csv
import random

# Declare global variables
chip_number = float('inf')
netlist_number = float('inf')
algorithm = float('inf')
annealing = float('inf')
size = 17
test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

# Request user input: chip number
while chip_number != "0" and chip_number != "1" and chip_number != "2":
    chip_number = input("Welk chipnumber wilt u testen? 0, 1 of 2?    ")

# Request user input: netlist number
if chip_number == "0":
    while netlist_number != "1" and netlist_number != "2" and netlist_number != "3": 
        netlist_number = input("Welke netlist wilt u gebruiken? 1, 2 of 3?   ")
elif chip_number == "1":
    while netlist_number != "4" and netlist_number != "5" and netlist_number != "6": 
        netlist_number = input("Welke netlist wilt u gebruiken? 4, 5 of 6?   ")  
elif chip_number == "2":
    while netlist_number != "7" and netlist_number != "8" and netlist_number != "9": 
        netlist_number = input("Welke netlist wilt u gebruiken? 7, 8 of 9?   ")

# Request user input: algorithm
while algorithm != "1" and algorithm != "2" and algorithm != "3":
    algorithm = input("Welk algoritme wilt u gebruiken? 1:Random 2:Greedy 3:A*   ")

# Perform desired algorithm: Random
if int(algorithm) == 1:
    rs.random_solve3D(test_grid)

# Perform desired algorithm : Greedy    
elif int(algorithm) == 2:
    reset = False
    while not reset:
        test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
        greedy = gr.LengthGreedy(test_grid)
        reset = greedy.run()

# Perform desired algorithm: A*       
elif int(algorithm) == 3:
    while annealing != "1" and annealing != "0":
        annealing = input("Wil je dat er simulated annealing wordt toegepast na het algoritme? 0:nee 1:ja   ")
    
    # Perform without simulated annealing
    if annealing == "0":
        reset = False
        while not reset:
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
            astar = ast.PopAstar(test_grid)
            reset = astar.run()
    
    # Perform with simulated annealing
    if annealing == "1":
        reset = False
        while not reset:
            test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)
            astar = ast.PopAstar(test_grid)
            reset = astar.run()

        simA = siman.SimulatedAnnealing(test_grid)
        cost = test_grid.cost_of_route()
        run = simA.run(cost)
        cost = run[0]
        pg.plot_graph(run[1])

  
# Print results and plot graph
print(f"De totale kost is: {cost}")
pg.plot_grid(test_grid, chip_number, netlist_number, cost, "Astar")