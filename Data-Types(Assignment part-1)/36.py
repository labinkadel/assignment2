dict1 = {}
n = int(input("Enter the number of dictionary: "))
for i in range(n):
    k = int(input("Enter key :"))
    v = int(input("Enter value :"))
    dict1.update({k: v})
    sum1 = sum(dict1.keys()) + sum(dict1.values())


print(dict1)
print(sum1)

