import gc
import pandas as pd
import yaml
from box import Box

from src.data.data_process import data_load, memory_manage


with open("src/config.yaml", "r") as ymlfile:
    config = Box(yaml.safe_load(ymlfile))

data = data_load(config.DATA_PATH)
memory_manage(
    data,
    str_list=["nameDest", "type"],
    int_list=["isFlaggedFraud", "isFraud", "step"],
)
