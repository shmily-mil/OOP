class Person:
    def __init__(self): # 初始化方法，在创建实例时，会自动调用这个方法
        self.__age = 21

    def setAge(self,value):
        if isinstance(value,int) and 0 < value < 100:
            self.__age = value
        else:
            print("error")

    def getAge(self):
        return self.__age

a = Person()
a.setAge(99)
print(a.getAge())