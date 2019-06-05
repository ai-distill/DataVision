import matplotlib.animation
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['animation.html'] = 'jshtml'

t = np.linspace(0, 2 * np.pi)
print(t)

fig, ax = plt.subplots()
ax.axis([0,2*np.pi,-1,1])
l, = ax.plot([],[])


def animate(i):
    l.set_data(t[:i], x[:i])


matplotlib.animation.FuncAnimation(fig, animate, frames=len(t))
plt.show()