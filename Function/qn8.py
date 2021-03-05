list1 = input("Enter a list: ")


sp_list1 = list1.split()

s1 = sorted(set(sp_list1))



for i in range(0, len(s1)):


    s1[i] = int(s1[i])


print(s1)