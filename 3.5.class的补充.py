'''
元类：
1.创建class的是元类,type就是最常见的元类
'''
# a = 10 # a的类为int，int的类为type,套娃，类中类
# print(a.__class__)
# print(int.__class__)
#
# s = "abc"
# print(s.__class__)
# print(str.__class__)
#
# class Person:
#     age = 21
# a = Person()
# print(a.__class__)
# print(Person.__class__)


'''
使用type创建class,自己手动创建类，而class创建类是内部系统自动创建的类对象
'''
# def eat(self):
#     print("吃饭")
# Person = type("Person",(),{"age":21,"eat":eat})
# print(Person.eat)
# a = Person()
# print(a.eat())


'''
类的描述:格式
'''
# class Person:
#     '''
#     关于这个类的描述，类的作用，类的构造函数等
#     '''
#
#     age = 21
#
#     def eat(self,num,liang):
#         '''
#
#         :param num: 参数的含义，参数类型，是否有默认值
#         :param liang:
#         :return:
#         '''
#         print("chifan")
#
# help(Person)


'''
注释文档的生成
1.python -m pydoc -b
'''


'''
私有化属性:
1.python中没有真正的私有化属性，但是可以使用下划线完成伪私有化的效果
2.变量前加一个_,表示受保护的属性;加两个_,表示私有化属性;该规则在class和instance均适用,变量前不加_，表示公有属性

1.公有属性:一般哪里都能访问
2.受保护属性:类的内部和子类都可以访问,其他modul内建议不要访问
3.私有属性:类内部可以访问，子类不可访问，也不可在类的外部访问，私有属性在其他地方不能被访问的原因是私有属性的名字重整机制
'''
# if __name__ == "__main__":
#     class Animal:
#         a = 10
#         def text(self):
#             print(self.a)
#
#     class Dog(Animal):
#         def text2(self):
#             print(self.a)
#
#     # A = Animal()
#     # A.text()
#     # d = Dog()
#     # d.text2()
#     # d.text()


'''
只读属性
'''









