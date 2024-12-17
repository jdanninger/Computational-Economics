import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import xgboost as xgb

# Load the data
train = pd.read_csv('Cleaned Data/cleaned_train.csv', low_memory=False)
train['saleyear'] = train['saleyear'].astype(str)

test = pd.read_csv('Cleaned Data/cleaned_test.csv', low_memory=False)
test['saleyear'] = test['saledate'].astype(str)

# Separate features and target
X = train.drop(columns=['sellingprice'])
y = train['sellingprice']

# Check for NaN, infinity, or extremely large values in the target variable
y = y.replace([np.inf, -np.inf], np.nan)
y = y.fillna(y.mean())

# Ensure the features match the cleaned target variable
X = X.loc[y.index]

# Identify categorical columns
categorical_cols = X.select_dtypes(include=['object']).columns

# Create a column transformer with one-hot encoding for categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'  # Keep the rest of the columns as they are
)

# Apply the transformations to the training and test data
X_transformed = preprocessor.fit_transform(X)
test_transformed = preprocessor.transform(test)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_transformed, y, test_size=0.1, random_state=42)

# Convert the data into DMatrix format
dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_val, label=y_val)
dtest = xgb.DMatrix(test_transformed)

# Define the parameters for the XGBoost model
params = {
    'objective': 'reg:squarederror',
    'max_depth': 6,
    'eta': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'eval_metric': 'rmse'
}

# Train the model
evals = [(dtrain, 'train'), (dval, 'eval')]
model = xgb.train(params, dtrain, num_boost_round=400, early_stopping_rounds=10, evals=evals)

# Predict on the test set
predictions = model.predict(dtest)

# Create a DataFrame with "vin" and predicted "sellingprice"
output = pd.DataFrame({'vin': test['vin'], 'sellingprice': predictions})

# Print the output DataFrame
print(output)
output.to_csv('Predictions.csv', index=False)