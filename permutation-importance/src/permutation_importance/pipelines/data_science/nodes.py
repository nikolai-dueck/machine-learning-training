from typing import Dict, Tuple
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import eli5
from eli5.sklearn import PermutationImportance


def split_data(model_input_data: pd.DataFrame, parameters: Dict) -> Tuple:
    y = model_input_data.fare_amount
    X = model_input_data[parameters["features"]]

    train_X, val_X, train_y, val_y = train_test_split(X, y, 
                                                      test_size=parameters['test_size'], 
                                                      random_state=parameters['random_state'])

    return train_X, val_X, train_y, val_y


def train_model(train_X: pd.DataFrame, train_y: pd.Series) -> RandomForestRegressor:
    return RandomForestRegressor(n_estimators=50, random_state=1).fit(train_X, train_y)


def evaluate_features(regressor: RandomForestRegressor, test_X: pd.DataFrame, test_y: pd.Series) -> pd.DataFrame:
    """Calculates and logs the Permutation Importance."""
    perm = PermutationImportance(regressor, random_state=1).fit(test_X, test_y)
    return eli5.explain_weights_df(estimator=perm, feature_names = test_X.columns.tolist())