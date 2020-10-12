# Exercise no 1

l = lambda a : a + 15
print(l(15))
l1 = lambda x, y : x * y
print(l1(10, 2))


#Exercise no 2

def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("x2 the number of 15 =", result(15))
result = func_compute(3)
print("x3 the number of 15 =", result(15))
result = func_compute(4)
print("x4 the number of 15 =", result(15))
result = func_compute(5)
print("x5 the number 15 =", result(15))

# Exercise no 3

scores = [('Mathematics', 85), ('Bahasa Indonesia', 77), ('ICT', 97), ('Mandarin', 82)]
print("Scores:")
print(scores)
scores.sort(key = lambda x: x[1])
print("Sorting the List of Scores:")
print(scores)

# Exercise no 4

import datetime
now = datetime.datetime.now()
print(now)
y = lambda x: x.year
m = lambda x: x.month
d = lambda x: x.day
t = lambda x: x.time()
print(y(now))
print(m(now))
print(d(now))
print(t(now))

# Exercise no 5

