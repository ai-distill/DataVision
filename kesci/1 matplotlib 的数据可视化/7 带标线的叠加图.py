import matplotlib.pyplot as plt

# 绘制标线
plt.plot([], [], c='m', label='sleeping')
plt.plot([], [], c='c', label='eating')
plt.plot([], [], c='r', label='working')
plt.plot([], [], c='k', label='playing')

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.savefig('7.png')
plt.show()
