def sub(pnum,pden,num,den):
    n = (pnum*den)-(num*pden)
    d = pden*den
    return n,d

def neargrt(num, den):
    while den % num:
        den += 1
    den //= num
    num //= num
    return num,den

n = int(input("Enter the Numerator: "))
d = int(input("Enter the Denominator: "))
tn = n
td = d
numlst = []
denlst = []

print("\nThe Fraction {}/{} can be represented in Egyptian Fraction System as\n".format(n,d))

if n == 1:
    print("{}/{}".format(n,d))
else:
    while n != 1:
        n1,d1 = neargrt(n,d)
        n2,d2 = sub(n,d,n1,d1)
        numlst.append(n1)
        denlst.append(d1)
        n, d = n2,d2
        if d % n == 0:
            d //= n
            n //= n
            numlst.append(n)
            denlst.append(d)
for i in range(0,len(numlst)):
    if i == (len(numlst)-1):
        print("{}/{}".format(numlst[i],denlst[i]), end = " ")
    else:
        print("{}/{} +".format(numlst[i],denlst[i]), end = " ")
print('\n')
