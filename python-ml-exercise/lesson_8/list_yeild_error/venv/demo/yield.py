def demp_yeild():
    print('im come')
    for i in range(4):
        print('yeild 前一行')
        yield i
        print('yeild 后一行')
t = demp_yeild()
# for i in t:
#     print(i)
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())

def yield_demo3():
    a = 10
    b = 20
    c = 30
    for x in range(3):
        yield a
        print("生成a之后")
        yield b
        print("生成b之后")
        yield c
        print("生成c之后")

y = yield_demo3()

print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())