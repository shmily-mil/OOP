'''

对象属性的查找（访问）机制，首先查找自己的属性，有则返回，没有根据__class__方法找到对象所对应的类的属性作为返回

object对象属性的增删改查
1.给对象增加属性或者修改属性:对象.属性=值
2.对象属性的访问:对象.属性
3.属性的删除:del 对象.属性

'''

# class Person:
#     pass
#
# a = Person()
#
# a.age = 21 # 向类中添加属性的方法:对象.属性=值
# a.height = 171
#
# a.age = 20 # 修改属性的值
#
# print(a.age) # 查看对象的属性
# print(a.__dict__)
#
# del a.age # 属性的删除
# print(a.__dict__)

'''

创建类对象时，内存内会自动生成一个地址用来存放和类相同名字的变量
类属性各个对象共享
类的__dict__属性不可被修改，而对象的__dict__属性可以被修改
不管是类还是对象，属性都是存储在__dict__这个字典中
限制对象属性的添加:__slots__ = ["age"],表示实例化的对象只能添加名为age的属性

class类属性的增删改查:(Python万物皆对象，把class当做对象，然后进行增删改查)
1.class增加属性
(1)类名.类属性=值
(2)直接在class中写属性，
class Dog:
    dogCount = 0
2.查找类属性
(1)通过类访问:类名.类属性
(2)通过对象访问:对象.类属性
3.修改类属性与增加属性相同，不能通过class实例化的object来修改class的属性
4.删除属性:del 类名.属性，不能从对象删除类的属性，只能删除直系属性

'''

# class Money:
#     pass
#
# Money.count = 1
# print(Money.count)
# print(Money.__dict__)
#
# one = Money()
# print(one.count)

class Money:
    age = 21
    hegith = 171

print(Money.age)
Money.age = 20
print(Money.age)

print(Money.__dict__)







