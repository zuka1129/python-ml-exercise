import time
def demo1(my_func):
    def wapper(args):
        print(args)
        my_func()
    return wapper

@demo1
def my_func(name='zhihao'):
    print('this is my print')

def max_runtime(timeout):
    def test_dec(my_func):
        def wapper():
            strat_time = time.time()
            my_func()
            end_time = time.time()
            use_time = end_time - strat_time
            #print(use_time)
            if use_time > timeout:
                print('函数运行超时')
            else:
                print(use_time)
        return wapper
    return test_dec

@max_runtime(timeout=1)
def my_fun2():
    time.sleep(2)
    print('this is myfunc。。。。')
    return 1
#my_func('lisi')
#my_fun2()

def test_dec1(my_func):
    def aaa(*args):
        print('111')
        #print('name:' + name, 'age:' + str(age))
        my_func(*args)
        print(args)
    return aaa

@test_dec1
def my_fun3(name, age):
    print('name:' + name, 'age:' + str(age))

my_fun3('xiaomage', 1)