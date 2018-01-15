#!/usr/bin/env python3  #可以让这个learning.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-    #表示.py文件本身使用标准UTF-8编码

'a learning module'   #一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'jinweizhao'  #使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名


	# 1.字符串和编码
# name = input('enter your name:')
# s1 = input('输入上一年成绩:')
# s2 = input('输入今年成绩:')
# s1 = float(s1)
# s2 = float(s2)

# t =  (s2 - s1) / s1

# print('%s 成绩提高了 %.1f%%' %(name, t))


	# 2.条件判断  循环
# classmates = ['aa', 'bb', 'cc']
# print(len(classmates))

# if len(classmates) > 3:
# 	print('>3') 
# elif len(classmates) == 3:
# 	print('=3')
# else:
# 	print('<3')


# print(list(range(5))) #[0,1,2,3,4]

# sum = 0
# for x in range(101):
# 	sum = sum + x

# print(sum)


	# 4.dict , set
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# # print(d['tom'])
# # print('tome' in d)
# print(d.get('tom'))
# print(d.get('tom', -1))
# print(d.pop('Bob'))

	# 5.函数
# def nop(): #空函数用pass占位
# 	pass

# isinstance(x, (int, float))  #类型检查，x是否是int或者float

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type') # 返回错误
#     if x >= 0:
#         return x
#     else:
#         return -x

# import math
# def move(x, y, step,angle = 0):
# 	nx = x + step * math.cos(angle)
# 	ny = y - step * math.sin(angle)
# 	return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# z = move(100, 100, 60, math.pi / 6)
# print(x, y, z)


# def power(x, n=2):#默认参数:必选参数在前，默认参数在后
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))
# print(power(5, 2))




# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', 'Tianjin')
# enroll('Adam', 'M', city='Tianjin')  #有间隔的话需要写city键指明是哪一个


#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
#每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# def add_end(L=[]):  
#     L.append('END')
#     return L

# print(add_end())
# print(add_end())
# print(add_end())

#定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end2(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# print(add_end2())
# print(add_end2())



#可变参数: 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# def calc(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum + n * n
# 	return sum
# nums = [1, 2, 3]
#*nums表示把nums这个list的所有元素作为可变参数传进去
# print(calc(*nums))


#关键字参数: 关键字参数允许你传入0个或任意个含参数名的参数，
#   	 这些关键字参数在函数内部自动组装为一个dict

#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
# def person(name, age, **kw):
# 	print('name:', name, 'age:', age, 'other:', kw)

# person('michael', 30)
#也可以传入任意个数的关键字参数
# person('bob', 35, city = 'Beijing')
# person('Adam', 45, gender = 'M', job = 'Engineer')

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
#     kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])
#或
# person('Jack', 24, **extra)


#命名关键字参数: 到底传入了哪些，就需要在函数内部通过kw检查
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         print('有city参数')
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)

# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

#要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# def person(name, age, *, city, job):
#     print(name, age, city, job)
# person('Jack', 24, city = 'Beijing', job = 'Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)

#命名关键字参数可以有缺省值，从而简化调用：
# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)

# person('Jack', 24, job='Engineer')


#参数组合: 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# f1(1, 2)
# f1(1, 2)
# f1(1, 2)
# f1(1, 2, 3, 'a', 'b', x=99)
# f2(1, 2, d=99, ext=None)

#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)

# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f2(*args, **kw)

#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(*numbers):
#     if len(numbers) == 0:
#         raise TypeError('没有数值')
#     total = 1
#     for num in numbers:
#         total = total * num
#     return total
# # 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


#递归函数:如果一个函数在内部调用自身本身，这个函数就是递归函数
# def fact(n):
# 	if n == 1:
# 		return 1
# 	return n * fact(n - 1)
# print(fact(5))
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
#所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
# print(fact(1000))

#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，
#所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，
#不会出现栈溢出的情况。
#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
#要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
# def fact(n):
# 	return fact_iter(n, 1)
# def fact_iter(num, product):
# 	if num == 1:
# 		return product
# 	return fact_iter(num - 1, num * product)
# print(fact(5))


