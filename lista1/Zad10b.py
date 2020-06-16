from math import pi
from math import *

plot_x_size, plot_y_size = 101, 31

def draw_plot(plot):
    print("")
    for i in range(plot_y_size):
        for j in range(plot_x_size):
            print(plot[j][i], end="")
        print("")

def init_plot():
    return [[" " for i in range(plot_y_size)] for j in range(plot_x_size)]

def add_axises(plot):
    for i in range(plot_x_size):
        plot[i][plot_y_size//2] = "-"

    for i in range(plot_y_size):
        plot[plot_x_size//2][i] = "|"

    return plot

def fill_plot(plot, func, a, b):
    a, b = eval(a), eval(b)
    values = {}
    step = (b-a)/plot_x_size
    index = 0

    while a<b:
        try:
            values[index] = eval(func.replace('x', str(a)))
            a += step
        except ZeroDivisionError or ValueError:
            a += step

        index +=1
        if(index >= plot_x_size):
            break

    scaler = ((plot_y_size-1)//2) / max(max(values.values()),abs(min(values.values())))
    for i in values:
        values[i] = -(round(values[i]*scaler) - plot_y_size//2)

    for i in values:
        plot[i][values[i]] = "*"

fx = input('Podaj funkcje f(x) = ')
a = input('Podaj początek przedziału a = ')
b = input('Podaj koniec przedziału b = ')

try:
    plot = init_plot()
    fill_plot(plot,fx,a,b)
    add_axises(plot)

    draw_plot(plot)
except:
    print("Zle dane!")
