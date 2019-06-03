import matplotlib.pyplot as plt
plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label='Example One')
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label='Example Two', color='g')
plt.title('Epic Graph\nAnother Line Whoa')
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.legend()
plt.savefig('3.png')
plt.show()