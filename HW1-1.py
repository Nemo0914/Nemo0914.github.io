
print('------------------------第一部分------------------------------')

import jieba
import jieba.posseg as pseg
txt_filename = 'C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程/第一次作业/第一题/作业文本.txt'
result_filename = 'C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程/第一次作业/第一题/作业词频统计.csv'
#文件命名和路径

# 从文件读取文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()
print('文件读取完成')

# 添加自定义字典
#jieba.load_userdict('./data/userdict_pseg.txt')

# 分词
words = pseg.cut(content) # peseg.cut返回生成器
print('分词完成')

# 用字典统计每个人物名词的出现次数
word_dict = {}
print('正在统计所有词中的名词……')
count = 0 # 用于记录已处理的名词数
for one in words: 
    # 为便于处理，用w记录本次循环检查的“词”，f记录对应的“词性”
    w = one.word 
    f = one.flag 
    
    if len(w) == 1:  # 忽略单字
        continue
    
    # 对指代同一事物的名词进行合并
    if w == '会计专业':
        w = '会计学'
    else:
        pass # pass表示“什么都不做”
    
    if 'n' in f: # 如果该词的词性中包含'n'，即这是个人物名词，……
        if w in word_dict.keys(): # 如果该词已经在词典中，……
            word_dict[w] = word_dict[w] + 1
        else: # 如果该词不在词典中，……
            word_dict[w] = 1

    
# 循环结束点

print()
print('名词统计完成')

## 经过词性筛选，不合要求的词应该大大减少了
## 如果需要，还可以在这里删除不想统计的词
#ignore_list = []
#for w in ignore_list:
#    del word_dict[w]
          
# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x:x[1], reverse=True)
print('排序完成')

# 根据用户需求，打印排名前列的词，同时把统计结果存入文件
total_num = len(items_list)
print('共有' + str(total_num) + '个可能的名词。')
num = input('您想查看前多少个名词？[10]:')
if not num.isdigit() or num == '':
    num = 10
else:
    num = int(num)

if num > total_num:
    num = total_num

result_file = open(result_filename, 'w')   
result_file.write('名词,出现次数\n')
for i in range(num):
    word, cnt = items_list[i]
    message = str(i+1) + '. ' + word + '\t' + str(cnt)
    print(message)
    result_file.write(word + ',' + str(cnt) + '\n')
result_file.close()

print('已写入文件：' + result_filename)

print('------------------------第三部分------------------------------')

#词云
from pyecharts.charts import WordCloud
from pyecharts import options as opts

##-------从文件中读出人物词频------------------
src_filename = 'C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程/第一次作业/第一题/作业词频统计.csv'
# 格式：人物,出现次数

src_file = open(src_filename, 'r')
line_list = src_file.readlines()  #返回列表，文件中的一行是一个元素
src_file.close()

print(line_list)  # 检查读入数据的情况

# 将读入的每行数据拆分成元组
wordfreq_list = []  #用于保存元组(词语,出现次数)
for line in line_list:
    line = line.strip()  #删除'\n'
    line_split = line.split(',') # 以逗号作为标志，把字符串切分成词，存在列表中
    wordfreq_list.append((line_split[0],line_split[1]))

print(wordfreq_list)

print('------------------------第四部分------------------------------')

del wordfreq_list[0] #删除csv文件中的标题行
##-------从文件中读出人物词频完成------------------

##===============================================
##-------生成词云---------------------------------
cloud = WordCloud() # 初始化词云对象

# 设置词云图
cloud.add('', 
          wordfreq_list[0:617], #元组列表，词和词频
          shape='star', # 轮廓形状：'circle','cardioid','diamond',
                           # 'triangle-forward','triangle','pentagon','star'
#          mask_image='./data/词云背景图-中国.jpg', # 轮廓图，第一次显示可能有问题，刷新即可’
          is_draw_out_of_bound=False, #允许词云超出画布边界
          word_size_range=[30, 100], #字体大小范围
          textstyle_opts=opts.TextStyleOpts(font_family="微软雅黑"),
          #字体：例如，微软雅黑，宋体，华文行楷，Arial
          )

# render会生成HTML文件。默认是当前目录render.html，也可以指定文件名参数
out_filename = 'C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程/第一次作业/第一题/HW1-1.html'
cloud.render(out_filename)

print('生成结果文件：' + out_filename)



    






           
           
       
