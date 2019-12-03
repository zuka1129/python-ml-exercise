from leaason_6.class_demo import Dog

class HaShiQi(Dog):
    def run(self):
        print('哈士奇跑')
h = HaShiQi()
# h.run()
# print(h.name)
# print(h.age)
# h.test_static()
# h.feed()
# h._phonate()
# h._Dog__like()

print(HaShiQi.mro())
