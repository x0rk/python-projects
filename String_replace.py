str1=input("Enter a String: ")
strplc=input("Enter the word to be replaced: ")
strplc2=input("Enter the replace word: ")

tmp=str1.split()

for i in range(len(tmp)):
    if tmp[i] == strplc:
        tmp[i] = strplc2

str2=""

for j in tmp:
    str2 += j + " "
        
print(str2)
