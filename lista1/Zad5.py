from math import factorial

def fraczero(n):

    silnia = factorial(n)

    str_silnia = str(silnia)
    counter = 0


    for i in range(len(str_silnia)-1, 0, -1):
        if str_silnia[i] == '0':
            counter+=1
        else:
            break

    return counter

print(fraczero(100))
