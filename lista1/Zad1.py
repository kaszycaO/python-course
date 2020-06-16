def pascal_triangle(n):
    space = ' '
    #kolejne wyrazy
    number = 1

    for i in range(n+1):
        #odpowiednie ustawienie
        print(space * (n-i+1), end = '')

        for j in range(i+1):
            if i == 0 or j == 0:
                number == 1
            else:
                number = int(number*(i-j+1)/j)

            print(number,end = ' ')

        print('')

pascal_triangle(8)
