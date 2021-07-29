import os
#inp = input("Enter a String: ")
inp="kavinash"
lst = []

for i in inp:
    lst.append(i)

s = os.system("cls")
k = 0

while k != 1:
    ind = 0
    for j in range(len(lst)):
       lst[ind] = lst[ind].upper()
       print(inp[:ind],end="")
       print(lst[ind], end="")
       print(inp[ind+1:])
       ind += 1
       s = os.system('cls')