#汉诺塔
# def move(n, a, b, c):
# 	if n == 1:
# 		print(a + '->' + c)
# 	else:
# 		move(n - 1, a, c, b)
# 		move(1, a, b, c)
# 		move(n - 1, b, a, c)

# move(3, 'A', 'B', 'C')


	# 6 高级特性
# 切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。
#索引0，1，2，正好是3个元素。
#如果第一个索引是0，还可以省略

# print(L[0:3])
# print(L[:2])

#既然Python支持L[-1]取倒数第一个元素，
#那么它同样支持倒数切片
# print(L[-2:])
# print(L[-2:-1])

# L = list(range(100)) #L = [0,1,2,...,99]
#前十个
# L[:10]
# #前十个数，每两个取一个
# print(L[:10:2])
# #所有的数 每五个取一个
# print(L[::5])
# #字符串也可以看成 list 操作
# print('ABCDEFG'[::2])

#去除字符串首尾的空格 ，注意不要调用str的strip()方法
# def trim(s):
# 	while s[:1] == ' ':
# 		s = s[1:]
# 	while s[-1:]==' ':
#	 	s = s[:-1]
# 	return s
# print(trim('   hello  world   3 '))
	
#迭代
# d = {'a': 1, 'b': 2, 'c': 3}
#dict迭代的是key。如果要迭代value，可以用for value in d.values()，
#如果要同时迭代key和value，可以用for k, v in d.items()
# for key in d:
# 	print(key)

#判断一个对象是否可迭代，通过 collections 模块的 Iterable 类型判断
# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance([1, 2, 3], Iterable))
# print(isinstance(123, Iterable))


#Python内置的enumerate函数可以把一个list变成索引-元素对
# for i, value in enumerate(['a', 'b', 'c']):
# 	print(i, value)

# 列表生成式
# list(range(1, 5)) #[1, 2, 3, 4, 5]

# [x * x for x in range(1, 11)] #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
# [x * x for x in range(1, 11) if x % 2 == 0] #[4, 16, 36, 64, 100]

#还可以使用两层循环，可以生成全排列
# [m + n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#列表生成式也可以使用两个变量来生成list
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# [k + '=' + v for k, v in d.items()]   #['y=B', 'x=A', 'z=C']


#生成器: 在Python中，这种一边循环一边计算的机制，称为生成器：generator，
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
# L = [x * x for x in range(10)]
# g = (x * x for x in range(10))
# print(L)
# print(g)

#斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
# def fib(max):
# 	n ,a, b = 0, 0, 1
# 	while n < max:
# 		print(b)
# 		a, b = b, a + b
# 		n = n + 1
# 	return 'done'
# fib(6)

#定义generator的另一种方法。如果一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator
# def fib(max):
# 	n ,a, b = 0, 0, 1
# 	while n < max:
# 		yield b
# 		a, b = b, a + b
# 		n = n + 1
# 	return 'done'
# f = fib(6)
# print(f)

#用for循环调用generator时，发现拿不到generator的return语句的返回值。
#   如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
# while True:
# 	try:
# 		x = next(f)
# 		print(x)
# 	except StopIteration as e:
# 		print('Generator return value: ', e.value)
# 		break


#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
#  在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# def odd():
# 	print('1')
# 	yield 1
# 	print('2')
# 	yield(2)
# 	print('3')
# 	yield(5)
# o = odd()
# next(o)
# next(o)
# next(o)


#杨辉三角
# def triangles():
# 	b = [1]
# 	while True:
# 		yield b
# 		temp = b[:]
# 		temp.append(0)
# 		temp = [temp[x - 1] + temp[x] for x in range(len(temp))]
# 		b = temp[:]

# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     # print(results)
#     n = n + 1
#     if n == 10:
#         break

# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')
	
#迭代器
#使用isinstance()判断一个对象是否是Iterable对象
# from collections import Iterable
# isinstance((x for x in range(10)), Iterable)
#而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回
#   下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

# isinstance(iter('abc'), Iterator)  # True

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？

# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的


# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

# for x in [1, 2, 3, 4, 5]:
#     pass
# 实际上完全等价于：

# 首先获得Iterator对象:
# it = iter([1, 2, 3, 4, 5])
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break


#        7 函数式编程
#高阶函数
#map() : 接收两个参数，一个是函数，一个是Iterable，
#   map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# def f(x):
# 	return x * x

# r = map(f, [1,2,3,4,5])
# print(r)
# print(list(r))
# list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Int数组转字符串数组


#reduce() : 把一个函数作用在一个序列[x1, x2, x3, ...]上，
#   这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#   reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#eg : 
# from functools import reduce
# def add(x, y):
# 	return x + y
# reduce(add, [1, 3, 5, 9])  # 25

# def fn(x, y):
# 	return x * 10 + y
# reduce(fn, [1, 3, 5, 7])   # 1357

#整理成一个函数:
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))

# 转成首字母大写，其余小写
# def normalize(name):
#     return name.capitalize()  #转换

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

#sum()函数可以接受一个list并求和,写一个接受一个list并利用reduce()求积
# def prod(L):
# 	def chengji(x, y):
# 		return x * y
# 	return reduce(chengji, L)

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# DIGITS = {'.': '.', '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2float(s):
# 	def fn(x, y):
# 		return x * 10 + y
# 	l = list(map(lambda c: DIGITS[c], s))
# 	if '.' in l:
# 		n = len(l) - l.index('.') - 1
# 		l.remove('.')
# 		return reduce(fn, l) / (10 ** n)  # **就是成方 10 的 n 次方
# 	else:
# 		return reduce(fn, l)
# print('str2float(\'123.456\') =', str2float('123.456'))


# filter()  过滤序列:filter()也接收一个函数和一个序列。filter()把传入的函数
#         依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 删掉偶数，只保留奇数
# def is_odd(n):
#     return n % 2 == 1
# list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

# def not_empty(s):
#     return s and s.strip()  
# list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

# 用 埃拉托色尼筛选法  计算无限素数

# 1，先构造一个从3开始的奇数序列
# def _odd_iter():
# 	n = 1
# 	while True:
# 		n = n + 2
# 		yield n
# # 2,定义筛选函数
# def _not_divisible(n):
# 	return lambda x: x % n > 0
# # 3,定义一个生成器，不断返回下一个素数
# def primes():
# 	yield 2
# 	it = _odd_iter()
# 	while True:
# 		n = next(it)
# 		yield n
# 		it = filter(_not_divisible(n), it)

# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break


#练习:回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数

# def is_palindrome(n):
#     str = '%s' % n
#     return str[:] == str[::-1]
	
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


# sorted 排序
# sorted([36, 5, -12, 9, -21]) # [-21, -12, 5, 9, 36]
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# sorted([36, 5, -12, 9, -21], key=abs) # [5, 9, -12, -21, 36]

#默认情况下，对字符串排序，是按照ASCII的大小比较的
# sorted(['bob', 'about', 'Zoo', 'Credit']) # sorted(['bob', 'about', 'Zoo', 'Credit'])
#实现忽略大小写的排序
# sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
# sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
#  ['Zoo', 'Credit', 'bob', 'about']

# 返回函数
#   可变参数的求和 如果不需要立刻求和
# def lazy_sum(*args):
# 	def sum():
# 		ax = 0
# 		for n in args:
# 			ax = n + ax
# 		return ax
	# return sum
# f = lazy_sum(1,3,4,6)
# print(f())

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
# f1 != f2
# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)


#  闭包
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
#等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量
#     当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# def count():
# 	def f(j):
# 		def g():
# 			return j * j
# 		return g
# 	fs = []
# 	for i in range(1, 4):
# 		fs.append(f(i))
# 	return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())


# def count():
#     fs = []
#     for i in range(1,4):
#         fs.append(lambda i : (lambda i: i * i))
#     return fs
# a,b,c = count()
# print(a(3)


