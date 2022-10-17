import matplotlib.pyplot as plt
import numpy as np
data1 = [100, 90, 80, 60]
data2 = [90, 80, 70, 100]
labels = ['Math', 'English', 'Physics', 'Computer']
x=np.arange(len(labels))
names = ['Bill', 'Mary']

fig, ax = plt.subplots()
ax.bar(labels,data1, label='Bill')
ax.bar(labels,data2, bottom=data1, label='Mary')
ax.set_title("Stacked graph for scores")
ax.legend()
# ******************************
# Make your code
# ******************************


fig.savefig('A10.png')
plt.show()