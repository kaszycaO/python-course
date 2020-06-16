from random import randint

def get_random(n):
    randoms = []

    for i in range(20):
        randoms.append(randint(0, 100))

    return randoms

def num_of_even(randoms):
    counter = 0
    for i in randoms:
        if i%2 == 0:
            counter+=1

    return counter

def find_value(randoms, type):
    new_randoms = list(set(randoms))
    new_randoms.sort()
    if type == "min":
        value = new_randoms[1]
    elif type == "max":
        value = new_randoms[len(new_randoms)-2]
    return value


my_randoms = get_random(20)

print("Wylosowana lista: ", my_randoms)
my_randoms.sort()
print("Posortowana lista: ", my_randoms)

print("Najmniejsza wartosc: ", my_randoms[0])
print("Najwieksza wartosc: ", my_randoms[len(my_randoms)-1])

print("Druga najmniejsza wartosc: ", find_value(my_randoms, "min"))
print("Druga najwieksza wartosc: ", find_value(my_randoms,"max"))

average = sum(my_randoms)/len(my_randoms)
print("Srednia to: ", average)
print("Liczba liczb parzystych: ", num_of_even(my_randoms))
