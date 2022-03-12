import pandas as pd

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

def data_analysis(data):
    trans_type = pd.DataFrame(
        {
            "isFraud": (data.groupby("type")["isFraud"].agg("sum") / 8213)
            * 100,
            "count": (data["type"].value_counts() / data.shape[0]) * 100,
        }
    ).reset_index(level=0)
    trans_type.columns = trans_type.columns.str.replace("index", "type")

    transaction_duration = pd.DataFrame(
        {
            "isFraud": (
                data.groupby("transaction_duration")["isFraud"].agg("sum")
                / 8213
            )
            * 100,
            "count": (
                data["transaction_duration"].value_counts() / data.shape[0]
            )
            * 100,
        }
    ).reset_index(level=0)
    transaction_duration.columns = (
        transaction_duration.columns.str.replace(
            "index", "transaction_duration"
        )
    )

    orig_transaction_error = pd.DataFrame(
        {
            "isFraud": (
                data.groupby("orig_transaction_error")["isFraud"].agg(
                    "sum"
                )
                / 8213
            )
            * 100,
            "count": (
                data["orig_transaction_error"].value_counts()
                / data.shape[0]
            )
            * 100,
        }
    ).reset_index(level=0)
    orig_transaction_error.columns = (
        orig_transaction_error.columns.str.replace(
            "index", "orig_transaction_error"
        )
    )

    amount_oldbalanceOrg = pd.DataFrame(
        {
            "isFraud": (
                data.groupby("amount_oldbalanceOrg")["isFraud"].agg("sum")
                / 8213
            )
            * 100,
            "count": (
                data["amount_oldbalanceOrg"].value_counts() / data.shape[0]
            )
            * 100,
        }
    ).reset_index(level=0)
    amount_oldbalanceOrg.columns = (
        amount_oldbalanceOrg.columns.str.replace(
            "index", "amount_oldbalanceOrg"
        )
    )

    dest_transaction_error = pd.DataFrame(
        {
            "isFraud": (
                data.groupby("dest_transaction_error")["isFraud"].agg(
                    "sum"
                )
                / 8213
            )
            * 100,
            "count": (
                data["dest_transaction_error"].value_counts()
                / data.shape[0]
            )
            * 100,
        }
    ).reset_index(level=0)
    dest_transaction_error.columns = trans_type.columns.str.replace(
        "index", "dest_transaction_error"
    )

    orig_dest = pd.DataFrame(
        {
            "isFraud": (
                data.groupby("orig_dest")["isFraud"].agg("sum") / 8213
            )
            * 100,
            "count": (data["orig_dest"].value_counts() / data.shape[0])
            * 100,
        }
    ).reset_index(level=0)
    orig_dest.columns = trans_type.columns.str.replace(
        "index", "orig_dest"
    )

    flag = pd.DataFrame({'isFraud' : (data.groupby('isFlaggedFraud')['isFraud'].agg('sum') /8213) * 100,
             'count': (data['isFlaggedFraud'].value_counts()/data.shape[0]) * 100}).reset_index(level=0)
    flag.columns = flag.columns.str.replace(
        "index", "flag"
    )
    
    return (
        trans_type,
        transaction_duration,
        orig_transaction_error,
        amount_oldbalanceOrg,
        dest_transaction_error,
        orig_dest,
        flag,
    )

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
