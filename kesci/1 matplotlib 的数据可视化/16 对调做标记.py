from matplotlib import style
import matplotlib.pyplot as plt
style.use("tableau-colorblind10")
plt.plot([1, 2, 3], [5, 7, 4])

# 参数1是图画上写的内容，参数2 xy指的是在哪个店进行标注
# 参数3 xytext 是指插入文本的坐标
# 参数4 textcoords 是指
# 参数5 arrowprops ：dict，设置指向箭头的参数，字典中key值有①arrowstyle：设置箭头的样式，其value候选项如'->','|-|','-|>',也可以用字符串'simple','fancy'等，详情见顶部的官方项目地址链接。
plt.annotate('Bad News', xy=(2, 7), xytext=(1, 1), textcoords='axes fraction', arrowprops = dict(facecolor='grey'))
plt.savefig('16.png')
plt.show()