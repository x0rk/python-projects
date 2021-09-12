# Enter the coefficients of the linear indeterminate equation in the following format
# ax + by + c = 0

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
n = int(input("Enter the number of solutions needed: "))

soln = []
x = 0
while n > 0:
	y = -(a*x+c)/b
	if y - int(y) == 0:
			print("\nValue of x: ",x)
			print("Value of y: ",int(y))
			n -= 1
	x += 1
