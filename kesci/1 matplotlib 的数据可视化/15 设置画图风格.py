from matplotlib import style
import matplotlib.pyplot as plt

# 可以设置画图风格，并且查看可用的style
print(style.available)

# 设置奇怪的风格
style.use('tableau-colorblind10')
plt.plot([1, 2, 3], [5, 7, 4])
plt.savefig('15.png')
plt.show()
