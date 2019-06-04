import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('example.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

plt.plot(x, y, label='Loaded from file!')
plt.title('Interesting Graph\nCheck it out')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('9.png')
plt.show()
