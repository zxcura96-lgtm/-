import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

x = []
y = []

filename = "Выход 1.xml"

tree = ET.parse(filename)
root = tree.getroot()

xdata = root.find("xdata")
ydata = root.find("ydata")

for i in xdata.findall("x"):
    x.append(float(i.text))

for i in ydata.findall("y"):
    y.append(float(i.text))

bottom = min(y)

plt.plot(x, y)
plt.fill_between(x, y, bottom, alpha=0.6)

plt.grid()
plt.show()