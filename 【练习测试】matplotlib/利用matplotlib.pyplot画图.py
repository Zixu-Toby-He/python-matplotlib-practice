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

x=numpy.linspace(start=-10,stop=11,num=100)
y=x**2
matplotlib.pyplot.title("Test Painting")
matplotlib.pyplot.xlabel("x")
matplotlib.pyplot.ylabel("y")
matplotlib.pyplot.plot(x,numpy.sin(x),color="red")
matplotlib.pyplot.scatter(x,numpy.sin(x),color="red")
matplotlib.pyplot.plot(x,numpy.cos(x),color="green")
matplotlib.pyplot.scatter(x,numpy.cos(x),color="green")
matplotlib.pyplot.show()





input("请按回车继续")