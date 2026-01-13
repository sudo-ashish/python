import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

x = [1,2,3,4,5,6,7]
y = [1,2,3,4,5,6,7]

plt.scatter(x, y, c='red', edgecolors='black', alpha=0.7)

plt.show()