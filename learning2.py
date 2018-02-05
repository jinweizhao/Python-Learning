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
# class Student(object):
#     pass

# s = Student()
# s.name = 'Michael' # 动态给实例绑定一个属性
# print(s.name)  # Michael

# 还可以尝试给实例绑定一个方法：
# def set_age(self, age):
# 	self.age = age

# from types import MethodType
# s.set_age = MethodType(set_age, s)  #给实例绑定一个方法
# s.set_age(28)
# print(s.age)

# 为了给所有实例都绑定方法，可以给class绑定方法：
# def set_score(self, score):
# 	self.score = score
# Student.set_score = set_score   # 给class绑定方法后，所有实例均可调用


# 使用__slots__
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
# class Student(object):
# 	__slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
		
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


# 使用 @property

# 为了限制score的范围：
# class Student(object):

#     def get_score(self):
#          return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# 上面的方法又略显复杂，没有直接用属性这么直接简单

# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# s = Student()
# s.score = 60   # OK，实际转化为s.set_score(60)
# print(s.score  # OK，实际转化为s.get_score()

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

# class Screen(object):

# 	@property
# 	def width(self):
# 		return self._width    #加单下划线意思：1，私有化属性或方法。2，防止递归调用

# 	@width.setter
# 	def width(self, value):
# 		if  not isinstance(value, int):
# 			raise ValueError('width must be an integer')
# 		self._width = value


# 	@property
# 	def height(self):
# 		return self._height

# 	@height.setter
# 	def height(self, value):
# 		if not isinstance(value, int):
# 			raise ValueError('height must be an interger')
# 		self._height = value

# 	@property
# 	def resolution(self):
# 		return self._width * self._height
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')


#  多重继承
# 我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，
# 		你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，
# 		让某个动物同时拥有好几个MixIn：
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 		我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# 多重继承三原则：
# 1.子类永远在父类前面
# 2.如果有多个父类，会根据它们在列表中的顺序被检查
# 3.如果对下一个类存在两个合法的选择，选择第一个父类



# 定制类 例如 __slots__

# __str__
# >>> class Student(object):
# ...     def __init__(self, name):
# ...         self.name = name
# ...
# >>> print(Student('Michael'))
# <__main__.Student object at 0x109afb190>
# 打印出一堆<__main__.Student object at 0x109afb190>，不好看

# >>> class Student(object):
# ...     def __init__(self, name):
# ...         self.name = name
# ...     def __str__(self):
# ...         return 'Student object (name: %s)' % self.name
# ...
# >>> print(Student('Michael'))
# Student object (name: Michael)

# >>> s = Student('Michael')
# >>> s
# <__main__.Student object at 0x109afb310>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
#     而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name=%s)' % self.name
#     __repr__ = __str__


# __iter__
# 	如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 		该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 		直到遇到StopIteration错误时退出循环。

# 以斐波那契数列为例
# class Fib(object):
# 	def __init__(self):
# 		self.a, self.b = 0, 1

# 	def __iter__(self):
# 		return self  # 实例本身就是迭代对象，故返回自己
# 	def __next__(self):
# 		self.a, self.b = self.b, self.a + self.b   # 计算下一个值
# 		if self.a > 100000:  # 退出循环的条件
# 			raise StopIteration()
# 		return self.a  # 返回下一个值
# for n in Fib():
# 	print(n)


# __getitem__ 
# 	Fib实例虽然能作用于for循环，看起来和list有点像，
# 	但是，把它当成list来使用还是不行，比如，取第5个元素：
# >>> Fib()[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object does not support indexing

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
# >>> f = Fib()
# >>> f[0]
# 1
# >>> f[1]
# 1
# >>> f[2]

# 这样不支持切片方法：原因是__getitem__()传入的参数可能是一个int，
# 		也可能是一个切片对象slice，所以要做判断：
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice): # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L


# __getattr__   
# 调用一个类中不存在的属性时会报错
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，
#     那就是写一个__getattr__()方法，动态返回一个属性。修改如下
# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'

#     def __getattr__(self, attr):
#         if attr=='score':
#             return 99
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
# 		要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
# class Student(object):

#     def __getattr__(self, attr):
#         if attr=='age':
#             return lambda: 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# REST API  /  链式调用   略


#  __call__
# 当我们调用实例方法时，我们用instance.method()来调用。实现直接在实例本身上调用
# class Student(object):
#     def __init__(self, name):
#         self.name = name

#     def __call__(self):
#         print('My name is %s.' % self.name)
# >>> s = Student('Michael')
# >>> s() # self参数不要传入
# My name is Michael.

# 怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
# >>> callable(Student())
# True
# >>> callable(max)
# True
# >>> callable([1, 2, 3])
# False
# >>> callable(None)
# False
# >>> callable('str')
# False
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

# 练习
# class Chain(object):
#     def __init__(self,path=''):
#         self._path=path
#     def __str__(self):
#         return self._path
#     def __getattr__(self,path):
#         return Chain('%s/%s' % (self._path,path))
#     __call__=__getattr__
#     __repr__=__str__

# print(Chain().status.user.timeline.list)
# print(Chain().users('Zhangsan').repos)


#  使用枚举类
from enum import Enum
Month = Enum('Month', 
	('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数。

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# @unique装饰器可以帮助我们检查保证没有重复值。

# 使用：
# >>> day1 = Weekday.Mon
# >>> print(day1)
# Weekday.Mon
# >>> print(Weekday.Tue)
# Weekday.Tue
# >>> print(Weekday['Tue'])
# Weekday.Tue
# >>> print(Weekday.Tue.value)
# 2
# >>> print(day1 == Weekday.Mon)
# True
# >>> print(day1 == Weekday.Tue)
# False
# >>> print(Weekday(1))
# Weekday.Mon
# >>> print(day1 == Weekday(1))
# True


#   使用元类
# >>> def fn(self, name='world'): # 先定义函数
# ...     print('Hello, %s.' % name)
# ...
# >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
# >>> h = Hello()
# >>> h.hello()
# Hello, world.
# >>> print(type(Hello))
# <class 'type'>
# >>> print(type(h))
# <class '__main__.Hello'>

# 要创建一个class对象，type()函数依次传入3个参数：

# 1，class的名称；
# 2，继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3，class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# metaclass : 定义metaclass，就可以创建类，最后创建实例。
# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# # metaclass是类的模板，所以必须从`type`类型派生：
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：

# class MyList(list, metaclass=ListMetaclass):
#     pass
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：
# 1,当前准备创建的类的对象；
# 2,类的名字；
# 3,类继承的父类集合；
# 4,类的方法集合。







