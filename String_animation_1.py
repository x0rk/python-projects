from os import system
from sys import platform
import time
inp = input("Enter a String: ")
lst = list(inp)
s = system('clear') if platform == 'linux' or platform == 'darwin' else system('cls')
t = int(time.time())
while True:
    for i in range(len(lst)):
        lst[i] = lst[i].upper()
        lst[i-1] = lst[i-1].lower()
        if lst[i] != ' ':
            for k in lst:
                print(k, end='')
            d = system('sleep 0.5')
            s = system('clear') if platform == 'linux' or platform == 'darwin' else system('cls')
    if int(time.time()) - t >= len(inp):
        break
    
