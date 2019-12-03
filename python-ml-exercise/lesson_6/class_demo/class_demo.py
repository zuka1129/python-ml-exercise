class Dog:
    name = 'baby'
    age = 1
    def __init__(self):
        self.name = 'baby'
        self.age = 1
        print('狗的构造方法')
    def run(self):
        print('baby run')
    def __like(self):
        print('dog like bone')
    def _phonate(self):
        print('wang wang')
    @classmethod
    def feed(cls):
        print('dog is pet of human')
    @staticmethod
    def test_static():
        print('你好啊')

#Dog.run(Dog)
# d = Dog()
# d.run()
# Dog.feed()
# Dog.test_static()
# d._phonate()
# # Dog._phonate()
# d._Dog__like()
# print(Dog.__dict__)
Dog.__init__(Dog)