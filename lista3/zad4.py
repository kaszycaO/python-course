def quick_sort(my_list):
    if len(my_list) < 2:
        return my_list
    pivot = my_list[0]
    list_L = (list(filter(lambda x : x < pivot, my_list[1:])))
    list_P = (list(filter(lambda x : x >= pivot, my_list[1:])))
    return quick_sort(list_L) + [pivot] + quick_sort(list_P)





ex_list = [4, 3, 9, 8, 1, 12]
print(ex_list)
print(quick_sort(ex_list))
