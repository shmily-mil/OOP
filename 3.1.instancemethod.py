class Person:
    def eat(self,food):
        print('吃饭',food)

a = Person()
a.eat("土豆") # 标准调用
Person.eat(a,"土豆")
print(Person.eat) # 返回的是函数本身















