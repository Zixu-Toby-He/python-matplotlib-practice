import matplotlib
Params={"xtick.direction":"in"}
matplotlib.rcParams.update(Params)
print("修改完成")
print("matplotlib.rcParams[\"xtick.direction\"]=\""+matplotlib.rcParams["xtick.direction"]+"\"")
print("请重新打开另一个python进程查询matplotlib.rcParams[\"xtick.direction\"]")
input("按回车继续")
print("")
print("经试验，该修改不会影响下一次运行")
input("请按回车结束程序")