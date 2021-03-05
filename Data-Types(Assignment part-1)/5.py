s1 = str(input('Enter the string:'))
def fun(s1):
    if len(s1)<3:
        return s1
    elif (s1[-3:]!='ing'):
       r = s1 + 'ing'
       return r
    else:
        r = s1 + 'ly'
        return r


print(fun(s1))