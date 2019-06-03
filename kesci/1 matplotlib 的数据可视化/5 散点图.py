import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]
# s 是标记大小，以平方磅为单位的标记面积
# marker 标记点的样式 o是圆圈
# color 是颜色， k是指black
plt.scatter(x, y, label='skitscat', color='k', s=25, marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.savefig('5.png')
plt.show()
