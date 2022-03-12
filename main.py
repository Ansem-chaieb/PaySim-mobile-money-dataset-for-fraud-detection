import gc
import pandas as pd
import yaml
from box import Box

from src.data.data_loading import data_load, memory_manage
from src.data.data_processing import feature_engineering

with open("src/config.yaml", "r") as ymlfile:
    config = Box(yaml.safe_load(ymlfile))

data = data_load(config.DATA_PATH)
memory_manage(
    data,
    str_list=["nameDest", "type"],
    int_list=["isFlaggedFraud", "isFraud", "step"],
)

gc.collect()
feature_engineering(data, save=True, path=config.PROCESSED_DATA_PATH)

processed_data = data_load(config.PROCESSED_DATA_PATH)
