from collections import Counter
from os import path
import jieba
from pyecharts import Pie
from pyecharts import Bar
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS
import collections


def word_segment():
    jieba.load_userdict(path.join(path.dirname(__file__), 'userdict.txt'))  # 导入用户自定义词典
    STOPWORDS = open(path.join(path.dirname(__file__), 'stopwords.txt'), 'r', encoding='utf-8').read()  # 导入屏蔽词
    '''
    通过jieba进行分词并通过空格分隔,返回分词后的结果
    '''
    fw= open(path.join(path.dirname(__file__),'词频统计2.txt'),'w',encoding = 'utf-8')
    fl= open(path.join(path.dirname(__file__),'等级统计.txt'),'w',encoding = 'utf-8')
    text1 =open(path.join(path.dirname(__file__),'message.txt'),'r',encoding = 'utf-8').read().strip("\n").split(" ")
    textlevel=open(path.join(path.dirname(__file__),'level.txt'),'r',encoding = 'utf-8').readlines()
    # 计算每个词出现的频率，并存入txt文件
    text=' '.join(text1)
    jieba_word=jieba.cut(text,cut_all=False) # cut_all是分词模式，True是全模式，False是精准模式，默认False
    data=[]
    for word in jieba_word:
        if word not in STOPWORDS :
         data.append(word)
    dataDict=Counter(data)
    dataS=dataDict.most_common()[:50]
    for k,v in dict(dataS).items():
        print(k,v)
        fw.write("关键词: %s                      出现次数: %d\n" % (k,v))
    fw.close()
    dataS=dict(dataS)
    #print(dataS.keys())
    #print(dataS.values())
    #print(dataS)
    #fw.write("%s"%dataS)
    print("词频分析完成!\n")

    #等级统计
    leveldata=[]
    for word in textlevel:
        if word not in STOPWORDS :
         word.strip("\n")
         leveldata.append(word)
    levelDict=dict(Counter(leveldata))
    levelSort0= sorted(levelDict.keys())
    levelSort1=sorted(levelDict.items(),key=lambda x:x[0])
    print(levelSort0)
    print(levelSort1)

    for k,v in levelDict.items():
        fl.write("等级: %s                      出现次数: %d\n" % (k,v))
    fl.close()

    # 返回分词后的结果
    jieba_word=jieba.cut(text,cut_all=False) # cut_all是分词模式，True是全模式，False是精准模式，默认False
    seg_list=' '.join(jieba_word)

    #print(seg_list)
    #return seg_list
    columns=dataS.keys()
    data1=dataS.values()

    #data2=[]

    #设置主标题与副标题，标题设置居中，设置宽度为900
    pie = Pie("饼状图", "热点词汇",title_pos='down',width=900)
    #加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
    pie.add("热点词",columns, data1 ,center=[75,50],is_legend_show=False,is_label_show=True)
    #加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
    #pie.add("热点", columns, data2 ,center=[75,50],is_legend_show=False,is_label_show=True)
    #保存图表
    pie.render(path.join(path.dirname(__file__),'热点词汇饼状图.html'))

    level_columns=[]
    for v in levelDict:
        level_columns.append(v)
    for v in level_columns:
        v=v.replace("\n","")
    print(level_columns)
    level_data=list(levelDict.values())
    print(level_data)

    bar = Bar("柱状图", "发帖用户吧内等级")
    #添加柱状图的数据及配置项
    bar.add("等级", level_columns, level_data, mark_line=["average"], mark_point=["max", "min"])
    bar.render(path.join(path.dirname(__file__),'用户等级分布图.html'))

    # 词频统计
    word_counts = collections.Counter(data) # 对分词做词频统计
    word_counts_top20 = word_counts.most_common(20) # 获取前10最高频的词
    #print (word_counts_top20) # 输出检查

    d = path.dirname(__file__)
    mask = np.array(Image.open(path.join(d, "2_1.png")))

    wc = WordCloud(
        #设置字体，不指定就会出现乱码,这个字体文件需要下载
        font_path=r'C:/Windows/Fonts/STFANGSO.TTF',
        background_color="white",
        max_words=2000,
        mask=mask,
        max_font_size=100)
    # generate word cloud
    #wc.generate(','.join(data))
    #wc.generate(jieba_word)
    # store to file
    #wc.to_file(path.join(d, "qq_result.jpg"))

    # show
    wc.generate_from_frequencies(word_counts) # 从字典生成词云
    wc.to_file(path.join(d, "result2.jpg"))
    #image_colors = WordCloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
    #wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
    plt.imshow(wc) # 显示词云
    plt.axis('off') # 关闭坐标轴
    plt.show() # 显示图像


