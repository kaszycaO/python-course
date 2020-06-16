import sys

import os


def get_words_count(file_name):
    data = ""
    try:
        with open(file_name, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print("No such file!")

    return len(data.split())


def get_info(file_name):
    lines = 0
    max_length = 0
    try:
        with open(file_name, 'r') as f:
            for line in f:
                if len(line) > max_length:
                    max_length = len(line)
                lines += 1
    except FileNotFoundError:
        print("No such file!")

    file_stats = os.stat(file_name)
    words = get_words_count(file_name)

    print("liczba bajtow:", file_stats.st_size)
    print("liczba slow:", words)
    print("liczba linii:", lines)
    print("maksymalna dlugosc linii:", max_length)


def main():
    file_name = sys.argv[1]
    get_info(file_name)


main()
