# _*_ coding: utf-8 _*_
# @Time     : 2020/10/28 10:47
# @Author   : Peter
# @File     : 1datatype.py
# 数据类型
# 1. 整数
# 2. 浮点数
# 3. 字符串
# 4. 布尔值 True  False
# 5. 空值 None
# 6. 列表、字典

# 字符串输出
# 1. 占位符格式输出
print("%s is %d" %('jasper', 23))
# 2. format输出
print('{} is {}'.format('jasper', 123))
# 3. f-string
name = 'Jasper'
age = 123
print(f'{name} is {age}')


# list使用, tuple用法类似，tupe是不可变的，没有append，insert方法
classmates = ['Thunder', 'Flash', 'Alex', 'Jasper']
print(len(classmates))
print(classmates[0])   # 获取第一个元素
print(classmates[-1])  # 获取最后一个元素
# 添加
classmates.append('harry')
print(classmates)
classmates.insert(2, 'nico')  # 在指定位置添加
print(classmates)
# 删除
classmates.pop()           # 删除list末尾的元素
print(classmates)
classmates.pop(1)          # 删除指定位置的元素
print(classmates)
# 替换
classmates[2] = 'Peter'
print(classmates)
# 遍历
print([classmate + '-class1' for classmate in classmates])
