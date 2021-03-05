str1 = input("Enter a sentence: ")
def fun(str1):
    f_not= str1.find('not')
    f_poor = str1.find('poor')
    if(f_poor>f_not):
        str1 = str1.replace(str1[f_not:(f_poor + 4)], 'good')
    return str1
print(fun(str1))