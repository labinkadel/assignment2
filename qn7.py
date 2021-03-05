str1 = input("Enter a string: ")

l = 0

u = 0

for var in str1:

    if var.islower():

        l = l + 1

    elif var.isupper():

        u = u + 1

print(u)

print(l)
