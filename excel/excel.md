## python excel, xlrd, xlwt
```
要解析 Excel 文件，需要用第三方的包 读excel使用xlrd、写excel需要xlwt
pip install xlrd 
pip install xlwt
```
## pyecharts
```
pip install pyecharts
```
- 错误
```
PendingDeprecationWarning: pyecharts 所有图表类型将在 v1.9.0 版本开始强制使用 ChartItem 进行数据项配置 
解决方法：需要去pyecharts的按照包下面找到文件globals.py，把ShowWarning改成False
class _WarningControl:
    ShowWarning = False
```
## jupyter
```
1. 安装jupyter
pip install jupyter
2. 配置jupyter
jupyter notebook --generate-config --allow-root  # 生成jupyter配置文件
3. 为jupyter设置密码
在终端中键入python回车后输入如下代码后回车
回车后会显示一串sha1加密的密码，后面会用到这个密码，需要保存
from notebook.auth import passwd 
passwd()
4. 修改jupyter配置文件
jupyter配置文件位置：
Linux下：vim /root/.jupyter/jupyter_notebook_config.py
Windows下：C:\Users\xxx\.jupyter\jupyter_notebook_config.py

c.NotebookApp.allow_password_change = False
c.NotebookApp.allow_remote_access = True
c.NotebookApp.allow_root = True
c.NotebookApp.ip = '*'
c.NotebookApp.notebook_dir = '这里填文档保存的路径'
c.NotebookApp.open_browser = False
c.NotebookApp.password = '这里填刚刚生成的密码'

5. 启动jupyter
linux下启动，在启动之前要设置防火墙规则对其放行，这里不建议彻底关闭防火墙，但是SELinux建议将其关闭
    nohup jupyter notebook --allow-root >/root/jupyter.logfile 2>&1 &
    或者
    nohup jupyter notebook --port 80 --allow-root --ip 192.168.1.184 --no-browser &
确认：如果8888端口正在监听，则表示jupyter启动成功
    ss -tnlp | grep 8888
windows下启动
    jupyter notebook
    jupyter notebook  --no-browser

6.访问
默认的监听端口是8888
浏览器访问：http://IP地址:8888 
```

## jupyter pyecharts
```
1. 安装基础库
pip install html5lib
pip install pyecharts
pip install matplotlib
2. 安装主题
pip install echarts-themes-pypkg
3. 代码可以在jupyter上面执行，就可以直接输出图片
```
## python excel xlsxwriter
- 不支持读取和修改
- 不支持XLS文件
- 暂时不支持透视表（Pivot Table）
- [xlsxwriter](https://xlsxwriter.readthedocs.io/chart_examples.html)


## python excel openpyxl
```
1. 安装openpyxl库
pip install openpyxl
```
### openpyxl常用属性函数

| 常用函数或者属性                           | 说明                         |
| :----------------------------------------- | :--------------------------- |
| openpyxl.load_workbook()                   | 加载excel工作本              |
| Workbook.active                            | 获得默认sheet                |
| Workbook.create_sheet()                    | 创建sheet                    |
| Workbook.get_sheet_names()                 | 已过时, 获得所有sheet名称    |
| workbook.sheetnames                        | 获得所有sheet名称            |
| workbook.get_sheet_by_name(name)           | 已过时获得指定的sheet对象    |
| workbook[sheetname]                        | 获得指定的sheet对象          |
| workbook.copy_worksheet(soure)             | 复制sheet                    |
| sheet[cell]                                | 获取单个单元格               |
| sheet.cell(self, row, column, value=None)  | 获取单个单元格               |
| sheet[cell,cell]                           | 访问多个单元格               |
| sheet.iter_rows(min_row, max_col, max_row) | 返回多行，用于访问多个单元格 |
| sheet.iter_cols(min_row, max_col, max_row) | 返回多列，用于访问多个单元格 |
| sheet.rows                                 | 获取所有行                   |
| sheet.columns                              | 获取所有列                   |
| cell.value                                 | 获取属性值                   |
| sheet.merge_cells()                        | 合并单元格                   |
| sheet.unmerge_cells()                      | 取消合并单元格               |