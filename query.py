# -*- coding:utf-8 -*-
import sys
from pypinyin import pinyin, lazy_pinyin, Style
from bs4 import BeautifulSoup
import urllib2
import re
import warnings 
import os
import pandas as pd
import string
from sklearn.cluster import KMeans

os.environ['PYPINYIN_NO_PHRASES'] = 'true'
warnings.filterwarnings("ignore")
dd=pd.read_json('result/price.json')
#dd.to_csv('result/price.csv', sep=';', header=True, index=True)
#df=pd.read_csv("result/price.csv",sep=";",names=['City','Feb','Mar'])
#df=df[1:]
dd[dd['Feb']>dd[dd.index==u'绵阳'].Feb.values[0]]#房价比绵阳高的城市
dd.insert(2,'Increment',dd['Mar']-dd['Feb'])#增量
rate=(dd['Mar']-dd['Feb'])/(dd['Feb'])
#KMeans
dataset=dd.as_matrix()
kmeans = KMeans(n_clusters=4, random_state=0).fit(dataset)  
center = kmeans.cluster_centers_
df_center = pd.DataFrame(center, columns=['Feb', 'Mar','Increment'])
labels = kmeans.labels_


dd.insert(3,'Speedup',list(map(lambda i:format(rate[i], '.3%'),range(rate.size))))#增速
dd[dd['Speedup']==max(dd['Speedup'])]#增速最快
dd[dd['Mar']>10000].index.size#房价破万
dd[dd['Mar']<4000]#低于四千

dd.insert(4,'Labels',labels)#增量
df1=dd[dd.Labels==0]
df2=dd[dd.Labels==1]
df3=dd[dd.Labels==2]
df4=dd[dd.Labels==3]

#绘图  
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8), dpi=80)  
axes = plt.subplot()  
#s表示点大小，c表示color，marker表示点类型，DataFrame数据列引用参考博客其他文章  
type1 = axes.scatter(df1.loc[:,['Feb']], df1.loc[:,['Mar']], s=50, c='red', marker='d')  
type2 = axes.scatter(df2.loc[:,['Feb']], df2.loc[:,['Mar']], s=50, c='green', marker='*')  
type3 = axes.scatter(df3.loc[:,['Feb']], df3.loc[:,['Mar']], s=50, c='brown', marker='p')  
type4 = axes.scatter(df4.loc[:,['Feb']], df4.loc[:,['Mar']], s=50, c='black')  
#显示聚类中心数据点  
type_center = axes.scatter(df_center.loc[:,'Feb'], df_center.loc[:,'Mar'], s=40, c='blue')  
plt.xlabel('x', fontsize=16)  
plt.ylabel('y', fontsize=16)  
axes.legend((type1, type2, type3, type4, type_center), ('0','1','2','3','center'), loc=1)  
plt.show()  
