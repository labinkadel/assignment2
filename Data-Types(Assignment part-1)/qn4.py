a = 'abc'
b = 'xyz'
def fun(a,b):

    p = b[:-1] + a[-1:]
    q = a[0:2] + b[-1:]
    return p + ' ' + q

print(fun('abc','xyz'))