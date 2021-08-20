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