start = int(input("Enter the start: "))
stop = int(input("Enter the stop: "))
step = int(input("Enter the step size: "))
t = input("Enter list of tuple: ")
a = tuple(int(x) for x in t.split())
t_slice =a[start:stop:step]
print(t_slice)