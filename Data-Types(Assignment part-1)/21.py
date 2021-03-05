ls1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def fun(data):
    return data[1]
print(sorted(ls1,key=fun))