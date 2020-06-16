import os

import sys

def change_size(directory):
    filenames = os.listdir(directory)
    for filename in filenames:
        curr_el = os.path.join(directory, filename)
        if os.path.isdir(curr_el):
            change_size(curr_el + "/")
        os.rename(curr_el, directory + filename.lower())

def main():
    dir_name = ""
    try:
        dir_name = sys.argv[1]
        if os.path.isdir(dir_name):
            if dir_name == "./":
                path = os.getcwd()
                path += '/'
                change_size(path)
            else:
                change_size(dir_name + "/")
        else:
            print("That's not directory!")

    except IndexError:
        print("Arguments are required!")
    except FileNotFoundError:
        print("There is no such file! ")

main()
