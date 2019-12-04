#本模块测试参数传递问题
def my_func(a, b, c=1, d=2, *args, **kwargs):
    print(a,b)
    print(c,d)
    print(args)
    print(kwargs)

#my_func(1,2,3,4,7,8, e=5, f=6)

###  参数列表*以后的所有参数必须写名字如：name = value的形式传入
# 命名关键字参数是必须参数，如果不需要他是必须参数，那么可以给一个默认值
def my_func1(a, b, *, c, d):
    print(a,b)
    print(c,d)

#my_func1(1, 2, c=3, d=4)

# 传参的其他方法
def my_func2(a,b,c):
    print(a,b,c)
args = (1, 2, 3)
my_func2(*args)
print(type(args))
n = [1, 2, 3]
my_func2(*n)
print(type(n))

kw = {'a':1, 'b':2, 'c':3}
my_func2(*kw)
my_func2(**kw)




