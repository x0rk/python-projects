num = int(input("Enter a number: "))

temp = num
div = 0
factors = []

while div != 1:
    for i in range(3, temp+1, 2):
        if num % 2 == 0:
            div = num = num / 2
            factors.append(2)
            break
        elif num % i == 0:
            div = num = num / i
            factors.append(i)
            break
        else:
            continue
print(factors)
