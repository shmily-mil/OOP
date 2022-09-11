
class Person:
    num = 10 # 类属性
    age = 21
    height = 171

    def shilifangfa(self):
        print(self)
        print(a.age)
        print(a.num)

    @classmethod
    def leifangfa(cls):
        print(cls)
        print(Person.age)
        print(cls.age)

    @staticmethod # 用不到class和instance
    def jingtaifangfa():
        print()


a = Person()
a.age = 20 # 实例属性
a.height = 170

# # 类属性
# print(Person.num)
# print(a.num) # 涉及到属性的访问顺序原则
#
# # 实例属性
# print(a.age)

# a.shilifangfa()

a.leifangfa()