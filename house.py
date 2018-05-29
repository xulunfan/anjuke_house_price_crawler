# -*- coding:utf-8 -*-
import sys
from pypinyin import pinyin, lazy_pinyin, Style
from bs4 import BeautifulSoup
import urllib2
import re
import warnings 
import os
import pandas as pd
os.environ['PYPINYIN_NO_PHRASES'] = 'true'
warnings.filterwarnings("ignore")

while 1:
    print "输入城市为：A 直辖市/地级市 B 县级市/区"
    city_type = raw_input()
    if city_type=='A':
        print "直辖市/地级市"
    elif city_type=='B':
        print "县级市/区"
    else:
        sys.exit()
        
    print "请输入直辖市/地级市名："
    raw_input_A = raw_input().decode(sys.stdin.encoding)
    if city_type=='B':
        print "请输入县级市/区名："
        raw_input_B = raw_input().decode(sys.stdin.encoding)
    #print(raw_input_A)
    #print raw_input_A
    #s=u'合肥'
    u=lazy_pinyin(raw_input_A)
    url='https://'
    for i in range(len(u)):
        url=url+u[i]
        
    url=url+'.anjuke.com/market/'
    if city_type=='B':
        u=lazy_pinyin(raw_input_B)
        for i in range(len(u)):
            url=url+u[i]
            
    def get_data_from_url(url):
        """ 下载来自url的数据 """
        headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',}
        req = urllib2.Request(url, None, headers)
        resp = urllib2.urlopen(req)
        return resp.read()
        
    try:
        soup = BeautifulSoup(get_data_from_url(url))
    except  urllib2.URLError, e:
        print "城市名解析错误"
        sys.exit()
    else:
        print "城市名解析成功"
    
    month=3
    for k in soup.find_all('h2'):
        for child in k.find_all('em'):
                 try:
                     print ("%d月房价：%s元"%(month,child.get_text().decode('utf-8').encode('gb18030')))
                 except UnicodeEncodeError:
                     sys.exit()
                 else:
                     pass
                 month=month-1
                 
    print "\n\n"
