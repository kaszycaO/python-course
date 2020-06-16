def subsets(my_list):
    res = [[]]
    for el in my_list:
        res += list(map(lambda x: x + [el], res))
    return res
ex_list = [1, 2, 3]
print(subsets(ex_list))
