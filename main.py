import os
import gc
import pandas as pd
from sympy import im
import yaml
import argparse
from box import Box

from src.data.data_loading import data_load, memory_manage
from src.data.data_processing import feature_engineering
from src.data.EDA import launch_streamlit

with open("config.yaml", "r") as ymlfile:
    config = Box(yaml.safe_load(ymlfile))

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--process",
        help="Get informtions about your dataset.",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--eda",
        help="Get informtions about your dataset.",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()
    return args

args = get_args()
if args.process:
    data = data_load(config.DATA_PATH)
    memory_manage(
        data,
        str_list=["nameDest", "type"],
        int_list=["isFlaggedFraud", "isFraud", "step"],
    )

    gc.collect()
    feature_engineering(data, save=True, path=config.PROCESSED_DATA_PATH)

if args.eda:
    os.system("streamlit run src/data/EDA.py")
    
