from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
x = np.arange(-10, 11).reshape(-1, 1)
y = (3*x**3 + 2*x**2 + x + np.random.randint(-2,2)).reshape(-1, 1)

print(x)
print(y)

model = DecisionTreeRegressor(max_depth=3)
model.fit(x, y)
y_pred = model.predict(x)
print("Predicted values:", y_pred)
print("R2 Score:", r2_score(y, y_pred))
print("Mean Squared Error:", mean_squared_error(y, y_pred))
plt.scatter(x, y, color="red", label="Actual Data")
plt.scatter(x, y_pred, color="blue", label="Predicted Data")
plt.legend()
plt.show()