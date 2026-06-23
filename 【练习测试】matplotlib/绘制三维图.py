import numpy
import matplotlib.pyplot

def main_1():
	a = numpy.linspace(-1,1,101)
	b = a
	_a,_b = numpy.meshgrid(a,b)
	e = numpy.exp(-(_a*_a+_b*_b))
	
	fig = matplotlib.pyplot.figure(figsize = (6,6))
	ax  = fig.add_subplot(projection = "3d")
	绘图 = ax.plot_surface(_a,_b,e,cmap = matplotlib.pyplot.get_cmap("rainbow"))
	matplotlib.pyplot.colorbar(绘图, shrink = 0.5)
	matplotlib.pyplot.show()

def main_2():
	a = numpy.linspace(-1,1,101)
	b = a
	_a,_b = numpy.meshgrid(a,b)
	e = numpy.exp(-(_a*_a+_b*_b))

	import mpl_toolkits.mplot3d
	fig = matplotlib.pyplot.figure(figsize=(6,6))
	ax  = mpl_toolkits.mplot3d.Axes3D(fig)
	绘图 = ax.plot_surface(
		X = _a,
		Y = _b,
		Z = e,
		cmap = matplotlib.pyplot.get_cmap("rainbow")
		)
	matplotlib.pyplot.colorbar(绘图, shrink = 0.5)
	matplotlib.pyplot.show()
	
	

if (__name__ == "__main__"):
	main_1()
	#main_2()
