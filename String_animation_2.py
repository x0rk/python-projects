import os
#inp = input("Enter a String: ")
inp="kavinash"
lst = []

for i in inp:
	lst.append(i)

s = os.system("clear")
c = 0
try:
	while c <= 100*len(inp):
		ind = 0
		c += 1
		for j in range(len(lst)):
			lst[ind] = lst[ind].upper()
			print(inp[:ind],end="")
			print(lst[ind], end="")
			print(inp[ind+1:])
			ind += 1
			s = os.system('clear')
except:
	print("Exit")
