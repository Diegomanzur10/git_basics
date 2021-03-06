import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

## Comment to check
X = np.array([[1,1], [1,2], [2,2], [2,3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1,2])) + 3

## Another comment to add
reg = LinearRegression().fit(X, y)

## This comment will be show up with the diff command???
reg.score(X,y)