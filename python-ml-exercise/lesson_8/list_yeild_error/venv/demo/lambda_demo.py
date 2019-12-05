#匿名函数lambda
# a = [lambda x: x+1 for x in [1,2,3,4]]
# print(a)
# print(list(a))
# a = lambda x : x + 1
#
# print(a(0))

# a = [lambda x : x+1 for x in [1,2,3,4]]
# for i in a:
#     print(i)

#map函数
a = map(lambda x : x + 1, [1, 2, 3, 4])
# print(a)
# print(list(a))
# print(type(a))

#reduce函数，相当于是做累加
from functools import reduce
b = reduce(lambda x, y : x + y, [1, 2, 3, 4, 5], 10)
# print(b)

#filter函数相当于做过滤
c = filter(lambda x : x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8])
# print(list(c))
# print(type(c))
# print(c)
