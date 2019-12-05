# class MyException(BaseException):
#     pass
# raise MyException('这是个异常')

#手动抛出异常
# try:
#     raise RuntimeError('zheshigeyichang')
# except RuntimeError as e:
#     print(e)
#     print('捕获异常')

try:
    a = 1 / 0
    print(a)
# except RuntimeError as  e:
#     print('RuntimeError')
# except ZeroDivisionError as e:
#     print(e)
#     print('ZeroDivisionError')
except BaseException as e:
    print(e)
    print('BaseExcept')
except Exception as e:
    print(e)
finally:
    print("please input correct denominator")
    print(input())
    print('结束')

# class MyException(BaseException):
#     pass
# try:
#     raise MyException('this is my defined exception')
# except MyException as e:
#     print(e)

