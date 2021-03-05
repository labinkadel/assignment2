
dict1 = {}

a = int(input("Enter  number of elements in dict1: "))

for i in range(a):

    key = int(input("Enter key: "))

    value = int(input("Enter  value: "))

    dict1.update({key:value})

print(dict1)

def sortByValue():

    sortedValue = sorted(dict1.items(), key=lambda x: x[1])

    return sortedValue


print(dict(sortByValue()))