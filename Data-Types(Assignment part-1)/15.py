def mid_string(str1, str2):
    length = int(len(str1)/2)
    print(str1[:length] + str2 + str1[length:])
print(mid_string(input("string1: "),input("string2: ")))




