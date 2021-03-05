s1 = str(input("Enter the list :"))
def fun(s1):
    r = s1.split(',')
    return sorted(r)
print(fun(s1))