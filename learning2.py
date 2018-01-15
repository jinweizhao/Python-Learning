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






























































