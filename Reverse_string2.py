def reverse(s):
    str1 = "" 
    for i in s: 
        str1 = i + str1
    return str1

string = input("Enter a string: ")
print("The reversed string is",reverse(string))
