# from urllib.request import urljoin
#
# url = urljoin('https://tieba.baidu.com/f?kw=%E6%96%87%E5%AD%A6',
#               '//tieba.baidu.com/f?kw=%E6%96%87%E5%AD%A6&ie=utf-8&pn=50')
# print(url)
class People():
    name = 'human'
    age = 20

    def __init__(self, name, age):
        print('执行构造方法-----')
        self.name = name
        self.age = age

    def eat(self):
        print(self)
        print(People.name)
        print(People.age)
        print(self.age)
        print(self.name)
        print('people eat')
        People.old()
    @classmethod
    def old(clz):
        #print('people old')
        print('classmethod---------')
        print(clz)
        print(clz.name)
        print(People.name)

    @staticmethod
    def young():
        print('staticmethod-----------')
p = People('child', 5)
# print(p.age)
# print(p.name)
# print(People.name)
# print(People.age)
#p.eat()
#People.eat(People('zhou',20))
#p.eat()
#People.eat(p)
# People.old()
# People.young()
#p.eat()
People.old()