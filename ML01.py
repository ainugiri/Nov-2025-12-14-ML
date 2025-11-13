import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

age = np.array([0,1,2,3,4,5,6,7]).reshape(-1,1)   # Ford -> End
price = np.array([21,20.5,20,19.5,19,18.5,18,17.5])   # Price in $10000



model = LinearRegression()
model.fit(age, price)
pred_price = model.predict(age)

age12 = int(input("Car Age: "))
predicted_price = model.predict([[age12]])
print("Predicted car price ", predicted_price)
plt.scatter(age, price, color='blue', marker='x')
plt.plot(age, pred_price, color='red')
plt.scatter(age12, predicted_price, color = 'blue', marker='o')
plt.show()