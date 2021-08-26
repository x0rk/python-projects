#my files in this repo
from Digital_Root import drt, drt2
from Prime_Numbers import primes
#python module
import matplotlib.pyplot as plt

m = int(input("Enter the Prime Number: "))
p = primes(m)
d = [drt2(x) for x in primes(m)]
#g = { p[i]:d[i] for i in range(len(p)) }
#print(p,'\n',d)
#plt.plot(p,d)

plt.title("Prime Distribution")
plt.xlabel("Prime Numbers")
plt.ylabel("Digital Roots of Prime Numbers")
plt.scatter (p, d, alpha = 0.5)
plt.show()
