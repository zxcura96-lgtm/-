
import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
x=[]
y=[]
z=[]
x1=[]
y1=[]
for i in np.arange(0,1.01,0.02):
    x.append(i)
    x1.append(str(i))
    y1.append(str(((6*i -2)**2)* np.sin(12*i - 4)))
    y.append(((6*i -2)**2)* np.sin(12*i - 4))
    z.append(str(i) + '  ' + str(y1))
plt.plot(x, y)
plt.xlabel("Ось x")
plt.ylabel('Ось y')
plt.grid()
plt.show()




root = ET.Element("data")


Ox = ET.SubElement(root, "xdata")

for x12 in x1:
    ox = ET.SubElement(Ox, "x")
    ox.text = str(x12)

Oy = ET.SubElement(root, "ydata")
for y12 in y1:
    oy = ET.SubElement(Oy, "y")
    oy.text = str(y12)

tree = ET.ElementTree(root)


tree.write("Выход 1.xml", encoding="utf-8", xml_declaration=True)
