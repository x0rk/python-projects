n = int(input("Enter the Numerator: "))
d = int(input("Enter the denominator: "))
tn = n
td = d
numlst=[]
count = 0
print("\nThe Fraction {}/{} can be represented in Sumerian Fraction System as\n".format(n,d))

if d == 60:
    print("{}/{}".format(n,d))
else:
    while n != 0:
        n *= 60
        q = n // d
        numlst.append(q)
        n = r = n % d
        count += 1
        if count > 8:
            break
for i in range(0,len(numlst)):
    if i == (len(numlst)-1):
        print("{}/60^{}".format(numlst[i],i+1), end = " ")
    else:
        print("{}/60^{} +".format(numlst[i],i+1), end = " ")
print('\n')
