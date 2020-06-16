def primes(n):
    my_primes = []
    for i in range(2,n+1):
        prime = True
        for j in range(2,i):
            if i%j == 0 and i != j:
                prime = False
                break
        if prime:
            my_primes.append(i)
    return my_primes
