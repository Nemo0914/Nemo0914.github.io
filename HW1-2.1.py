
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts.globals import ChartType


txt_filename = 'C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程/第一次作业/第二题/Book1.csv'

txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()
print('文件读取完成\n',content)

a_list = content


print('第一部分完成')
c = (
    Geo()
    .add_schema(maptype="china")
    .add(
        "全国新冠患者累计人数",
         [("福建省", 513),("陕西省", 507),
         ('江苏省',684),
         ('四川省',853),
         ('山东省',862),
         ('江西省',935),
         ('黑龙江省',964),
         ('新疆',980),
         ('安徽省',993),
         ('湖南省',1021),
         ('河南省',1299),
         ('浙江省',1306),
         ('湖北省',68149),
         ('广东省',2046),
         ('海南省',171),
         ('台湾省',799),
         ('西藏',1),
         ('青海省',18),
         ('宁夏回族自治区',75),
         ('贵州省',147),
         ('吉林省',157),
         ('甘肃省',182),
         ('云南省',230),
         ('山西省',224),
         ('广西',264),
         ('辽宁省',351),
         ('内蒙古自治区',364),
         ('河北省',373)],
        type_=ChartType.HEATMAP,
        
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color,min_=0,max_=1000,split_number=100), 
        title_opts=opts.TitleOpts(title="2020年12月31日全国新冠累计患者情况")
    )
    .render("C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程/第一次作业/第二题/HW1-2.1.html")
    )

print('第二部分完成')