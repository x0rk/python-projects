from time import sleep
str1 = input("Enter a string: ")
str1 = str1.upper()
#str1 = 'COMPUTER'

for i in range(5):        
    index=1
    for i in str1:
        print(str1[:index])
        index+=1
        sleep(0.1)
    ind=len(str1)-1
    for i in str1:
        print(str1[:ind])
        ind-=1
        sleep(0.1)
        
