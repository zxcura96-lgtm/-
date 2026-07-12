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
print('Закрасить область под графиком? ДА - 1; НЕТ - 0')
t=int(input())
if t == 1:
    plt.fill_between(x, y, bottom, alpha=0.6)
    plt.grid()
    plt.show()
else:
    plt.grid()
    plt.show()
