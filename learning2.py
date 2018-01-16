#!/usr/bin/env python3  #可以让这个learning.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-    #表示.py文件本身使用标准UTF-8编码


# 面向对象编程  — —  Object Oriented Programming，简称OOP

#字典方法
# std1 = {'name': 'Michael', 'score': 98}
# std2 = {'name': 'Bob', 'score': 81}

# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))
#
# print_score(std2)

# 类

# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
#    因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
# 普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，
#    不用传递该参数。除此之外，类的方法和普通函数没有什么区别
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

# bart = Student()
# bart
# <__main__.Student object at 0x10a67a590>
# Student
# <class '__main__.Student'>

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
# >>> bart.name = 'Bart Simpson'
# >>> bart.name
# 'Bart Simpson'

#  访问限制

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
#    实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))


# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
# class Student(object):
#     def get_name(self):
#         return self.__name
#     def get_score(self):
        # return self.__score

# 如果又要允许外部代码修改score怎么办
# class Student(object):
#     def set_score(self, score):
#         self.__score = score

# 原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？
#     因为在方法中，可以对参数做检查，避免传入无效的参数：
# class Student(object):
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，
# 这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
# 意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量

# 最后注意下面的这种错误写法：

# >>> bart = Student('Bart Simpson', 59)
# >>> bart.get_name()
# 'Bart Simpson'
# >>> bart.__name = 'New Name' # 设置__name变量！
# >>> bart.__name
# 'New Name'
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

# >>> bart.get_name() # get_name()内部返回self.__name
# 'Bart Simpson'


#  继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
    
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

#c不仅仅是Dog，c还是Animal
# print(isinstance(c, Animal)) # True
# print(isinstance(c, Dog)) # True

def run_twice(ani):
    	ani.run()
    	ani.run()

run_twice(b)
run_twice(c)

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())
# 这就是著名的“开闭”原则：
# 	对扩展开放：允许新增Animal子类；
# 	对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())






















































































