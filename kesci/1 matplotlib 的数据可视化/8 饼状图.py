import matplotlib.pyplot as plt

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

# 参数说明：
# startangle 开始的角度，最开始是在正右方
# explode=(0,0.1,0,0) 每个部分突出的部分
# autopct='%1.1f%%') # 百分比的格式
plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow=True, explode=(0,0.1,0,0), autopct='%1.1f%%')
plt.title('Interesting Graph\nCheck it out')
plt.savefig('8.png')
plt.show()
