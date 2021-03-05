def fib(count):
    lst = [0, 1]
    any(map(lambda _: lst.append(sum(lst[-2:])), range(2, count)))
    return lst[:count]

print(fib(int(input())))

