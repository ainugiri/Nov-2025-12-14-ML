import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
x = np.arange(-5, 6,1)
print(x)
y = np.array([
    -358,-204,-102,-32,-6,1,3,17,60,150,308
])

print(y)

df = pd.DataFrame({
    "x": x,
    "y": y })
print(df)

plt.scatter(df["x"], df["y"], color="red")
plt.show()

poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(df[["x"]])
df_poly = pd.DataFrame(x_poly, columns=poly.get_feature_names_out(["x"]))
print(df_poly)

model = LinearRegression()
model.fit(df_poly, df[["y"]])

model_predict = model.predict(df_poly)

plt.scatter(df["x"], df["y"], color="red")
plt.scatter(df["x"], model_predict, color="blue")
plt.show()

df1 = pd.DataFrame({
    "x": x,
    "y1":y,
    "y2": model_predict.flatten() })
print(df1)

print("R2 score", r2_score(df1["y1"], df1["y2"]))

x2 = int(input("Enter x value for prediction: "))
x2_poly = poly.transform([[x2]])
y2_pred = model.predict(x2_poly)

plt.scatter(df["x"], df["y"], color="red")
plt.scatter(df["x"], model_predict.flatten(), color="blue")
plt.scatter(x2, y2_pred, color="green")
plt.show()