# 利用闭包返回一个计数器函数，每次调用它返回递增整数
# 生成器方法：
# def createCounter():
#     def f():
#         n = 0
#         while True:
#             n += 1
#             yield n
#     sum = f()
#     def counter():
#         return next(sum)
#     return counter

# # list方法：
# def createCounter():
#     fs = [0]
#     def counter():
#         fs[0] = fs[0] + 1
#         return fs[0]
#     return counter

# # 全局变量方法（自己写的是这个，但是忽略了局部变量和全局变量，一直没有调出来）：
# def createCounter():
#     i = 0
#     def counter():
#         nonlocal i #加上这句之后就可以了
#         i += 1
#         return i
#     return counter


# 匿名函数 lambda x: x * x  ==   def f(x): return x * x

# f(x)=x2 [1, 4, 9, 16, 25, 36, 49, 64, 81] 
# list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 装饰器   假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
#       但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# def now():
# 	print('2015-3-25')
# 函数对象有一个__name__属性，可以拿到函数的名字：
# print(now.__name__)
# print(f.__name__)

# decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
# def log(func):
# 	def wrapper(*args, **kw):
# 		print('call %s():' % func.__name__)
# 		return func(*args, **kw)
# 	return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 	 我们要借助Python的@语法，把decorator置于函数的定义处：
# @log
# def now():
# 	print('2015-3-3')
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
# now()
# 把@log放到now()函数的定义处，相当于执行了语句
# abc = log(now)
# abc()
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
#     写出来会更复杂。比如，要自定义log的文本
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# @log('execute')
# def now():
#     print('2015-3-25')

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的
# now = log('execute')(now)
# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，
# 再调用返回的函数，参数是now函数，返回值最终是wrapper函数
# now()

#以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，
#   它有__name__等属性，但你去看经过decorator装饰之后的函数，
#   它们的__name__已经从原来的'now'变成了'wrapper'：
#   不需要编写wrapper.__name__ = func.__name__这样的代码，
#   Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

# import functools
# def log():
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print('call %s()' % func.__name__)
# 		return func(*args, **kw)
# 	return wrapper
# 或者针对带参数的decorator：
# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# import time, functools
# def metric(fn):
# 	@functools.wraps(fn)
# 	def wrapper(*args, **kw):
# 		begin = time.time()
# 		result = fn(*args, **kw) # 函数在此执行
# 		end = time.time()
# 		print('%s executed in %s ms' % (fn.__name__, (end - begin)))
# 		return result
# 	return wrapper
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
# f = fast(11, 22)
# s = slow(11, 22, 33)
# print(fast.__name__, s)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


# 偏函数
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住
# （也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
# 所谓偏函数，其实就是将一个已知参数和函数进行绑定，生成一个新的函数
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
# int('12345')   # 12345

# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
# int('12345', base=8)  # 5349
# int('12345', 16)    # 74565
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
#     于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
# def int2(x, base=2):
#     return int(x, base)
# int2('1000000')   #  64

# functools.partial就是帮助我们创建一个偏函数的，
#   不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
# import functools
# int2 = functools.partial(int, base=2)
# int2('1000000')   #  64

# int2('1000000', base=10)   # 1000000

# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入:
# int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是：
# int2('10010')
# 相当于
# kw = { 'base': 2 }
# int('10010', **kw)
# 当传入：
# max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：

# max2(5, 6, 7)
# 相当于：
# args = (10, 5, 6, 7)
# max(*args)
# 结果为10
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。




#              模块
# 一个.py文件就称之为一个模块（Module）。
# 如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，
#      Python又引入了按目录来组织模块的方法，称为包（Package）。
	# mycompany
	# ├─ __init__.py
	# ├─ abc.py
	# └─ xyz.py
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
# 现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。

# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，
# Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
# 也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany

# 创建自己的模块时，要注意：
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检
#     查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。

# 使用模块  import hello.py
# 作用域  import hello.py

# 安装第三方模块：Python中，安装第三方模块，是通过包管理工具pip完成的
# 第三方库都会在Python官方的pypi.python.org网站注册
# pip install Pillow
# 使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，
#     我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。

#-------->面向对象编程    后边接  learning2.py
