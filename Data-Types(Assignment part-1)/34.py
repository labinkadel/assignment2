dict2 = {}
dict1 = {}
dict3 = {}

n = int(input("Enter the number of elements in dict1: "))
p = int(input("Enter the number of elements in dict2: "))

for i in range(n):
    k = int(input("Enter the key: "))
    v = int(input("Enter the value: "))
    dict1.update({k:v})
for a in range(p):
    k1 = int(input("Enter the key: "))
    v2 = int(input("Enter the value: "))
    dict2.update({k1:v2})
for i in (dict1,dict2):
    dict3.update(i)

print(f"Merged dictionary :{dict3}")
