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

    flag = pd.DataFrame({'isFraud' : (df.groupby('isFlaggedFraud')['isFraud'].agg('sum') /8213) * 100,
             'count': (df['isFlaggedFraud'].value_counts()/df.shape[0]) * 100}).reset_index(level=0)
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


def launch_streamlit(data):
    (
        trans_type,
        transaction_duration,
        orig_transaction_error,
        amount_oldbalanceOrg,
        dest_transaction_error,
        orig_dest,
        flag,
    ) = data_analysis(data)

    
