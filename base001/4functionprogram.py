# _*_ coding: utf-8 _*_
# @Time     : 2020/10/28 12:03
# @Author   : Peter
# @File     : 4functionprogram.py
# 1. 高阶函数 map/reduce、filter、sorted
# 2. 返回函数  函数作为返回值
# 3. 匿名函数  lambda x: x * x
# 4. 装饰器
# 5. 偏函数


# 高阶函数
# 把这个list所有数字转为字符串, 使用map即可
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)  这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce


def add(x, y):
    return x + y


reduce(add, [1, 3, 5, 7, 9])


# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1


ret = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(ret)


# 返回函数，就是函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())

# 匿名函数 lambda x: x * x, 冒号前面的x表示函数参数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
f = lambda x: x * x
print(f(5))

print('########################## decorator ##################################')
# 装饰器一: 函数带多个参数
import time


def timer(func):
    def wrapper(*kargs, **kwargs):
        start_time = time.time()
        func(*kargs, **kwargs)
        end_time = time.time()
        print('{} elapse time {}s'.format(func.__name__, int(end_time - start_time)))

    return wrapper


@timer
def test_time():
    time.sleep(3)


@timer
def test_time_var(name, age):
    print(f'{name} is {age}')


test_time()
test_time_var('harry', 18)


# 装饰器二： 多装饰器情况
# 离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程
# 装饰过程:
# @make_div + @make_p
# content = make_div(make_p(content))
def make_div(func):
    def wrapper(*args, **kwargs):
        return '<div>' + func() + '</div>'

    return wrapper


def make_p(func):
    def wrapper(*args, **kwargs):
        return '<p>' + func() + '</p>'

    return wrapper


@make_div
@make_p
def content():
    return "人生苦短"


print(content())


# 装饰器三: 函数带多个参数，装饰器也带多个参数
def decorator(*dargs, **dkargs):
    def wrapper(func):
        def _wrapper(*args, **kargs):
            print(f'decrator param: {dargs}, {dkargs}')
            print(f'function param: {args}, {kargs}')
            return func(*args, **kargs)

        return _wrapper

    return wrapper


@decorator(1, a=2)
def foo(x, y=0):
    print(f'foo {x} {y}')


foo(3, 4)

print('================================ 偏函数 functools.partial ==================================================')
# 偏函数
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单
import functools
int2 = functools.partial(int, base=2)    # int2是把传入的二进制字符串，转换成十进制
print(int2('1000101'))
