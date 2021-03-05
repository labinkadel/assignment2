ls1 = ['abc', 'xyz','aba','1221']

def fun(ls1):
    cnt = 0
    for i in ls1:
         if len(i) > 1 and i[0] == i[-1]:
             cnt += 1
             return cnt


print(fun(ls1))