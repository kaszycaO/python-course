def prime_factors(n):
    result = []
    for i in range(2,n+1):
        counter = 0
        if n != 0:
            while n%i == 0 and n != 0 :
                counter+=1
                n = n/i
        else:
            break

        if counter != 0:
            result.append((i,counter))

    return result

print(prime_factors(720))
