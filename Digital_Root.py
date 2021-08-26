#n = input("Enter an integer to find its Digital Root: ")
#n = '256'

def drt(x):
    for k in range(len(x)):
        s = 0
        for i in x:
            s += int(i)
        x = str(s)
    return x

#print(drt(n))

def drt2(x):
    k = 0
    while x:
        r = x % 10 
        x //= 10
        k += r
    return k if len(str(k)) == 1 else drt2(k)

#print(drt2(n))