import matplotlib.pyplot as plt

def plot(x_coordinates, y_coordinates, x_max, y_max):
    plt.plot(x_coordinates, y_coordinates, 'ro')
    plt.axis([0, x_max + 1, 0, y_max + 1])
    plt.show()


def Read(file_name):
    with open (file_name) as f:
        lines = f.read()
    return(lines)

if __name__ == '__main__':
    print_0 = Read("gates&netlists/chip_0/print_0.csv")
    print(print_0)
