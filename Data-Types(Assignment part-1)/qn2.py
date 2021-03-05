
# output: #Pyon  #PyPy #empty
s1 = input("Enter a string:")


def fun(s1):
    if len(s1) < 2:
            return "Empty string"
    else:
         return s1[0:2] + s1[-2:]

print(fun(s1))

