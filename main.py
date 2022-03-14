import os
import gc
import pandas as pd
import numpy as np
import yaml
import argparse
from box import Box
from sklearn.metrics import confusion_matrix

from src.data_loading import data_load, memory_manage
from src.data_processing import feature_engineering, data_clean, data_preprocess
from src.models import create_test_data, run_model, metrics


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
    parser.add_argument(
        "--train",
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
    os.system("streamlit run src/streamlit_app.py")

if args.train:
    data = data_load(config.PROCESSED_DATA_PATH) 
    data = data_clean(data)
    train, test, train_target, test_target = create_test_data(data, config.TEST_SIZE)
    X, Xtest, y, ytest = data_preprocess(train, test, train_target, test_target)
    if config.XGB.TRAIN:
        model, final_preds = run_model(config, X, Xtest, y, ytest,  key= 'xgb')
        print('Testing') 
        preds = np.max(np.column_stack(final_preds), axis=1)
        conf_matrix = confusion_matrix(y_true=ytest, y_pred=preds)
        f1, recall, precision, accuracy = metrics(ytest, preds)
        print('Average F1 score: {}'.format(np.mean(f1)))
        print('Average Recall score: {}'.format(np.mean(recall)))
        print('Average Precision score: {}'.format(np.mean(precision)))
        print('Average Accuracy score: {}'.format(np.mean(accuracy)))
    elif config.LGBM.TRAIN:
        model, final_preds = run_model(config, X, Xtest, y, ytest,  key= 'lgb')
        print('Testing') 
        preds = np.max(np.column_stack(final_preds), axis=1)
        conf_matrix = confusion_matrix(y_true=ytest, y_pred=preds)
        f1, recall, precision, accuracy = metrics(ytest, preds)
        print('Average F1 score: {}'.format(np.mean(f1)))
        print('Average Recall score: {}'.format(np.mean(recall)))
        print('Average Precision score: {}'.format(np.mean(precision)))
        print('Average Accuracy score: {}'.format(np.mean(accuracy)))
    else:
        model, final_preds = run_model(config, X, Xtest, y, ytest,  key= 'cat')
        print('Testing') 
        preds = np.max(np.column_stack(final_preds), axis=1)
        conf_matrix = confusion_matrix(y_true=ytest, y_pred=preds)   
        f1, recall, precision, accuracy = metrics(ytest, preds)
        print('Average F1 score: {}'.format(np.mean(f1)))
        print('Average Recall score: {}'.format(np.mean(recall)))
        print('Average Precision score: {}'.format(np.mean(precision)))
        print('Average Accuracy score: {}'.format(np.mean(accuracy)))     
            
    



    
