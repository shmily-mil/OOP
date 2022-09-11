'''

内置方法:
1.__str__:用来打印对线的属性，格式化的打印方式
2.repr():该方法用来查看类型和地址
3.__str__和repr()方法的区别:查找时先找__str__,找到即返回，找不到再去找repr()方法


'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'这个人的名字是{self.name},这个人的年龄是{self.age}'

p = Person("wpf",21)
print(p)
print(repr(p))


