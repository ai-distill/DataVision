
# 正确代码



'''

import matplotlib.pyplot as plt
from matplotlib import style
# 导入这行代码防止出现 ValueError: Unknown projection '3d'
from mpl_toolkits.mplot3d import axes3d

style.use('fivethirtyeight')

# 新建一个画图窗口
fig = plt.figure()
# 参数111的意思是把画布分成1行1列，其中图画在第1块
ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]

ax1.plot(x, y, z)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
'''


import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]

ax1.plot(x, y, z)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.savefig('20.png')
plt.show()