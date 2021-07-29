def str_len():
    str1 = input("Enter a string: ")
    #str1 = "kavinash"
    result = str1.index(str1[-1]) + 1
    return result

print("Length of the string is ",str_len())
