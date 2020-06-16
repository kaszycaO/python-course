from functools import reduce

def get_size(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        yield sum([int(line.split()[-1]) for line in lines])

print("Calkowita liczba bajtow:", list(get_size("plik.txt"))[0])
