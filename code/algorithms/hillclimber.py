from code.function import plot_grid as pg
from code.classes import gate
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
from code.algorithms import greedy as gr
import csv

class HillClimber():
    def __init__(self, chip_number, netlistfile, size):
        self.chip_number = chip_number
        self.netlistfile = netlistfile
        self.size = size
        climbing = self.Climb()

    def Climb(self):
        best_net_score = float("inf")
        counter = 0
        reset = False

        while counter < 50:
            while not reset:
                test_grid = grid.Grid(f"data/chip_{self.chip_number}/print_{self.chip_number}.csv", f"data/chip_{self.chip_number}/{self.netlistfile}", self.size)
                greedy = gr.Greedy(test_grid)
                netlist = test_grid.get_netlists()
                reset = greedy.run(10)
            
            new_score = test_grid.cost_of_route()
            if new_score > best_net_score:
                counter += 1
            else:
                best_netlist = netlist
                counter = 0
                best_net_score = new_score
                print(best_net_score)
            counter += 1
            reset = False

        return best_netlist, best_net_score
