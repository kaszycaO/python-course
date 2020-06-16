from math import *

x_size, y_size = 81, 27

def init_my_tab():
    return [[" "for i in range(y_size)] for j in range(x_size)]

def add_coordinate(my_tab, begin):
    for i in range(x_size):
        my_tab[i][y_size//2] = "-"

        if(i < y_size and begin < 0):
            my_tab[x_size//2][i] = "|"

    return my_tab

def get_values(user_function, begin, end):

    function_var = {}
    counter = (end - begin) / x_size
    helper = 0

    while end > begin:
        try:
            var = eval(user_function.replace('x', str(begin)))
            function_var[helper] = var
            begin += counter
        except ZeroDivisionError or ValueError:
            begin += counter

        helper+=1
        if(counter >= x_size):
            break
    return function_var


def fill_tab(my_tab, values):
    scaler = ((y_size)//2) / max(max(values.values()),abs(min(values.values())))
    for i in values:
        values[i] = -(round(values[i]*scaler) - y_size//2)

    for i in values:
        my_tab[i][values[i]] = "*"
    return my_tab

def draw_my_tab(my_tab):
    print("\n")
    for i in range(y_size):
        for j in range(x_size):
            print(my_tab[j][i], end="")
        print("")



function = input("Podaj f(x): ")
a = input("Podaj początek przedziału a: ")
b = input("Podaj koniec przedziału b: ")
try:
    begin = eval(a)
    end = eval(b)
    my_var = get_values(function ,begin ,end)
    my_tab = init_my_tab()
    my_tab = add_coordinate(my_tab, begin)
    my_tab = fill_tab(my_tab, my_var)
    draw_my_tab(my_tab)

except Exception as e:
    print("Bledne dane!")
