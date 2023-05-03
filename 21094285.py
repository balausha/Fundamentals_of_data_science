# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:40:32 2023

@author: Bala
"""

import numpy as np
import matplotlib.pyplot as plt

arr = np.genfromtxt('data5.csv', delimiter = ',')

x, y = np.histogram(arr, bins = 20)
x = np.append(x, 0)

# calculating the average weight of newborn babies in the given region
W = np.mean(y)

# finding X value
lower_range = 0.8 * W
upper_range = 1.2 * W

# Calculate the fraction of babies in the range
# the value X, which is the fraction of babies born weighting between 0.8  ̃W and 1.2  ̃W
num_babies_within_range = len([w for w in y if lower_range <= w <= upper_range])
X = num_babies_within_range / len(y)
X = np.round(X, 5)

#plot
plt.figure(figsize = (6, 4))
#bar plot
plt.bar(y, x, label = "33% of newborns are born with a weight above X")
#mean value
#plt.plot(W, 45, 'k--')
plt.plot([W, W], [0, np.max(x) + 0.002], 'k--', c = "black")
plt.text(3.33, 5, "Mean value is 3.3193", c = "black", fontsize = 10)
#X value
#plt.plot(x, 30, 'k--')
plt.text(3.90, 35, f"X value is {X}", c = "black", fontsize = 10)
#title, legends
plt.title("Distribution of new born in certain regions of Europe", fontsize = 10)
plt.xlabel("Weights of newborn babies (Distribution)", fontsize = 10)
plt.ylabel("Counts", fontsize = 10)
plt.savefig('plot.png', dpi = 300, bbox_inches = 'tight')
plt.show()
