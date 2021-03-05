d = {}
n = int(input("Enter the number of elements in d: "))
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d.update({key:value})
print(d)
for i in d:
    print("key" + i + " " + "value" + d[i] )