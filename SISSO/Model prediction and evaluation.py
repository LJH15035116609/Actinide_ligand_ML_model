import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('train_selected.csv')

# Extract actual values and the features
actual = data['logK'].values  # Assuming the last column is the actual values
SMR_VSA1 = data['SMR_VSA1'].values
NumHDonors = data['NumHDonors'].values
VSA_EState2 = data['VSA_EState2'].values
s_ = data['s+'].values
HOMO_metal = data['HOMO_metal'].values
VIP = data['VIP'].values

# Predicted values based on the provided formula
predicted = 0.069 * SMR_VSA1 + NumHDonors + 0.23 * VSA_EState2 - 1.66 * s_ - 4.26 * HOMO_metal - 55.43 * VIP + 13.87

# Calculate R^2
r2 = r2_score(actual, predicted)

# Calculate RMSE (Root Mean Squared Error)
rmse = np.sqrt(mean_squared_error(actual, predicted))

# Calculate MaxAE (Maximum Absolute Error)
maxae = np.max(np.abs(actual - predicted))

# Print the results
print(f"R²: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MaxAE: {maxae:.4f}")
