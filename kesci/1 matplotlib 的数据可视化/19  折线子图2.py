import matplotlib.pyplot as plt
from matplotlib import style
plt.plot([1,2,3])
plt.show()


p1 = plt.subplot(211)
p1.plot(range(12))
# sharex 设置x轴对齐
p2 = plt.subplot(212, sharex=p1)
p2.plot(range(20))
# 把图片的 x 轴去掉
plt.setp(p1.get_xticklabels(), visible=False)
plt.savefig('19.png')
plt.show()