import pandas as pd


def memory_manage(data, str_list=None, int_list=None):
    for col in str_list:
        print("Reduce memory usage for strings:")
        print(
            "Convert",
            col.ljust(30),
            "size: ",
            round(data[col].memory_usage(deep=True) * 1e-6, 2),
            end="\t",
        )
        data[col] = data[col].astype("category")
        print("->\t", round(data[col].memory_usage(deep=True) * 1e-6, 2))

    max_length = max([len(col) for col in int_list])
    for col in int_list:
        print("Downcasting integers:")
        print(
            "Convert",
            col.ljust(max_length + 2)[: max_length + 2],
            "from",
            str(
                round(data[col].memory_usage(deep=True) * 1e-6, 2).rjust(8)
            ),
            "to",
            end="\t",
        )
        data[col] = pd.to_numeric(data[col], downcast="integer")
        print(
            str(round(data[col].memory_usage(deep=True) * 1e-6, 2)).rjust(
                8
            )
        )


def data_load(path):
    data = pd.read_csv(path)
    print("-------data information:-----------")
    data.info(memory_usage="deep")
    print("Data shape: {}".format(data.shape[0]))
    return data


