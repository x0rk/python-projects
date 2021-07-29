num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))
tn = num
td = den

def sub(pnum,pden,num,den):
    n = (pnum*den)-(num*pden)
    d = pden*den
    return n,d

#finding the GCD of the numbers
while td:
    tn, td = td, tn % td

gcd = tn

print("\nThe simplest form of {}/{}".format(num,den),end="")
#dividing the numbers by their GCD
num //= gcd
den //= gcd
print(" is {}/{}".format(num,den))
sub = sub(6727,5395,13122,36292165)
print(sub)
