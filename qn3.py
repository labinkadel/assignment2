from functools import reduce

list1= input("Enter a list: ")

l_s = list1.split()

for i in range(len(l_s)):

       l_s[i] = int(l_s[i])

print(l_s)


mul = lambda a, b: a*b

res = reduce(mul, l_s)


print(f"Product is : {res}")