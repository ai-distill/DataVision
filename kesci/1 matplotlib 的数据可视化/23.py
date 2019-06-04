import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from matplotlib import style


style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data()
ax1.plot_wireframe(x,y,z, rstride = 20, cstride = 20) # 选择采样周期


ax1.set_xlabel('x asis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.savefig('23.png')
plt.show()