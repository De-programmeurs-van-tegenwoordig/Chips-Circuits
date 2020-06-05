import csv
from .chip import Chip

def Read(file_name):
    """ Reads the file """
    with open(file_name, 'r') as input_file:
        reader = csv.DictReader(input_file)
        chips={}

        counter = 1
        for row in reader:
            # print(row)
            new_chip = Chip(counter, row['x'], row['y'])
            chips[int(counter)] = new_chip
            counter += 1
    return chips