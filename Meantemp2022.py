# Making Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Preprocessing Input data
data = pd.read_csv('temp2022.csv')
X = data.iloc[:, 1]
Y = data.iloc[:, 0]

# Building the model
X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean


# Making prediction
Y_pred = m*X + c

plt.scatter(X, Y)
plt.title("Meantemp Stockholm 2022")
plt.xlabel("Meantemp")
plt.ylabel("Date")
plt.scatter(X_mean, Y_mean, label="Meantemp")
plt.plot(X_mean, m * Y_mean + c, "-r",
label = f"where:\nm = {m}\nc = {c}")
plt.plot(X, Y_pred, linestyle='-', color='red')
plt.legend()
plt.show()

