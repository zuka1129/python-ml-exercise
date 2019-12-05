lists = [2,4,3,6,7,4,89]
a = [x for x in lists if x > 10]
# print(a)

#集合推导式
sets = [1,3,46, 24, 37]
b = {x for x in sets if x > 10}
# print(b)

#字典推导式
c = {x : y for x, y in {'a':1, 'b':'c', 'c':3}.items()}
# print(c)

d = {'a':1, 'b':'c', 'c':3}
for i in {'a':1, 'b':'c', 'c':3}:
    print(type(i))
print(type(d.items()))
print(d.items())

