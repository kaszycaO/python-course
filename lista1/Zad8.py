def converter(roman_number):
    pattern = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last = 0
    converted_num = 0

    for rom in reversed(roman_number.upper()):
        var = pattern[rom]
        if var >= last:
            last = var
            converted_num += var
        else:
            converted_num -= var
    return converted_num


x = input("Podaj liczbe rzymska: ")
print(converter(x))
