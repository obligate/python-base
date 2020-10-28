# _*_ coding: utf-8 _*_
# @Time     : 2020/10/28 11:32
# @Author   : Peter
# @File     : 3advancefeature.py

# 1. 切片 [:]
# 2. 迭代
# 3. 列表生成式 []
# 4. 生成器 yield 和 ()
# 5. 迭代器 for

# 切片
classmates = ['Thunder', 'Flash', 'Alex', 'Jasper']
# 取前3个元素
print(classmates[0:3])  # 等价下面
print(classmates[:3])
# 取后3个元素
print(classmates[-3:])
# 只写[:]就可以原样复制一个list
print(classmates[:])

# 如何判断一个对象是可迭代对象
# from collections import Iterable # - 3.8 deprecated
# isinstance('abc', Iterable)
# isinstance(classmates, Iterable)
# isinstance({'a': 1, 'b': 2, 'c': 3}, Iterable)

# 列表迭代
print([classmate + '-11' for classmate in classmates])
# 获取列表的索引
for i, value in enumerate(classmates):
    print(i, value)
# 字典迭代
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()
dicts = {'a': 1, 'b': 2, 'c': 3}
for key in dicts:
    print(key)
for value in dicts.values():
    print(value)
for k, v in dicts.items():
    print(f'{k} {v}')

# 列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])  # for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])  # 同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value

# 生成器
# 1. 只要把一个列表生成式的[]改成()
# 2. yield
print('========================generator=============================')
g = (x * x for x in range(10))
print(next(g))  # next获取值，基本不用
for n in g:  # for循环获取值
    print(n)


def g1():
    yield 1
    yield 2
    yield 3
    yield 4


for n in g1():
    print(n)
