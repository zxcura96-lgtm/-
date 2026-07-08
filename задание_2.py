import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    D = 2
    return -20 * np.exp(-0.02 * np.sqrt((x1**2 + x2**2) / D)) \
           - np.exp((np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2)) / D)


x1_min, x1_max = -5, 5
x2_min, x2_max = -5, 5

x10 = 0
x20 = 0

x1 = np.linspace(x1_min, x1_max, 200)
x2 = np.linspace(x2_min, x2_max, 200)

X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)

z0 = f(x10, x20)

fig = plt.figure(figsize=(10, 6))

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_surface(X1, X2, Z,  cmap='viridis')


ax2 = fig.add_subplot(2, 2, 2)
contour = ax2.contour(X1, X2, Z, levels=30)
ax2.grid()

ax3 = fig.add_subplot(2, 2, 3)
Y1 = f(x1, x20)
ax3.plot(x1, Y1)
ax3.grid()

ax4 = fig.add_subplot(2, 2, 4)
Y2 = f(x10, x2)
ax4.plot(x2, Y2)
ax4.grid()


plt.tight_layout()
plt.show()