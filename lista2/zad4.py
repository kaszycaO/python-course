import sys

import os

import hashlib


def encoded_file(file):
    code = ""
    with open(file, 'r') as f:
        data = f.read()
        code = hashlib.md5(data.encode()).hexdigest()
    return code

def get_size(file):
    file_stats = os.stat(file)
    return file_stats.st_size



def repchecker(dir_name):
    list_of_files = []
    hash_list = []
    flag = 0
    print("------------------------------------")
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            list_of_files.append(os.path.join(root, name))
            hash_list.append(encoded_file(os.path.join(root, name)))

    length = len(hash_list)
    i = 0
    while i < length:
        flag = 0
        j = i + 1
        while j < length:
            if hash_list[i] == hash_list[j]:
                if get_size(list_of_files[i]) == get_size(list_of_files[j]):
                    if flag == 0:  
                        print(list_of_files[i])
                    print(list_of_files[j])
                    list_of_files.pop(j)
                    hash_list.pop(j)
                    flag = 1
                    length -= 1
                    j -= 1    # zapobiega utracie danych przy przesuwaniu indeksu
            j += 1
        if flag == 1:
            print("------------------------------------")
        i += 1


def main():
    dir_name = sys.argv[1]
    if os.path.isdir(dir_name):
        if dir_name == "./":
            path = os.getcwd()
            path += '/'
            repchecker(path)
        else:
            repchecker(dir_name + '/')
    else:
        print("That's not directory!")


main()
