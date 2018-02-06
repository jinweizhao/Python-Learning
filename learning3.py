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
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise   #raise语句如果不带参数，就会把当前错误原样抛出。

bar()
# raise语句如果不带参数，就会把当前错误原样抛出。
# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：















































