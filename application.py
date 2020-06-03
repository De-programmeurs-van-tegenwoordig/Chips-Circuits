import matplotlib.pyplot as plt
from models import *

def plot(x_coordinates, y_coordinates, x_max, y_max):
    plt.plot(x_coordinates, y_coordinates, 'ro')
    plt.axis([0, x_max + 1, 0, y_max + 1])
    plt.grid(linestyle='-', linewidth=0.5)
    plt.show()


def Read(file_name):
    """ Reads the file """
    with open (file_name) as f:
        lines = f.read().splitlines()
    for i in range (len(lines)):
        lines[i] = lines[i].split(',')
    return(lines)

if __name__ == '__main__':
    print_0 = Read("gates&netlists/chip_0/print_0.csv")
    netlist_1 = Read("gates&netlists/chip_0/netlist_1.csv")
    x = []
    y = []
    chips = []
    counter = 1
    for i in range (len(print_0)):
        if i == 0:
            continue
        chips.append(Chip(counter, int(print_0[i][1]), int(print_0[i][2])))
        x.append(int(print_0[i][1]))
        y.append(int(print_0[i][2]))
        counter += 1
    plt = plot(x,y,6,6)
    

    
