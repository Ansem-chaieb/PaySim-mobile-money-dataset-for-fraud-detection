import pandas as pd

def memory_manage(data, str_list=None, int_list=None):
    for col in str_list:
        print("Convert", col, "size: ", round(data[col].memory_usage(deep=True)*1e-6,2), end="\t")
        data[col] = data[col].astype("category")
        print("->\t", round(data[col].memory_usage(deep=True)*1e-6,2))
        
def data_load():
    pass

def data_analysis():
    pass