# ----------------------------------------
# House Price Predictor using Linear Regression
# ----------------------------------------

import numpy as np
from sklearn.linear_model import LinearRegression

# Training Dataset (House Size in sq.ft vs Price)
house_size = np.array([500, 700, 900, 1100, 1300, 1500]).reshape(-1, 1)
house_price = np.array([150000, 200000, 250000, 300000, 360000, 400000])

# Create model
model = LinearRegression()

# Train model
model.fit(house_size, house_price)

# Test prediction
new_size = np.array([[1200]])
predicted_price = model.predict(new_size)

print("House size:", new_size[0][0], "sq.ft")
print("Predicted house price: $", round(predicted_price[0], 2))