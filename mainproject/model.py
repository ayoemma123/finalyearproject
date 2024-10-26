# Save the model as CADAI.pkl (run this script separately to create the model file)
import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np
from keras import Sequential

# Example training data (ensure these arrays have matching sample sizes)
X_train = np.array([
    [45, 1, 3, 120, 240, 1, 0, 150, 0, 2.3, 0, 0, 1],
    [50, 0, 2, 130, 250, 0, 1, 160, 1, 1.4, 2, 1, 3],
    # Add more samples here
])
y_train = np.array([0, 1])  # Ensure this matches the number of samples in X_train

model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'CADAI.pkl')

X_train = np.array([
    [45, 1, 3, 120, 240, 1, 0, 150, 0, 2.3, 0, 0],
    [50, 0, 2, 130, 250, 0, 1, 160, 1, 1.4, 2, 1],
    # Add more samples here
])
y_train = np.array([0, 1])  # Ensure this matches the number of samples in X_train

model =  Sequential()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model,'HF.pkl')