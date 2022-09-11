class Person:
    def run(self):
        print("实例方法")

    @classmethod # 装饰器
    def leifangfa(cls,a):
        print('这是一个类方法',cls)

Person.leifangfa(123) # 通过类调用

a = Person()
a.leifangfa(666) # 通过实例调用，实例调用的实质是实例被忽略，但class不会被忽略

class A(Person):
    pass
A.leifangfa(0) # 衍生类调用父类类方法时，传入的类是衍生类