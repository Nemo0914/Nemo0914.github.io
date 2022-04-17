# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:35:16 2022

@author: 86153
"""


import jieba
import jieba.posseg as pseg

##--- 第0步：准备工作，重要变量的声明

# 输入文件
txt_file_name = 'C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程（交作业）/作业2/网页3/《机动战士GUNDAM》.txt'
# 输出文件
node_file_name = 'C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程（交作业）/作业2/网页3/高达人物节点.csv'
link_file_name = 'C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程（交作业）/作业2/网页3/高达人物连接.csv'

# 运行时，经常出现目标文件被打开，导致写文件失败
# 可以提前测试打开，这样可以很大程度避免问题，但更好的方式是用异常处理机制
test = open(node_file_name, 'w')
test.close()
test = open(link_file_name, 'w')
test.close()

# 打开文件，读入文字
txt_file = open(txt_file_name, 'r', encoding='utf-8')
line_list = txt_file.readlines()
txt_file.close()
#print(line_list)  # 测试点

# 加载用户字典
jieba.load_userdict('C:/Users/86153/Desktop/Courses/北京大学选课/计算机编程（交作业）/作业2/网页3/Gundamuser.txt')


##--- 第1步：生成基础数据（一个列表，一个字典）
line_name_list = []  # 每个段落出现的人物列表
name_cnt_dict = {}  # 统计人物出现次数

# ！！设置忽略词的列表
ignore_list = ['白色基地','吉翁','萨克','加农','艾尔','明白','艾尔美斯',
               '雷射','里克·德姆','德姆','士官长','米诺夫斯基','米诺','马哈尔','阿兹'
               ,'马可','吉翁军','小姐','布劳·布罗','布劳','布罗','来福枪','吉翁·戴肯','戴肯']

print('正在分段统计……')
print('已处理词数：')
progress = 0  # 用于计算进度条
for line in line_list: # 逐个段落循环处理
    word_gen = pseg.cut(line) # peseg.cut返回分词结果，“生成器”类型
    line_name_list.append([])
    
    for one in word_gen:
        word = one.word
        flag = one.flag
        
        if word in ignore_list:  # 跳过标记忽略的人名 
            continue
        
 # 对指代同一人物的名词进行合并
        if word == '阿姆罗':
            word = '阿姆罗·雷'
        elif word == '夏亚' or word =='夏亚中校' or word =='凯斯柏·雷姆·戴肯':
            word = '夏亚·阿兹纳布' 
        elif word == '龙'or word =='龙·何赛' or word =='何赛':
            word = '龙·何赛·荷西' 
        elif word == '隼人':
            word = '小林隼人'
        elif word == '凯'or word =='西汀':
            word = '凯·西汀'  
        elif word == '拉拉':
            word = '拉拉·丝'
        elif word == '布莱德' or word =='布莱德舰长' :
            word = '布莱德·诺亚'
        elif word == '艾儿':
            word = '库丝可·艾儿'
        elif word == '基西莉亚':
            word = '基西莉亚·查比'           
        elif word == '米莱'or word =='米莱中尉': 
            word = '米莱·矢岛'  
        elif word == '夏里亚'or word =='布尔': 
            word = '夏里亚·布尔'            
        elif word == '莎拉'or word =='莎拉·玛斯'or word =='阿尔蒂西亚'or word =='阿尔蒂': 
            word = '阿尔蒂西亚·索姆·戴肯'            
        elif word == '鲁洛依'or word =='基里安': 
            word = '鲁洛依·基里安'   
        elif word == '史雷格'or word =='罗伍':
            word = '史雷格·罗伍' 
        elif word == '卡尔马': 
            word = '卡尔马·查比' 
        elif word == '弗拉纳罕博士': 
            word = '弗拉纳罕' 
        elif word == '兰巴'or word =='拉尔': 
            word = '兰巴·拉尔'
        elif word == '迪尼中尉': 
            word = '迪尼'    
        elif word == '查普曼': 
            word = '查普曼·吉洛姆'
        elif word == '基连'or word =='基连总帅': 
            word = '基连·查比'
        elif word == '马可': 
            word = '马可贝里'            
            
            
        if len(word) == 1:  # 跳过单字词
                continue
            
        if flag == 'nr': 
            line_name_list[-1].append(word)
            if word in name_cnt_dict.keys():
                name_cnt_dict[word] = name_cnt_dict[word] + 1
            else:
                name_cnt_dict[word] = 1
        
        # 因为词性分析耗时很长，所以需要打印进度条，以免用户误以为死机了
        progress = progress + 1
        progress_quo = int(progress/1000)
        progress_mod = progress % 1000 # 取模，即做除法得到的余数
        if progress_mod == 0: # 每逢整千的数，打印一次进度
            #print('---已处理词数（千）：' + str(progress_quo))
            print('\r' + '-'*progress_quo + '> '\
                  + str(progress_quo) + '千', end='')
# 循环结束点        
print()
print('基础数据处理完成')
#print(line_name_list)  # 测试点
#print('-'*20)
#print(name_cnt_dict)  # 测试点


##--- 第2步：用字典统计人名“共现”数量（relation_dict）
relation_dict = {}

# 只统计出现次数达到限制数的人名
name_cnt_limit = 30 

for line_name in line_name_list:
    for name1 in line_name:
        # 判断该人物name1是否在字典中
        if name1 in relation_dict.keys():
            pass  # 如果已经在字典中，继续后面的统计工作
        elif name_cnt_dict[name1] >= name_cnt_limit:  # 只统计出现较多的人物
            relation_dict[name1] = {}  # 添加到字典
            #print('add ' + name1)  # 测试点
        else:  # 跳过出现次数较少的人物
            continue
        
        # 统计name1与本段的所有人名（除了name1自身）的共现数量
        for name2 in line_name:
            if name2 == name1 or name_cnt_dict[name2] < name_cnt_limit:  
            # 不统计name1自身；不统计出现较少的人物
                continue
            
            if name2 in relation_dict[name1].keys():
                relation_dict[name1][name2] = relation_dict[name1][name2] + 1
            else:
                relation_dict[name1][name2] = 1

print('共现统计完成，仅统计出现次数达到' + str(name_cnt_limit) + '及以上的人物')

##--- 第3步：输出统计结果
#for k,v in relation_dict.items():  # 测试点
#    print(k, ':', v)

# 字典转成列表，按出现次数排序
item_list = list(name_cnt_dict.items())
item_list.sort(key=lambda x:x[1],reverse=True)

## 导出节点文件
node_file = open(node_file_name, 'w') 
# 节点文件，格式：Name,Weight -> 人名,出现次数
node_file.write('Name,Weight\n')
node_cnt = 0  # 累计写入文件的节点数量
for name,cnt in item_list: 
    if cnt >= name_cnt_limit:  # 只输出出现较多的人物
        node_file.write(name + ',' + str(cnt) + '\n')
        node_cnt = node_cnt + 1
node_file.close()
print('人物数量：' + str(node_cnt))
print('已写入文件：' + node_file_name)

## 导出连接文件
# 共现数可以看做是连接的权重，只导出权重达到限制数的连接
link_cnt_limit = 5 
print('只导出数量达到' + str(link_cnt_limit) + '及以上的连接')

link_file = open(link_file_name, 'w')
# 连接文件，格式：Source,Target,Weight -> 人名1,人名2,共现数量
link_file.write('Source,Target,Weight\n')
link_cnt = 0  # 累计写入文件的连接数量
for name1,link_dict in relation_dict.items():
    for name2,link in link_dict.items():
        if link >= link_cnt_limit:  # 只输出权重较大的连接
            link_file.write(name1 + ',' + name2 + ',' + str(link) + '\n')
            link_cnt = link_cnt + 1
link_file.close()
print('连接数量：' + str(link_cnt))
print('已写入文件：' + link_file_name)      
