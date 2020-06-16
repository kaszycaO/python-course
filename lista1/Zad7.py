from random import randint
def create_list(size, length):
    my_list = []
    for i in range(0, size):
        my_string = ''
        for j in range(0, length):
            var = randint(0,2)
            if var == 0:
                my_string += 'a'
            elif var == 1:
                my_string += 'b'
            else:
                my_string += 'c'

        my_list.append(my_string)

    return my_list

def to_dictionary(user_string):
    my_dic = {}
    for i in range(len(user_string)):
        if user_string[i] != '*':
            my_dic[i] = user_string[i]
    return my_dic

def match(pattern, user_dic):
    correct = []
    for pat in pattern:
        if_good = True
        for j in user_dic:
             if user_dic[j] != pat[j]:
                 if_good = False
        if if_good:
            correct.append(pat)
    return correct


user_input = input("Podaj swoj kod: ")
pattern = create_list(3, len(user_input))

my_dic = to_dictionary(user_input)
print(match(pattern, my_dic))
