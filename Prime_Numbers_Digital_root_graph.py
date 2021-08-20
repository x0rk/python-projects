#my files in this repo
from Digital_Root import drt
from Prime_Numbers import primes
#python module

m = int(input("Enter the Prime Number: "))
for i in primes(100):
    print(drt(str(i)))