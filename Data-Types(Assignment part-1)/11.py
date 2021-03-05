import operator
str = input("Enter the sentence: ")
d = {}
for x in str: #takes each character of string and use it
   if x in d.keys():
       d[x]+=1

   else:
       d[x] = 1


print(dict(sorted(d.items())))
