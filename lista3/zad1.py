def transposition(my_list):
    return[" ".join(el) for el in [[row[i] for row in [j.split(" ") for j in my_list]] for i in range(len(my_list))]]
print(transposition(["1.1 2.2 3.3", "5.5 6.6 7.7", "8.8 9.9 0.0"]))
