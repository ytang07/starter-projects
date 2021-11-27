import matplotlib.pyplot as plt
import random

samples = 100
x = [random.randint(0, 10) for _ in range(samples)]
y = [random.randint(0, 10) for _ in range(samples)]

plt.scatter(x, y)
plt.title("Randomized Data Points between 0 and 10")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()