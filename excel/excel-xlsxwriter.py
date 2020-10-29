# _*_ coding: utf-8 _*_
# @Time     : 2020/10/29 12:48
# @Author   : Peter
# @File     : excel-xlsxwriter.py

import xlsxwriter  # 导入模块


def create_workbook():
    workbook = xlsxwriter.Workbook('result/excel_xlsxwriter.xlsx')  # 新建excel表
    worksheet = workbook.add_worksheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）
    headings = ['Number', 'testA', 'testB']  # 设置表头
    data = [
        ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
        [10, 40, 50, 20, 10, 50],
        [30, 60, 70, 50, 40, 30],
    ]  # 自己造的数据

    worksheet.write_row('A1', headings)

    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])  # 将数据插入到表格中

    workbook.close()  # 将excel文件保存关闭，如果没有这一行运行代码会报错


def create_book_with_charts():
    workbook = xlsxwriter.Workbook('result/new_xlsxwriter_with_charts.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    headings = ['Number', 'testA', 'testB']  # 创建表头
    data = [
        ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
        [10, 40, 50, 20, 10, 50],
        [30, 60, 70, 50, 40, 30],
    ]  # 自己造的数据

    worksheet.write_row('A1', headings)

    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])  # 将数据插入到表格中


    # area：面积图
    # bar：直方图
    # colume：柱状图
    # line：折线图
    # pie：饼图
    # doughnut：环形图
    # sactter：散点图
    # stock：股票趋势图
    # radar：雷达图
    chart_col = workbook.add_chart({'type': 'line'})  # 新建图表格式 line为折线图
    chart_col.add_series(  # 给图表设置格式，填充内容
        {
            'name': '=sheet1!$B$1',
            'categories': '=sheet1!$A$2:$A$7',
            'values': '=sheet1!$B$2:$B$7',
            'line': {'color': 'red'},
        }
    )

    chart_col.set_title({'name': '测试'})
    chart_col.set_x_axis({'name': "x轴"})
    chart_col.set_y_axis({'name': 'y轴'})  # 设置图表表头及坐标轴

    chart_col.set_style(1)

    worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})  # 放置图表位置

    workbook.close()


def create_charts_line():
    # 创建一个excel
    workbook = xlsxwriter.Workbook("result/chart_line.xlsx")
    # 创建一个sheet
    worksheet = workbook.add_worksheet()
    # 自定义样式，加粗
    bold = workbook.add_format({'bold': 1})
    # --------1、准备数据并写入excel---------------
    # 向excel中写入数据，建立图标时要用到
    headings = ['Version', '1.0.27', '1.0.29', '1.0.30', '1.0.31']
    data = [
        ['1', '-1', '-2', '-3', '-4', '-5'],
        [10, 40, 50, 20, 30, 50],
        [20, 60, 40, 10, 40, 30],
        [30, 40, 60, 10, 50, 10],
        [40, 30, 55, 15, 30, 30]
    ]
    # 写入表头
    worksheet.write_row('A1', headings, bold)
    # 写入数据
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3])
    worksheet.write_column('E2', data[4])
    # --------2、生成图表并插入到excel---------------
    # 创建一个柱状图(line chart)
    chart_col = workbook.add_chart({'type': 'line'})
    # 配置第1个系列数据
    chart_col.add_series({
        # 这里的Sheet1是默认的值
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$B$2:$B$7',
        'line': {'color': 'red'},
    })
    # 配置第2个系列数据
    chart_col.add_series({
        'name': '=Sheet1!$C$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$C$2:$C$7',
        'line': {'color': 'yellow'},
    })
    # 配置第二个系列数据
    chart_col.add_series({
        'name': '=Sheet1!$D$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$D$2:$D$7',
        'line': {'color': 'blue'},
    })
    # 配置第二个系列数据
    chart_col.add_series({
        'name': '=Sheet1!$E$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$E$2:$E$7',
        'line': {'color': 'green'},
    })
    # 设置图表的title 和 x，y轴信息
    chart_col.set_title({'name': 'The dll return Analysis'})
    chart_col.set_x_axis({'name': 'return value'})
    chart_col.set_y_axis({'name': 'count'})
    # 设置图表的风格
    chart_col.set_style(1)
    # 把图表插入到worksheet并设置偏移
    worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})
    # 关闭文件
    workbook.close()

