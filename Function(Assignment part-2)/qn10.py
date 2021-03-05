list1 = input("Enter a list: ")


l_s = list1.split()

for i in range(len(l_s)):

   l_s[i] = int(l_s[i])

print(l_s)

                                     # use of lambda and filter)

even = lambda x:x % 2 == 0


res = list(filter(even,l_s))


print(f"Even no from the list are : {res} ")