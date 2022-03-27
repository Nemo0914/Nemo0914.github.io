

from pyecharts import options as opts
from pyecharts.charts import Bar, Line

v1 = [95,126,109,131,123,132,93,114,118,131,100,101,114,103]
v2 = [0,0.33,-0.13,0.20,-0.06,0.07,-0.30,0.23,0.04,0.11,-0.24,0.01,0.13,-0.10]

month_1=['12月1日','12月2日','12月3日','12月4日','12月5日','12月6日','12月7日','12月8日','12月9日','12月10日','12月11日','12月12日','12月13日','12月14日']


bar = (
    Bar()
    .add_xaxis(month_1)
    .add_yaxis("新增新冠患者", v1)
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value}"), interval=0.2, min_=-1, max_=1
        )
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国2021年12月1日-14日新增新冠患者人数及每日增速"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}"),min_=0, max_=400,interval=50)
    )
)

line = (
        Line()
        .add_xaxis(month_1)
        .add_yaxis("感染增速", v2, yaxis_index=1)# 使用的 y 轴的 index，在单个图表实例中存在多个 y 轴的时候有用
)

'''
bar = (
    Bar()
    .add_xaxis(Faker.months)
    .add_yaxis("新增新冠患者", v1)
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value}"), interval=5
        )
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Overlap-bar+line"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}")),
    )
)
'''
#line.overlap(bar)
#line.render()
bar.overlap(line)
bar.render("C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程/第一次作业/第四题/HW1-4.html")
