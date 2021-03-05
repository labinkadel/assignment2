dict2={}
dict1 = {}
dict3={}
dict4={}
n = int(input("Enter the number of dictionary in dict1: "))
p = int(input("Enter the number of dictionary in dict2: "))
q = int(input("Enter the number of dictionary in dict3: "))
for i in range(n):
    k = int(input("Enter the key: "))
    v = int(input("Enter the value: "))
    dict1.update({k:v})
for a in range(p):
    k1 = int(input("Enter the key: "))
    v2 = int(input("Enter the val  ue: "))
    dict2.update({k1:v2})
for b in range(q):
    k3 = int(input("Enter the key: "))
    v3 = int(input("Enter the value: "))
    dict3.update({k3:v3})
for i in (dict1,dict2,dict3):
    dict4.update(i)

print(f"Dict1 : {dict1}")
print(f"Dict2 : {dict2}")
print(f"Dict2 : {dict3}")
print(f"Merged dict : {dict4}")

