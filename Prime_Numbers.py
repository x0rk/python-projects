#x = int(input("Enter the number to get all the prime numbers lesser than the number: "))

def primes(n):
    p = []
    s = 0
    for i in range(2, n+1):
        pt = []
        for z in p:
            if z < n**0.5 + 1:
                pt.append(z)
        for k in pt:
            if i%k == 0:
                s = 1
        if (i not in p) and (s != 1):
            p.append(i)
        s = 0    
    return p

#print('There are {} Prime numbers <= {}'.format(len(primes(x)),x),'\n',primes(x))
