tup_inp_values = input("Enter  sequence seperated by comma: ")

lst_values = tup_inp_values.split(',')

tup_no = tuple(lst_values)


print(tup_no)

lst = list(tup_no)

for i in range(len(lst)):

    lst[i] = int(lst[i])

lst.sort(key=lambda x: lst)

print(tuple(sorted(lst)))
