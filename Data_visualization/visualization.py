import matplotlib.pyplot as plt #导入模块并设定一个别名

print(plt.style.available)
input_value=[1,2,3,4,5]
squares=[1,4,9,16,25]
#squares=[0,1,4,9,16,25]
plt.style.use('Solarize_Light2') #在subplots之前使用样式
fig,ax=plt.subplots() #subplots函数可以绘制一个或多个图表，返回两个对象：fig图形，ax轴（定位图表在图形中的位置）
ax.plot(squares,linewidth=3) #数据被绘制到轴对应的图表中
#设置图形标题并给坐标轴加上标签
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)
#设置标记刻度的大小
ax.tick_params(labelsize=14)

plt.show()