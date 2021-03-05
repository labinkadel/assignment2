array1 = input("Enter  first array: ")
sp_list1 = array1.split()

for i in range(0, len(sp_list1)):
    sp_list1[i] = int(sp_list1[i])

print(sp_list1)
array2 = input("Enter second array: ")
sp_list2 = array2.split()
for i in range(0, len(sp_list2)):
    sp_list2[i] = int(sp_list2[i])
print(sp_list2)

result = list(set(filter(lambda x: x in array1, array2)))
print(f"Inserted array: {result}")


