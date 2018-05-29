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
os.environ['PYPINYIN_NO_PHRASES'] = 'true'
warnings.filterwarnings("ignore")
table=pd.read_csv("data/cities.csv")
table=table[table['name']!='市辖区']
table=table[table['name']!='省直辖县级行政区划']
table=table[table['name']!='自治区直辖县级行政区划']

def DelLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)

tb=[]
for i in table.index:
    new_str=table['name'].loc[i]
    new_str=unicode(new_str,"utf-8")
    new_str=DelLastChar(new_str)
    if len(new_str)<=4:
        if len(new_str)>=2 and new_str[-1]!=u'\u5730':
            tb.append(new_str)


df2=pd.DataFrame({'City':[],'Mar':[],'Feb':[]})         
for i in range(len(tb)):
    #print tb[i]
    u=lazy_pinyin(tb[i])
    state=[]
    state.append(tb[i])
    url='https://'
    for i in range(len(u)):
        url=url+u[i]
        
    url=url+'.anjuke.com/market/'
            
    def get_data_from_url(url):
        """ 下载来自url的数据 """
        headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',}
        req = urllib2.Request(url, None, headers)
        resp = urllib2.urlopen(req)
        return resp.read()
        
    try:
        soup = BeautifulSoup(get_data_from_url(url))
    except  urllib2.URLError, e:
        pass
    else:
        pass
    
    month=3

    for k in soup.find_all('h2'):
        for child in k.find_all('em'):
                 try:
                     price=child.get_text().decode('utf-8').encode('gb18030')
                     if len(state)==1:
                         state.append(price)
                                  
                     else:
                         state.append(price)
                 except UnicodeEncodeError:
                     pass
                 else:
                     pass
                 month=month-1
     
    if len(state)!=3:
        state.append("-1")
        state.append("-1")
         
    df2=df2.append(pd.DataFrame([state],columns=['City','Mar','Feb']))            
    #print "\n\n" 
       
df2=df2.set_index('City')
df2.to_json('result/price.json')

