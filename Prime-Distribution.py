from Prime_Numbers import *
#import matplotlib.pyplot as plt

n = int(input("Enter the number to get all the prime numbers lesser than the number: "))

def primeDiff(n):
    f = primes(n)
    d = []
    for i in range(1, len(f)):
        d.append(f[i] - f[i-1])
    return d
'''
g = primes(n)
g.pop()
plt.title("Prime Distribution")
plt.xlabel("Prime Numbers")
plt.ylabel("Digital Roots of Prime Numbers")
plt.scatter (g, primeDiff(n), alpha = 0.5)
plt.show()
'''

print("The maximum difference between Prime numbers so far is {}\nAnd the numbers are {}".format(max(primeDiff(n)),primeDiff(n)))
