'''

1.方法是描述目标的行为，所以调用方式:目标.方法()
2.方法分为实例方法，类方法，静态方法
3.根据方法接收的第一个参数可以分辨出该方法是什么方法
4.方法是存储在类的__dict__方法所对应的字典中

'''

class Person:
    def shilifangfa(self): # 实例方法，第一参数接收的是对象
        print('这个是一个实例方法',self)

    @classmethod
    def leifangfa(cls): # 类方法，第一个参数接收的是类
        print("这是一个类方法",cls)

    @staticmethod
    def jingtaifangfa(): # 静态方法
        print('这是一个静态方法')

a = Person()
# print(a)
# a.shilifangfa()
# a.jingtaifangfa()
#
# Person.leifangfa()
#
# Person.jingtaifangfa()

print(a.__dict__)
print(Person.__dict__)

def eat():
    pass
a.age = eat
print(a.__dict__)















