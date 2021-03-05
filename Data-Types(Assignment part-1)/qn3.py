def fun(s1):
    x = s1[0]

    s1 = s1.replace(x ,'$')

    s1 = x + s1[1:]

    return s1


print(fun('restart'))