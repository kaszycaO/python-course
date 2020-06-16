from math import *

def calculator(input):

    try:
        output = eval(input)
    except Exception as e:
        print("Bledne dane!")
        return

    print(output)

print("Kalkulator: ")
print("Nacisnij 'q' zeby zakonczyc")
while True:
    x = input()
    if x == 'q':
        break
    else:
        calculator(x)
