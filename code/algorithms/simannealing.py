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
    """
    Simulated annealing is used to optimize the chip
    """
    def __init__(self, grid_file):
        self.grid_file = copy.deepcopy(grid_file)       

    def run(self, cost, iterations):
        """
        Deletes a few lines and places them again using A*
        """
        max_iterations = iterations
        start_temp = 1000

        amount_of_netlists = len(self.grid_file.get_list_of_routes())
        amount_of_redirects = amount_of_netlists // 10

        all_cost = []
        lowest_cost = []
        all_cost.append(cost)
        lowest_cost.append(cost)

        # Run simulated annealing for every iteration
        for iteration in range(max_iterations):
            backup_grid = copy.deepcopy(self.grid_file)
            counter = 0

            # Progression notifier
            if iteration % 10 == 0:
                print("Nu bij iteratie:", iteration)

            # Get all routes and amount of crosses
            routes = self.grid_file.get_list_of_routes()
            amount_of_crosses = self.grid_file.get_list_of_crosses()
            redirect = {}
            
            # Remove x amount of routes
            for i in range(amount_of_redirects):
                if counter % 5 == 0:
                    redirect_route = max(amount_of_crosses, key=lambda key: amount_of_crosses[key])
                    route = routes[redirect_route]
                else:
                    redirect_route, route = random.choice(list(routes.items()))
        
                redirect_route = int(redirect_route)
                start = route[0].get_coordinates_from()
                end = route[-1].get_coordinates_to()
    
                redirect[redirect_route] = [start, end]
                self.grid_file.remove_route(redirect_route)
                self.grid_file.remove_crosses(redirect_route)

                counter += 1

            self.grid_file.empty_netlists()

            # Formulate the removed routes into a netlist for Astar
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

            # Check if Astar was successful, if yes then calculate probability to accept new state
            # If no then return to state before iteration
            if reset:
                new_cost = self.grid_file.cost_of_route()
                all_cost.append(new_cost)

                current_temp = start_temp - (start_temp/max_iterations) * iteration
                probability = acceptance_probability(cost, new_cost, current_temp)

                # Calculates if new state should be accepted
                if random.uniform(0, 1) < probability:
                    cost = new_cost
                else:
                    self.grid_file = backup_grid
            else:
                self.grid_file = backup_grid
            
            lowest_cost.append(cost)
        
        return cost, all_cost, lowest_cost, self.grid_file  