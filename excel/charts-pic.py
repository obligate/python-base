# _*_ coding: utf-8 _*_
# @Time     : 2020/10/29 10:56
# @Author   : Peter
# @File     : charts-pic.py

# 需要安装 pip install snapshot-selenium
# chrome://version/  查看chrome版本，下载对应的chromedriver驱动，下载路径 http://chromedriver.chromium.org/downloads
# 需要下载 chromedriver.exe， 把 chromedriver.exe 放入存放着 python.exe的目录中
from snapshot_selenium import snapshot as driver

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot


def bar_chart() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
            .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c


make_snapshot(driver, bar_chart().render(), "bar.png")  # 会在当前目录生成一个bar.png文件
