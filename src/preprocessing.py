# import libraries
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from config import RAW_DATA, PROCESSED_DATA, MODEL_DIR
# from api.routers import prediction

# load dataset
df = pd.read_csv(RAW_DATA)

# remove unneccessary columns
columns_to_drop = [
    "customerID"
]

df = df.drop(columns=columns_to_drop)

# separate features and target
X = df.drop(columns="Churn")
y = df["Churn"] = df['Churn'].map({"Yes": 1, "No": 0})

# numerical columns
numerical_cols = [
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]


# categorical columns
categorical_cols = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod"
]

# identify feature types
categorical_features = X.select_dtypes(
    include=["str"] #, "category"
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object", "string", "category"]
).columns.tolist()

numerical_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

print(categorical_features)
print(numerical_features)

# create preprocessing pipeline
# numerical pipeline
numerical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()) #, numerical_cols
])

# categorical pipeline
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")) #, categorical_cols
])

# combine pipelines
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_pipeline, numerical_cols),
        ("cat", categorical_pipeline, categorical_cols),
    ]
)

# preprocessor = ColumnTransformer( # This ensures the same transformations are applied consistently during training and inference.
#     transformers=[
#         ("num", numerical_pipeline, numerical_features),
#         ("cat", categorical_pipeline, categorical_features)
#     ]
# )

# train/test/validation split
# by using a three-way split.
X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.50,
    random_state=42,
    stratify=y_temp
)

# fit only on the training data
# NB: Never fit preprocessing on validation or test data. This prevents data leakage
X_train_processed = preprocessor.fit_transform(X_train)
X_val_processed = preprocessor.transform(X_val)
X_test_processed = preprocessor.transform(X_test)

# get feature names - Useful for debugging and explainability.
feature_names = preprocessor.get_feature_names_out()

# save the feature names file
joblib.dump(
    feature_names,
    MODEL_DIR / "features_names.pkl"
)

# save the preprocessor file
# Instead of saving separate encoders and scalers, save the entire fitted preprocessing pipeline.
joblib.dump(
    preprocessor,
    MODEL_DIR / "preprocessor.pkl"
)

# During inference, you'll load this single object and call:
# X_new_processed = preprocessor.transform(X_new)

# save the processed data
# Convert the processed arrays to DataFrames
X_train_df = pd.DataFrame(
    X_train_processed,
    columns=feature_names
)

X_test_df = pd.DataFrame(
    X_test_processed,
    columns=feature_names
)

X_val_df = pd.DataFrame(
    X_val_processed,
    columns=feature_names
)

# save them
X_train_df.to_csv(PROCESSED_DATA / "X_train.csv", index=False)
X_val_df.to_csv(PROCESSED_DATA / "X_val.csv", index=False)
X_test_df.to_csv(PROCESSED_DATA / "X_test.csv", index=False)

y_train.to_csv(PROCESSED_DATA / "y_train.csv", index=False)
y_val.to_csv(PROCESSED_DATA / "y_val.csv", index=False)
y_test.to_csv(PROCESSED_DATA / "y_test.csv", index=False)

# verify the shapes
print(X_train_processed.shape)
print(X_test_processed.shape)
print(X_val_processed.shape)
# print(X.columns.tolist())

# next lesson 5 - neural network
