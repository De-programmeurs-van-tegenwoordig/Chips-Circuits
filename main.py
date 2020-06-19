import matplotlib.pyplot as plt
from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve as rs
from code.algorithms import greedy as gr
from code.algorithms import astar as ast
import csv
import random

# Read multiple files
chip_number = float('inf')
netlist_number = float('inf')
algorithm = float('inf')
while chip_number != "0" and chip_number != "1" and chip_number != "2":
    chip_number = input("Welk chipnumber wilt u testen? 0, 1 of 2?    ")


if chip_number == "0":
    while netlist_number != "1" and netlist_number != "2" and netlist_number != "3": 
        netlist_number = input("Welke netlist wilt u gebruiken? 1, 2 of 3?   ")
elif chip_number == "1":
    while netlist_number != "4" and netlist_number != "5" and netlist_number != "6": 
        netlist_number = input("Welke netlist wilt u gebruiken? 4, 5 of 6?   ")  
elif chip_number == "2":
    while netlist_number != "7" and netlist_number != "8" and netlist_number != "9": 
        netlist_number = input("Welke netlist wilt u gebruiken? 7, 8 of 9?   ")

size = 17
test_grid = grid.Grid(f"data/chip_{chip_number}/print_{chip_number}.csv", f"data/chip_{chip_number}/netlist_{netlist_number}.csv", size)

output = open("chip2netlistLength.csv", "a")

while algorithm != "1" and algorithm != "2" and algorithm != "3":
    algorithm = input("Welk algoritme wilt u gebruiken? 1:Random 2:Greedy 3:A*   ")

if int(algorithm) == 1:
    rs.random_solve3D(test_grid)
elif int(algorithm) == 2:
    reset = False
    while not reset:
        greedy = gr.LengthGreedy(test_grid)
        reset = greedy.run()
elif int(algorithm) == 3:
    reset = False
    while not reset:
        astar = ast.PopAstar(test_grid)
        reset = astar.run()

cost = test_grid.cost_of_route()    
print(f"De totale kost is: {cost}")
pg.plot_grid(test_grid, chip_number, netlist_number, cost, "Astar")