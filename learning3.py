#!/usr/bin/env python3  #可以让这个learning.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-    #表示.py文件本身使用标准UTF-8编码


#     错误、调试和测试


# 错误处理
# try
# try:
# 	print('try...')
# 	r = 10 / 0
# 	print('result:', r)
# except ZeroDivisionError as e:
# 	print('except:', e)
# finally:
# 	print('finally...')
# print('END')

# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
# 而是直接跳转至错误处理代码，即except语句块，执行完except后，错误可能有多种，就通过多个except处理，
# 如果有finally语句块，则执行finally语句块，至此，执行完毕。

# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')


# Python的错误其实也是class，所有的错误类型都继承自BaseException.
# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy


#  记录错误 logging
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
# import logging
# def foo(s):
# 	return 10 / int(s)

# def bar(s):
# 	return foo(s) * 2

# def main():
# 	try:
# 		bar('0')
# 	except Exception as e:
# 		logging.exception(e)
# main()
# print('END')
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。


# 错误抛出
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例
# 要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，
# 然后，用raise语句抛出一个错误的实例：
# class FooError(ValueError):
# 	pass

# def foo(s):
# 	n = int(s)
# 	if n == 0:
# 		raise FooError('invalid value : %s' % s)
# 	return 10 / n
# foo(0)

# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（
# 比如ValueError，TypeError），尽量使用Python内置的错误类型。

# eg
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise   #raise语句如果不带参数，就会把当前错误原样抛出。

# bar()
# raise语句如果不带参数，就会把当前错误原样抛出。
# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：


#  调试  断言（assert）
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n

# def main():
#     foo('0')
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。
# 不过，启动Python解释器时可以用-O参数来关闭assert  $ python -O err.py
# 关闭后，你可以把所有的assert语句当成pass来看


# logging ：和assert比，logging不会抛出错误，而且可以输出到文件
# import logging

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
# logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？

# logging之后添加一行配置再试试：

# import logging
# logging.basicConfig(level=logging.INFO)
# 看到输出了：

# $ python err.py
# INFO:root:n = 0
# Traceback (most recent call last):
#   File "err.py", line 8, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero
# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，
# debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。


# pdb : 启动Python的调试器pdb，让程序以单步方式运行
# 我们先准备好程序：
# s = '0'
# n = int(s)
# print(10 / n)
# 然后启动：
# $ python -m pdb learning3.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
# 输入命令 n 可以单步执行代码：
# 任何时候都可以输入命令 p 变量名来查看变量：
# 输入命令 q 结束调试，退出程序：
# 如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，
# 然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
# import pdb

# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，
# 可以用命令 p 查看变量，或者用命令 c 继续运行

# IDE 
# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：
# Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。
# PyCharm：http://www.jetbrains.com/pycharm/

#  单元测试

# 我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
class Dict(dict):

	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except Exception as e:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

# d = Dict(a=1, b=2)

# print(d['a'])
# print(d.a)


# 为了编写单元测试，我们需要引入Python自带的unittest模块
# import unittest

# class TestDict(unittest.TestCase):

# 	def test_init(self):
# 		d = Dict(a = 1, b = 'test')
# 		self.assertEqual(d.a, 1)
# 		self.assertEqual(d.b, 'test')
# 		self.assertTrue(isinstance(d, dict))
		
# 	def test_key(self):
# 		d = Dict()
# 		d['key'] = 'value'
# 		self.assertEqual(d.key, 'value')

# 	def test_attr(self):
# 		d = Dict()
# 		d.key = 'value'
# 		self.assertTrue('key' in d)
# 		self.assertEqual(d['key'], 'value')

# 	def test_keyerror(self):
# 		d = Dict()
# 		with self.assertRaises(KeyError):
# 			value = d['empty']

# 	def test_attrerror(self):
# 		d = Dict()
# 		with self.assertRaises(AttributeError):
# 			value = d.empty

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
# 对每一类测试都需要编写一个test_xxx()方法
# 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：

# with self.assertRaises(KeyError):
#     value = d['empty']
# 而通过d.empty访问不存在的key时，我们期待抛出AttributeError：

# with self.assertRaises(AttributeError):
#     value = d.empty

# 运行单元测试
# if __name__ == '__main__':
# 	unittest.main()
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试：
# $ python -m unittest mydict_test

# 文档测试


# ----------------暂且放一放





























