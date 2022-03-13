import pandas as pd

def data_analysis(data):
    trans_type = pd.DataFrame(
        {
            "isFraud": (data.groupby("type")["isFraud"].agg("sum") / 8213)
            * 100,
            "count": (data["type"].value_counts() / data.shape[0]) * 100,
        }
    ).reset_index(level=0)
    trans_type.columns = trans_type.columns.str.replace("index", "type")
    trans_type.to_csv("data/group_data/trans_type.csv")

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
    transaction_duration.to_csv("data/group_data/transaction_duration.csv")

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
    orig_transaction_error.to_csv("data/group_data/orig_transaction_error.csv")

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
    amount_oldbalanceOrg.to_csv("data/group_data/amount_oldbalanceOrg.csv")

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
    dest_transaction_error.to_csv("data/group_data/dest_transaction_error.csv")

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
    orig_dest.to_csv("data/group_data/orig_dest.csv")

    flag = pd.DataFrame({'isFraud' : (data.groupby('isFlaggedFraud')['isFraud'].agg('sum') /8213) * 100,
             'count': (data['isFlaggedFraud'].value_counts()/data.shape[0]) * 100}).reset_index(level=0)
    flag.columns = flag.columns.str.replace(
        "index", "flag"
    )
    flag.to_csv("data/group_data/flag.csv")
    return (
        trans_type,
        transaction_duration,
        orig_transaction_error,
        amount_oldbalanceOrg,
        dest_transaction_error,
        orig_dest,
        flag,
    )