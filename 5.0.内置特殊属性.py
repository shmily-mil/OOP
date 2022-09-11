'''

类属性:
1.__dict__:类属性
2.__bases__:类的所有父类构成元组
3.__doc__:类的文档字符串
4.__name__:类名
5.__module__:类定义所在的模块

实例属性:
1.__dict__:实例属性
2.__class__:实例对应的类

'''

class Person:
    '''
    这是一个人的类
    '''
    age = 21
    def __init__(self):
        self.name = "wpf"

    def run(self):
        print('run')

print(Person.__dict__)
print(Person.__bases__)
print(Person.__doc__)
help(Person)
print(Person.__name__)
print(Person.__module__)

p = Person()
print(p.__dict__)
print(p.__class__)