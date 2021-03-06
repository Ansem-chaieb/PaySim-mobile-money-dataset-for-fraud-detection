import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder


def data_clean(data):
    data = data[data["orig_dest"] == "C-C"]
    data = data[(data["type"] == "CASH_OUT") | (data["type"] == "TRANSFER")]

    return data


def data_preprocess(train, test, train_target, test_target):
    train = train.drop(
        [
            "amount_oldbalanceOrg",
            "dest_transaction_error",
            "orig_transaction_error",
            "orig_dest",
        ],
        1,
    )
    required_features = [
        col
        for col in train.columns
        if col not in ("Unnamed: 0", "nameOrig", "nameDest")
    ]
    cat_cols = [
        col for col in required_features if train[col].dtypes == np.object
    ]
    # enocde cat features
    encoder = OrdinalEncoder()
    train[cat_cols] = encoder.fit_transform(train[cat_cols])
    test[cat_cols] = encoder.fit_transform(test[cat_cols])

    X = train[required_features].values
    Xtest = test[required_features].values
    y = train_target.values
    ytest = test_target.values

    return X, Xtest, y, ytest


def feature_engineering(data, save=False, path=None):
    assert (save == True) & (
        path == None
    ), "Error: Path shouldn't be None. Enter path for processed data"
    data["amount_oldbalanceOrg"] = data.apply(amount_oldbalanceOrg, axis=1)
    data["orig_transaction_error"] = data.apply(
        orig_transaction_error, axis=1
    )
    data["dest_transaction_error"] = data.apply(
        dest_transaction_error, axis=1
    )
    data["orig_dest"] = data.apply(get_name_prefix, axis=1)
    data["transaction_duration"] = data.apply(transaction_duration, axis=1)

    data.to_csv(path)


def amount_oldbalanceOrg(row):
    if row["oldbalanceOrg"] - row["amount"] == 0:
        return "equal"
    else:
        return "not equal"


def dest_transaction_error(row):
    if row["newbalanceDest"] - row["oldbalanceDest"] - row["amount"] != 0:
        return "error"
    else:
        return "no error"


def orig_transaction_error(row):
    if row["oldbalanceOrg"] - row["newbalanceOrig"] - row["amount"] != 0:
        return "error"
    else:
        return "no error"


def get_name_prefix(row):
    return row["nameOrig"][0] + "-" + row["nameDest"][0]


def transaction_duration(row):
    if row["step"] / 24 < 1:
        return "less than one day"
    elif row["step"] / 168 < 1:
        return "less than a week"
    elif row["step"] / 744 < 1:
        return "less than a month"
    else:
        return "month"
