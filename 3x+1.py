n = int(input("Enter a number: "))
c = 0
n1 = n
while n != 1:
    if n%2 == 0:
        n/=2
    else:
        n=3*n + 1
    print('\n'+n+'\n')
    g = n1 if n1 > n and else n
    c+=1
print("Number of Loops: ",c)
print("The greatest number attained is {}".format(g))