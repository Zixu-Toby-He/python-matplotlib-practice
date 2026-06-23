import numpy
import matplotlib
import matplotlib.pyplot

params = {
	'backend': 'ps',
#	'font.size': 30,
#	'font.style': 'normal',
#	'axes.labelsize': 10,
#	'axes.linewidth': 2,
	'legend.fontsize': 12,
#	'xtick.labelsize': 30,
#	'ytick.labelsize': 30,
	'xtick.direction': 'in',
	'ytick.direction': 'in',
	'xtick.top': True,
	'ytick.right': True,
	'ps.usedistiller': 'xpdf'
	}
matplotlib.rcParams.update(params)

def 绘制(x,y,颜色):
	matplotlib.pyplot.plot(x,y,color=颜色)
	matplotlib.pyplot.scatter(x,y,color=颜色)

x=numpy.linspace(start=-10,stop=11,num=100)
y=x**2
matplotlib.pyplot.title("Test Painting")
matplotlib.pyplot.xlabel("x")
matplotlib.pyplot.ylabel("y")
绘制(x=x,y=numpy.sin(x),颜色="red")
绘制(x=x,y=numpy.cos(x),颜色="green")
matplotlib.pyplot.show()

input("请按回车继续")