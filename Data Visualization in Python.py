import pandas as pd
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_values = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# # Line Plot
# plt.plot(x_values, y_values, color = "lightblue")
# plt.xlabel("x-axis placeholder")
# plt.ylabel("y-axis placeholder")
# plt.title("title placeholder")
# plt.show()
#
# # Scatter Plot
# plt.scatter(x_values, y_values, color = "darkblue")
# plt.xlabel("x-axis placeholder")
# plt.ylabel("y-axis placeholder")
# plt.title("title placeholder")
# plt.show()
#
# # Bar Chart
# cat = ["cat", "dog", "horse", "mouse"]
# cat_value = [10, 30, 100, 1]
#
#
# plt.bar(cat, cat_value, color = "forestgreen")
# plt.xlabel("Animals")
# plt.ylabel("Weight of an Animal")
# plt.title("Weight per Animal")
# plt.show()

# Histogram
# Histogram are useful for visualizing the distribution of numerical data
import numpy as np
x_normal = np.random.normal(0, 1, 100000)
plt.hist(x_normal, 50, facecolor = "lightblue", edgecolor = "black")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.title("Randomly Sampled Data from Standard Normal Distribution")
plt.show()

# Population Distribution
from scipy.stats import norm
x_values = np.arange(-4, 4, 0.01)
y_values = norm.pdf(x_values)
counts, bin, ignored = plt.hist(x_normal, 50, density = True, facecolor = "lightblue", edgecolor = "black", label = "Sampling Distribution")
plt.plot(x_values, y_values, color = "y", linewidth = 2.5, label = "Population Distribution")
plt.title("Randomly generating 1000 observation from Normal Distribution mu = o sigma = 1")
plt.ylabel("Probability")
plt.legend()
plt.show()