def create_charts_column():
    # 创建一个excel
    workbook = xlsxwriter.Workbook("result/chart_column.xlsx")
    # 创建一个sheet
    worksheet = workbook.add_worksheet()

    # 自定义样式，加粗
    bold = workbook.add_format({'bold': 1})

    # --------1、准备数据并写入excel---------------
    headings = ['Version', '1.0.27', '1.0.29', '1.0.30', '1.0.31']
    data = [
        ['1', '-1', '-2', '-3', '-4', '-5'],
        [10, 40, 50, 20, 30, 50],
        [20, 60, 40, 10, 40, 30],
        [30, 40, 60, 10, 50, 10],
        [40, 30, 55, 15, 30, 30]
    ]

    # 写入表头
    worksheet.write_row('A1', headings, bold)

    # 写入数据
    worksheet.write_column('A2', data[0], bold)
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3])
    worksheet.write_column('E2', data[4])

    # --------2、生成图表并插入到excel---------------
    # 创建一个柱状图(column chart)
    chart_col = workbook.add_chart({'type': 'column'})

    # 配置第1个系列数据
    chart_col.add_series({
        # sheet1是默认的值
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$B$2:$B$7',
        'fill': {'color': 'red', 'transparency': 30},
    })

    # 配置第2个系列数据
    chart_col.add_series({
        'name': '=Sheet1!$C$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$C$2:$C$7',
        'fill': {'color': 'blue', 'transparency': 30},
    })

    # 配置第3个系列数据
    chart_col.add_series({
        'name': '=Sheet1!$D$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$D$2:$D$7',
        'fill': {'color': 'green', 'transparency': 30},
    })

    # 配置第4个系列数据
    chart_col.add_series({
        'name': '=Sheet1!$E$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$E$2:$E$7',
        'fill': {'color': 'yellow', 'transparency': 30},
    })

    # 设置图表的title 和 x，y轴信息
    chart_col.set_title({'name': 'The dll return Analysis'})
    chart_col.set_x_axis({'name': 'return value'})
    chart_col.set_y_axis({'name': 'count'})

    # 设置图表的风格
    chart_col.set_style(1)

    # 把图表插入到worksheet以及偏移
    worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})

    workbook.close()

def create_charts_pie():
    # 创建一个excel
    workbook = xlsxwriter.Workbook("result/chart_pie.xlsx")
    # 创建一个sheet
    worksheet = workbook.add_worksheet()

    # 自定义样式，加粗
    bold = workbook.add_format({'bold': 1})

    # --------1、准备数据并写入excel---------------
    # 向excel中写入数据，建立图标时要用到
    data = [
        ['1.0.27', '1.0.29', '1.0.30', '1.0.31'],
        [32, 23, 18, 25],
    ]

    # 写入数据
    worksheet.write_row('A1', data[0], bold)
    worksheet.write_row('A2', data[1])

    # --------2、生成图表并插入到excel---------------
    # 创建一个柱状图(pie chart)
    chart_col = workbook.add_chart({'type': 'pie'})

    # 配置第一个系列数据
    chart_col.add_series({
        'name': 'Bug Counts',
        'categories': '=Sheet1!$A$1:$D$1',
        'values': '=Sheet1!$A$2:$D$2',
        'points': [
            {'fill': {'color': '#BC3FBC'}},
            {'fill': {'color': '#0DAD48'}},
            {'fill': {'color': '#D8B31C'}},
            {'fill': {'color': 'gray'}},
        ],

    })

    # 设置图表的title 和 x，y轴信息
    chart_col.set_title({'name': 'Bug Counts'})

    # 设置图表的风格,excel内置48种图表样式
    chart_col.set_style(25)

    # 把图表插入到worksheet以及坐标位置
    worksheet.insert_chart('B10', chart_col, {'x_offset': 25, 'y_offset': 10})
    workbook.close()

# create_pie_charts()