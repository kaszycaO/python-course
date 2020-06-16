def rem_same(bad_list):
    helper = set(bad_list)
    return list(helper)


lista = ["o","o",2,3,4,555,555,3,3,3,2]
print(rem_same(lista))
