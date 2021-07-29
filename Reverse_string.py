def reverse(s):
    r = s[::-1]
    return r

str1 = input("Enter a string: ")
print("The Mirror image of ", str1, " is ", reverse(str1))
