import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import sys

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
plt.xlabel("Ось x")
plt.ylabel('Ось y')
plt.plot(x, y)
if len(sys.argv) > 1 and sys.argv[1] == "yes":
    plt.fill_between(x, y, bottom, alpha=0.6)

plt.grid()
plt.show()
