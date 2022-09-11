'''

1.继承于object的是新式类，类名.__bases__
2.这个区别存在于Python2和Python3中

'''

# class Person(object):
#     def __init__(self):
#         self.__age = 21
#
#     def get_age(self):
#         print("_____,get")
#         return self.__age
#
#     def set_age(self,value):
#         print("___,set")
#         self.__age = value
#
#     age = property(get_age,set_age) # 两个方法关联,类似于装饰器
#
# # print(Person.__bases__)
# p = Person()
# print(p.age)
#
# p.age = 20
# print(p.age)
#
# print(p.__dict__)
# print(Person.__dict__)

class Person(object):
    def __init__(self):
        self.__age = 21

    @property
    def get_age(self):
        print("get_age")
        return self.__age

    @get_age.setter
    def set_age(self,value):
        print("set_age")
        self.__age = value

p = Person()
print(p.get_age)

p.set_age = 20
print(p.get_age)


