list1 = input("Enter a list :")
sp_ls1 = list1.split()
for i in range(0,len(sp_ls1)):
    sp_ls1[i] = int(sp_ls1[i])

if len(sp_ls1) == 0:
    print("True")

else:
    print("False")

