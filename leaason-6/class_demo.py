class Dog:
    name = 'baby'
    age = 1
    def __init__(self):
        self.name = 'baby'
        self.age = 1
    def run(self):
        print('baby run')
Dog.run(Dog)
d = Dog()
d.run()
