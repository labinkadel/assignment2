import operator

str = input("Enter a string: ")

d = {}
for x in str:
    if x in d.keys():
        d[x]+= 1
    else:
       d[x] = 1

print(dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)))
