'''

1.私有属性或者方法都是通过名字重整机制来实现的
2.如果定义了一个名字重整机制之后的名字为方法名，这会导致之前的方法被覆盖

'''

class Person:
    __age = 21
    def __run(self):
        print("run")

p = Person()
# p.__run()
print(Person.__dict__)