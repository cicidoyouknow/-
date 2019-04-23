import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy.optimize import curve_fit 

 
#2） 温度数据的曲线拟合
#最大值: 17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18
#最小值: -62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58
#绘制这些温度极值。
#定义一个函数，可以描述温度的最大值和最小值。提示：这个函数的周期是一年。提示：包含时间偏移。
#用scipy.optimize.curve_fit()拟合这个函数与数据。
#绘制结果。这个拟合合理吗？如果不合理，为什么？
#最低温度和最高温度的时间偏移是否与拟合一样精确？


month=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
Tmax=np.array([17,19,21,28,33,38,37,37,31,23,19,18])
Tmin=np.array([-62,-59,-56,-46,-32,-18,-9,-13,-25,-46,-52,-58])

def func2(time,A,k,theta,C):

    '''

    温度T对于时间t的函数:周期为k，omiga=2pi/k

    T=A*sin(omiga*time+theta)+C

    '''

    
    return A*np.sin(2*np.pi/k*time+theta)+C

p0=(8,12,-2,28)
p1=(10,12,-2,28)
popt1,pcov1=curve_fit(func2,month,Tmax,p0=p0)
popt2,pcov2=curve_fit(func2,month,Tmin,p0=p1)
print(popt1,popt2)
x=np.linspace(0,12,100)

plt.rcParams['font.family'] = ['Heiti']
plt.rcParams['font.sans-serif'] = ['Heiti'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
plt.plot(month,Tmax,label=u"real1")
plt.plot(month,Tmin,label=u"real2")
plt.plot(x,func2(x,*popt1),label=u"fit1")
plt.plot(x,func2(x,*popt2),label=u"fit2")
plt.legend()
plt.show()