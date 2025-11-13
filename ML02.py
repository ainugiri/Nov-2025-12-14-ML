import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
data = {
"age" :[0,
                1,1,1,1,1,
                2,2,2,2,2,
                3,3,3,3,3,
                4,4,4,4,4,
                5,5,5,5,5],
"price" : [21,
                  20.5,20.51,20.52,20.49,20.5,
                  20.01,19.99,20,20.011,20,
                  19.6,19.5,19.4,19.5,19.51,
                  None,19,19.01,19.1,18.99,
                  18.5,18.51,18.52,18.48,18.49]    # Price in $10000
}
df = pd.DataFrame(data)
print(df)
df = df.dropna()
print(df)

x = df["age"].values.reshape(-1, 1)
y = df["price"].values.reshape(-1, 1)

model = LinearRegression()
model.fit(x,y)
predict_price = model.predict(x)

print("Coeff", model.coef_)
print("Intercept", model.intercept_)
print("R2 Score ",r2_score(y, predict_price))
plt.scatter(x,y,color="red")
plt.scatter(x,predict_price,color="blue")
plt.show()

print(predict_price)

ageforPrediction = int(input("ENter the age for prediction :"))
predicted_price_for_age = model.predict([[ageforPrediction]])
print(f"Predicted price for age {ageforPrediction} is {predicted_price_for_age[0][0]}")