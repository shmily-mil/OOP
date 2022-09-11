

class Person:
    @staticmethod
    def jingtaifangfa():
        print('这是一个静态方法')

Person.jingtaifangfa() # 通过类调用

a = Person()
a.jingtaifangfa() # 通过实例调用