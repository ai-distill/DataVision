from matplotlib import style
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y3 = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z3 = np.zeros(10)


# 长度
dx = np.ones(10)
# 宽度
dy = np.ones(10)
# 高度
dz = [1,2,3,4,5,6,7,8,9,10]
# 画图，前面3个是坐标，后面3个是描绘图像大小的
ax1.bar3d(x3, y3, z3, dx, dy, dz)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.savefig('22.png')
plt.show()
