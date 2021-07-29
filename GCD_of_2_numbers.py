get1 = int(input("Enter the 1st number:"))
get2 = int(input("Enter the 2nd number:"))

def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def lcm(n1, n2):
    g = gcd(n1,n2)
    l = (n1*n2)//g
    return l
    
print("G.C.D. is",gcd(get1,get2))
print("L.C.M. is",lcm(get1,get2))
