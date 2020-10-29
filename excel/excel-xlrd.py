# _*_ coding: utf-8 _*_
# @Time     : 2020/10/29 9:32
# @Author   : Peter
# @File     : excel-xlrd.py

import xlrd
from pyecharts.charts import Bar


def test_xlrd():
    workbook_data = xlrd.open_workbook('./data/xlrd-data.xlsx')  # 读取表格
    sheet_data = workbook_data.sheets()[0]  # 获取表格的sheets[0]
    # 输出行列
    print(sheet_data.nrows)
    print(sheet_data.ncols)
    # 获取第一行数据
    row1data = sheet_data.row_values(0)
    print(row1data)
    print(row1data[0])


def vw_pyecharts():
    data = xlrd.open_workbook('./data/xlrd-data.xlsx')
    sheet_table = data.sheets()[0]
    xdata = []
    ydata = []
    for i in range(1, sheet_table.nrows):
        print(sheet_table.row_values(i))
        xdata.append(sheet_table.row_values(i)[0])
        ydata.append(sheet_table.row_values(i)[1])

    print(xdata)
    print(ydata)

    # 数据可视化，柱状图
    bar = Bar()
    bar.add_xaxis(xdata)
    bar.add_yaxis("名称1", ydata)
    bar.render("show.html")


vw_pyecharts()
