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
def triangles():
	b = [1]
	while True:
		yield b
		temp = b[:]
		temp.append(0)
		temp = [temp[x - 1] + temp[x] for x in range(len(temp))]
		b = temp[:]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    # print(results)
    n = n + 1
    if n == 10:
        break

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
	



























