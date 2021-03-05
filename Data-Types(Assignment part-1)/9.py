s1 = str(input("Enter a string :"))
def fun(s1):
    s2 = s1[-1] + s1[1:-1] + s1[0]
    return s2
print(fun(s1))