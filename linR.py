import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

exp = np.array([
    1,1,1,1,1,
    2,2,2,2,2,
    3,3,3,3,3,
    4,4,4,4,4,
    5,5,5,5,5]
).reshape(-1, 1)

sal = np.array([
    4,4,4,4,4,
    7,7,7,7,7,
    10,10,10,10,10,
    13,13,13,13,13,
    16,16,16,16,16
]).reshape(-1, 1)

plt.scatter(exp, sal)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()

model = LinearRegression()
model.fit(exp, sal)
ui = input(" User :")
predsale = model.predict([[float(ui)]])
print(" Predicted Salary :", predsale[0][0])


plt.scatter(exp, sal, color='blue')
plt.plot(exp, model.predict(exp), color='red')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()
