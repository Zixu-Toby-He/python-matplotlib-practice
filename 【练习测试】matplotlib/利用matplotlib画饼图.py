import numpy
import matplotlib
import matplotlib.pyplot

matplotlib.pyplot.rcParams["font.sans-serif"]=["SimHei"]
标题=["暗能量","暗物质","重子物质"]
比例=[0.6911,0.2589,0.0486]
matplotlib.pyplot.pie(比例,labels=标题)
matplotlib.pyplot.savefig("ΛCDM模型.jpg")
matplotlib.pyplot.show()

input("请按回车继续")