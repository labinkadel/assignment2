a = []
string = ''
n = int(input("Enter the no of ele: "))
for i in range(n):
    a.append(input("Enter element: "))
a = tuple(a)
# print(type(a))
string = str(a)
# print(type(string))
print(string)

#<or>
# t = input("Enter list of tuple: ")
# a = tuple(str(x) for x in t.split())
# c =str(a)
# str = ''
# for item in a:
#     str = str + c
#     break


