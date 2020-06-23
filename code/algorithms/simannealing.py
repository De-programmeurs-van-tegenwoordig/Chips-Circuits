from code.classes import net
from code.classes import node
from code.classes import grid
from code.algorithms import astar as ast
from code.function import check_constraints
import copy
import numpy as np
import random

def acceptance_probability(cost, new_cost, temperature):
    """
    Calculate probability of accepting new cost
    """
    if new_cost < cost:
        return 1
    else:
        p = np.exp(- (new_cost - cost) / temperature)
        return p

class SimulatedAnnealing():
    def __init__(self, grid_file):
        self.grid_file = copy.deepcopy(grid_file)

    def run(self, cost, iterations):
        max_iteraties = iterations
        start_temp = 1000
        amount_of_redirects = 3

        all_cost = []
        lowest_cost = []
        all_temps = []
        all_cost.append(cost)
        lowest_cost.append(cost)
        
        for iteratie in range(max_iteraties):
            if iteratie % 10 == 0:
                print("nu bij iteratie:", iteratie)

            routes = self.grid_file.get_list_of_routes()

            redirect = {}
            current_temp = start_temp - (start_temp/max_iteraties) * iteratie
            all_temps.append(current_temp)
            backup_grid = copy.deepcopy(self.grid_file)

            for i in range(amount_of_redirects):
                redirect_route, route = random.choice(list(routes.items()))
                redirect_route = int(redirect_route)

                start = route[0].get_coordinates_from()
                end = route[-1].get_coordinates_to()

                redirect[redirect_route] = [start, end]

                self.grid_file.remove_route(redirect_route)
                self.grid_file.remove_crosses(redirect_route)

            self.grid_file.netlists = []

            for item in redirect:
                start = redirect[item][0]
                end = redirect[item][1]

                start_x = int(start[0])
                start_y = int(start[1])

                end_x = int(end[0])
                end_y = int(end[1])

                gate_a = self.grid_file.get_current_gate_number(start_x, start_y)
                gate_b = self.grid_file.get_current_gate_number(end_x, end_y)

                self.grid_file.netlists.append((gate_a, gate_b))
            
            # print("netlists die opnieuw gelegd gaan worden", self.grid_file.netlists)
            
            astar = ast.Astar(self.grid_file)
            reset = astar.run()

            if reset:
                new_cost = self.grid_file.cost_of_route()
                all_cost.append(new_cost)
                # print(f"oude cost: {cost} vs {new_cost} nieuw cost")

                probability = acceptance_probability(cost, new_cost, current_temp)
                print(probability)

                # random tussen 0 en 1
                if random.uniform(0, 1) < probability:
                    cost = new_cost
                else:
                    self.grid_file = backup_grid
            else:
                self.grid_file = backup_grid
            
            lowest_cost.append(cost)
        
        return cost, all_cost, self.grid_file, lowest_cost          

    def run2(self, cost):
        max_iteraties = 10
        start_temp = 1000
        amount_of_redirects = 3
        all_cost = []
        lowest_cost = []
        all_temps = []
        all_cost.append(cost)
        lowest_cost.append(cost)
        counter = 0
        
        for iteratie in range(max_iteraties):
            if iteratie % 10 == 0:
                print("nu bij iteratie:", iteratie)

            routes = self.grid_file.get_list_of_routes()
            amount_of_crosses = self.grid_file.get_list_of_crosses()
            redirect = {}
            current_temp = start_temp - (start_temp/max_iteraties) * iteratie
            all_temps.append(current_temp)
            backup_grid = copy.deepcopy(self.grid_file)

            for i in range(amount_of_redirects):
                if counter % 5 == 0:
                    redirect_route = max(amount_of_crosses, key=lambda key: amount_of_crosses[key])
                    route = routes[redirect_route]
                else:
                    redirect_route, route = random.choice(list(routes.items()))
        
                redirect_route = int(redirect_route)

                counter += 1

                start = route[0].get_coordinates_from()
                end = route[-1].get_coordinates_to()

                redirect[redirect_route] = [start, end]

                self.grid_file.remove_route(redirect_route)
                self.grid_file.remove_crosses(redirect_route)

            self.grid_file.netlists = []

            for item in redirect:
                start = redirect[item][0]
                end = redirect[item][1]

                start_x = int(start[0])
                start_y = int(start[1])

                end_x = int(end[0])
                end_y = int(end[1])

                gate_a = self.grid_file.get_current_gate_number(start_x, start_y)
                gate_b = self.grid_file.get_current_gate_number(end_x, end_y)

                self.grid_file.netlists.append((gate_a, gate_b))
            
            astar = ast.Astar(self.grid_file)
            reset = astar.run()

            if reset:
                new_cost = self.grid_file.cost_of_route()
                all_cost.append(new_cost)
                print(f"oude cost: {cost} vs {new_cost} nieuw cost")

                probability = acceptance_probability(cost, new_cost, current_temp)
                print(probability)

                # random tussen 0 en 1
                if random.uniform(0, 1) < probability:
                    cost = new_cost
                else:
                    self.grid_file = backup_grid
            else:
                self.grid_file = backup_grid
            
            lowest_cost.append(cost)
        
        return cost, all_cost, self.grid_file, lowest_cost  