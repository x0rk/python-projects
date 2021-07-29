num = int(input("Enter a number: "))

temp = num
div = 0
fac = []

while div != 1:
    for i in range(3, temp, 2):
        if num % 2 == 0:
            div = num = num / 2
            fac.append(2)
            break
        if num % i == 0:
            div = num = num / i
            fac.append(i)
            break
        else:
            continue
print(fac)
