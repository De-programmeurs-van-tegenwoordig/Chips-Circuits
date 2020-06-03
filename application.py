def Read(file_name):
    with open (file_name) as f:
        lines = f.read()
    return(lines)

if __name__ == '__main__':
    print_0 = Read("gates&netlists/chip_0/print_0.csv")
    print(print_0)
