def Read(file_name):
    with open (file_name) as f:
        lines = f.read().splitlines()
    for i in range (len(lines)):
        lines[i] = lines[i].split(',')
    return(lines)

if __name__ == '__main__':
    print_0 = Read("gates&netlists/chip_0/print_0.csv")
    netlist_1 = Read("gates&netlists/chip_0/netlist_1.csv")
    
    
