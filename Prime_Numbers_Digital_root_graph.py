#my files in this repo
from Digital_Root import drt
from Prime_Numbers import primes
#python module
from matplotlib import pyplot

m = int(input("Enter the Prime Number: "))
for i in primes(100):
    print(drt(str(i)))