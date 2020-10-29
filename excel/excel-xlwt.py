# _*_ coding: utf-8 _*_
# @Time     : 2020/10/29 12:42
# @Author   : Peter
# @File     : excel-xlwt.py

import xlwt

def xlwt_write():
    # 创建工作簿
    workbook = xlwt.Workbook()
    # 创建工作表
    sheet1 = workbook.add_sheet(u'练习表1')
    sheet2 = workbook.add_sheet(u'练习表2')
    # 定义首行标题内容
    title = [u'name', u'age', u'gender', u'major']
    # 写入数据
    row = 0
    for col, v in enumerate(title):
        sheet1.write(row, col, v)
    row += 1
    sheet1.write(row, 0, 'simon')
    sheet1.write(row, 1, 18)
    sheet1.write(row, 2, 'male')
    row += 1
    sheet1.write(row, 0, 'lisa')
    sheet1.write(row, 1, 18)
    sheet1.write(row, 2, 'female')

    # 合并major列（第2、3行，第4列）使用合并方法
    # x代表第几行，这里第2行，x = 1（从0开始，和数组下标类似）
    # m代表合并行数，m = 1，x + m = 2
    # y代表第几列，这里第4列，y = 3
    # n代表合并列数，n = 0，y + n = 3
    # string为填入单元格的内容，style参数是可选的，这里没有定义格式，就先不写
    sheet1.write_merge(1, 2, 3, 3, 'IT')

    # 保存
    workbook.save('./data/demo.xls')


xlwt_write()
