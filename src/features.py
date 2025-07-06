import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def encode_categorical_features(df: pd.DataFrame, categorical_cols: list) -> pd.DataFrame:
    """Encode categorical columns using one-hot encoding."""
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df_encoded

def select_features(df: pd.DataFrame, target_col: str, drop_cols: list = []) -> tuple:
    """Select features and target for modeling."""
    X = df.drop(columns=[target_col] + drop_cols)
    y = df[target_col]
    return X, y
