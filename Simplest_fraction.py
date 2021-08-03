num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))
tn = num
td = den

#finding the GCD of the numbers
while td:
    tn, td = td, tn % td

gcd = tn

print("\nThe simplest form of {}/{}".format(num,den),end="")
#dividing the numbers by their GCD
num //= gcd
den //= gcd
print(" is {}/{}".format(num,den))

