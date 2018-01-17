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

class Husky(Dog):

    def run(self):
        print('Husky is running...')

# class Cat(Animal):

#     def run(self):
#         print('Cat is running...')

# a = list() # a是list类型
# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型

#c不仅仅是Dog，c还是Animal
# print(isinstance(c, Animal)) # True
# print(isinstance(c, Dog)) # True

# def run_twice(ani):
#     	ani.run()
#     	ani.run()

# run_twice(b)
# run_twice(c)

# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running slowly...')

# run_twice(Tortoise())
# 这就是著名的“开闭”原则：
# 	对扩展开放：允许新增Animal子类；
# 	对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

# class Timer(object):
#     def run(self):
#         print('Start...')

# run_twice(Timer())


# 获取对象信息
# 来判断对象类型，使用type()函数
# >>> type(abs)
# <class 'builtin_function_or_method'>
# >>> type(a)
# <class '__main__.Animal'>
# >>> type(abs)
# <class 'builtin_function_or_method'>
# >>> type(a)
# <class '__main__.Animal'>

# 如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
# import types
# def fn():
# 	pass
# print(type(fn))   #<class 'function'>
# >>> type(fn)==types.FunctionType
# True
# >>> type(abs)==types.BuiltinFunctionType
# True
# >>> type(lambda x: x)==types.LambdaType
# True
# >>> type((x for x in range(10)))==types.GeneratorType
# True

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
# 继承关系是：object -> Animal -> Dog -> Husky
a = Animal()
d = Dog()
h = Husky()

# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
# >>> isinstance(h, Husky)
# True
# >>> isinstance(h, Dog)
# True


# 能用type()判断的基本类型也可以用isinstance()判断：
# >>> isinstance('a', str)
# True
# >>> isinstance(123, int)
# True
# >>> isinstance(b'a', bytes)
# True

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
# >>> isinstance([1, 2, 3], (list, tuple))
# True
# >>> isinstance((1, 2, 3), (list, tuple))
# True

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。


# dir():如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# print(dir('abc'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，
#     如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
#     它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
# >>> len('ABC')
# 3
# >>> 'ABC'.__len__()
# 3

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
# >>> class MyDog(object):
# ...     def __len__(self):
# ...         return 100
# ...
# >>> dog = MyDog()
# >>> len(dog)
# 100


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
# class MyObject(object):
# 	def __init__(self):
#         self.x = 9
#     def power(self):
#         return self.x * self.x
# obj = MyObject()

# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19

# 可以传入一个default参数，如果属性不存在，就返回默认值：
# >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 404

# 也可以获得对象的方法：
# >>> hasattr(obj, 'power') # 有属性'power'吗？
# True
# >>> getattr(obj, 'power') # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
# >>> fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn() # 调用fn()与调用obj.power()是一样的
# 81

# python 中 or 和 and 的使用规则
# 		x or y 的值只可能是x或y.  x为真就是x, x为假就是y
# 		x or y 的值只可能是x或y.  x为真就是x, x为假就是y
# 		对于, 1 or 5 and 4: 先算5 and 4, 5为真, 值为4. 再算1 or 4, 1 为真,值为1

# 		对于, (1 or 5) and 4: 先算1 or 5, 1为真, 值为1. 再算1 and 4, 1为真,值为4

# or的左右两边都为假时，返回最后一个假
# and的左右两边都为真时，返回最后一个真

# >>> tuple or list
# <class 'tuple'>
# >>> list or tuple
# <class 'list'>
# >>> tuple and list
# <class 'list'>
# >>> list and tuple
# <class 'tuple'>


# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。给实例绑定属性的方法是通过实例变量，或者通过self变量：
# class Student(object):
#     def __init__(self, name):
#         self.name = name

# s = Student('Bob')
# s.score = 90
# print(s.score)   #90
# print(hasattr(s, 'score'))   #True

# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，
# 这种属性是类属性，归Student类所有：

# class Student(object):
#     name = 'Student'
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：

# >>> class Student(object):
# ...     name = 'Student'
# >>> s = Student() # 创建实例s
# >>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
# >>> print(Student.name) # 打印类的name属性
# Student
# >>> s.name = 'Michael' # 给实例绑定name属性
# >>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
# >>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student
# >>> del s.name # 如果删除实例的name属性
# >>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student




#       面向对象高级编程
































