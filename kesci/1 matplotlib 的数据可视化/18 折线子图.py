import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')
fig = plt.figure()


def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys


# 把图片分成两行两列的第一个位置
ax1 = fig.add_subplot(221)
p = create_plots()
ax1.plot(p[0], p[1])
# 把图片分成两行两列的第2个位置
ax2 = fig.add_subplot(222)
ax2.plot(p[0], p[1])
# 把图片分成两行一列的第二个位置
ax3 = fig.add_subplot(212) # 把图片分成两行一列的第二个位置
p = create_plots()
ax3.plot(p[0], p[1])

plt.savefig('18.png')
plt.show()