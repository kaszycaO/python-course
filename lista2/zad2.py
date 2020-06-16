import sys


array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def decode(input, output):

    data = ""
    bin_data = ""
    result = ""
    padding = 0

    try:
        with open(input, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print("No such file!")

    for l in data.rstrip('\n'):
        if l == '=':
            padding += 1
        elif l == '\n':
            bin_data += "00001010"
            continue
        else:
            binary = bin(array.index(l)).lstrip('0b')
            for i in range(6 -len(binary)):
                bin_data += '0'
            bin_data += binary

    if padding == 1:
        bin_data[:len(bin_data)-4]
    elif padding == 2:
        bin_data[:len(bin_data)-4]


    i = 0
    while i < len(bin_data):
        letter = int(bin_data[i: i+8], 2)
        result += chr(letter)
        i += 8

    with open(output, 'w') as f:
        data = f.write(result)



def encode(input, output):
    data = ""
    bin_data = ""
    result = ""
    padding = 0

    try:
        with open(input, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print("No such file!")

    for i in data:
        conv = format(ord(i), 'b')
        for i in range(8 - len(conv)):
            bin_data += '0'
        bin_data += conv

    if len(bin_data) % 6 == 2:
        bin_data += "0000"
        padding = 2
    elif len(bin_data) % 6 == 4:
        bin_data += "00"
        padding = 4


    i = 0
    while i < len(bin_data):
        letter = int(bin_data[i: i+6], 2)
        result += array[letter]
        i += 6

    if(padding == 2):
        result += '='
    elif(padding == 4):
        result += '=='

    with open(output, 'w') as f:
        data = f.write(result)



def main():
     try:
        if sys.argv[1] == "--decode":
            decode(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "--encode":
            encode(sys.argv[2], sys.argv[3])
        else:
            print("There is no such option!")
     except IndexError:
         print("Arguments are required!")

main()
