import matplotlib.pyplot as plt #导入模块并设定一个别名
from random_walk import RandomWalk


#只要程序处于活动状态，就不断地模拟随机游走
while True:

    #创建一个RandomWalk实例
    rw=RandomWalk(50000)
    rw.fill_walk() #调用fill_walk函数

    #将所有的点都绘制出来
    plt.style.use('Solarize_Light2') #在subplots之前使用样式
    fig,ax=plt.subplots(figsize=(15,9)) #subplots函数可以绘制一个或多个图表，返回两个对象：fig图形，ax轴（定位图表在图形中的位置）
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.plasma,
               edgecolors='none',s=1)
    #突出起点和终点
    ax.scatter(0,0,c='lime',edgecolors='none',s=25)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='white',edgecolors='none',s=25)
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')
    plt.show()

    keep_running=input("Make another walk?(y/n):")
    if keep_running=='n':
        break

"""Matplotlib 内置了 140+ 种标准颜色名称，包括常见颜色和一些小众颜色，以下是高频使用的：
基础色（10 种核心）：red、blue、green、yellow、black、white、gray、orange、purple、brown；
柔和色（常用）：coral、pink、cyan（青）、magenta（品红）、lime（酸橙绿）、navy（藏青）、teal（青绿色）、salmon（三文鱼色）；
灰度色：lightgray（浅灰）、darkgray（深灰）、silver（银灰）、snow（雪白）"""

"""格式：#RRGGBB 或 #RRGGBBAA（AA 控制透明度，00 = 全透明，FF = 不透明），
   #其中 RR、GG、BB 是 00-FF 的十六进制数（对应 0-255 的十进制）。"""

"""格式：(r, g, b) 或 (r, g, b, a)，其中 r、g、b、a 的值是 0-1 之间的浮点数（0 = 无该颜色，1 = 最大浓度）。

1. 常用渐变色（Sequential）—— 数值从低到高，颜色渐变（最常用）
适合展示「有大小顺序」的数据（比如成绩、温度、浓度），颜色从浅到深 / 从暗到亮过渡：
基础款（高频使用）：
viridis（默认，蓝→绿→黄，视觉友好，适合科研论文）
plasma（紫→粉→黄，鲜艳）
Reds（浅红→深红，你想要的「salmon 类似色系」可以用这个）
Blues（浅蓝→深蓝）
Greens（浅绿→深绿）
Oranges（浅橙→深橙，和 salmon 色系接近）
YlOrRd（黄→橙→红，暖色调）
其他实用款：
GnBu（绿→蓝）、PuRd（紫→红）、BuPu（蓝→紫）
2. 双向渐变色（Diverging）—— 中间是中性色，两端是对比色
适合展示「有中间基准」的数据（比如温度高于 / 低于 0℃、成绩高于 / 低于平均分）：
常用：
coolwarm（蓝→白→红，冷→热对比）
RdBu（红→白→蓝，反向对比）
RdYlGn（红→黄→绿，比如正负数、及格 / 不及格）
3. 分类色（Qualitative）—— 无顺序，颜色互不关联
适合展示「无大小关系的类别数据」（比如不同班级、不同性别、不同类别），每个类别用不同颜色：
常用：
tab10（10 种颜色循环，默认分类色，适合多类别）
tab20（20 种颜色循环，适合更多类别）
Set3（柔和的分类色，不刺眼）
4. 特殊用途色（Miscellaneous）—— 自定义或特殊场景
gray（灰度渐变，黑→白）
pink（粉色渐变，浅粉→深粉，接近 salmon 柔和感）
magma（黑→红→黄，高对比度）"""