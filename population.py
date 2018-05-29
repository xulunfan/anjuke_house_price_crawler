# -*- coding:utf-8 -*-
import urllib
import numpy as np
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from  matplotlib.animation import FuncAnimation
import pandas as pd
import seaborn as sns


# posi=pd.read_csv("D:\\Files\\datasets\\CitiesLatLon_China.csv")

posi=pd.read_excel("data/python-code/resources/Basemap/2015Cities-CHINA.xlsx")


lat = np.array(posi["lat"][0:120])                        # 获取维度之维度值
lon = np.array(posi["lon"][0:120])                        # 获取经度值
pop = np.array(posi["pop"][0:120],dtype=float)    # 获取人口数，转化为numpy浮点型
gdp = np.array(posi["GDP"][0:120],dtype=float)    # 获取人口数，转化为numpy浮点型

size=(pop/np.max(pop))*100    # 绘制散点图时图形的大小，如果之前pop不转换为浮点型会没有大小不一的效果

# size=(gdp/np.max(gdp))*100    # 绘制散点图时图形的大小，如果之前pop不转换为浮点型会没有大小不一的效果

map = Basemap(projection='stere', 
              lat_0=35, lon_0=110,
              llcrnrlon=82.33, 
              llcrnrlat=3.01, 
              urcrnrlon=138.16, 
              urcrnrlat=53.123,resolution='l',area_thresh=10000,rsphere=6371200.)


map.drawcoastlines()   
map.drawcountries()    
map.drawcounties()
map.readshapefile("data/python-code/resources/CHN_adm_shp/CHN_adm1",'states',drawbounds=True)
map.drawmapboundary()


parallels = np.arange(0.,90,10.) 
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线

meridians = np.arange(80.,140.,10.)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线


x,y = map(lon,lat)

# map.scatter(x,y,edgecolors='r',facecolors='r',marker='*',s=320)

map.scatter(x,y,s=size)

plt.title("Population Distribution in China")
plt.show()
