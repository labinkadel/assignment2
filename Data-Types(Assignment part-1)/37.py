mul=1
dict1 = {}
n = int(input("Enter the number of dictionary: "))
for i in range(n):
    k = int(input("Enter the key: "))
    v = int(input("Enter the value: "))
    dict1.update({k:v})
for i in dict1.values():
    mul=mul*i
print(dict1)
print(mul)




