# _*_ coding: utf-8 _*_
# @Time     : 2020/10/28 11:18
# @Author   : Peter
# @File     : 2function.py

# 1. 位置参数
# 2. 默认参数
# 3. 可变参数
# 4. 关键字参数

# 位置参数
def func(name):
    print(f'func say hi {name}')


func('Jasper')


# 默认参数
def default_func(name='nico'):
    print(f'default_func say hi {name}')


default_func()
default_func('peter')


# 可变参数
def var_fun(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print(f'var_fun is {sum}')


var_fun()
var_fun(1)
var_fun(1, 2, 3, 4, 5)


# 关键词参数
def kw_func(name, age, **kw):
    print(f'kw_func {name} is {age},{kw}')


kw_func('Nico', 18)
kw_func('Nico', 18, harry=19)
