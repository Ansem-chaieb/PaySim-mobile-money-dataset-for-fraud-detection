import lightgbm as lgb
from pytest import param
import xgboost as xgb
import catboost as cb

import timeit
import numpy as np
from sklearn.metrics import f1_score, recall_score, precision_score, accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split, RepeatedKFold


def create_test_data(data, test_size):
    train, test, train_target, test_target = train_test_split(
        data.drop("isFraud",1), data["isFraud"], test_size=test_size)
    return train, test, train_target, test_target

def run_model(config, model, X, Xtest, y, ytest,  key):
    final_preds, F1, Recall, Precision,  Accuracy = [], [], [], [], []
    train_speed, test_speed = 0, 0

    rkf = RepeatedKFold(n_splits=config.N_SPLITS, n_repeats=config.N_REPEATS, random_state=config.RANDOM_STATE)
    params = get_model_params(key, config)
    model = define_model(key, params)

    print('-' * 60)
    print("Start training {}".format(key))
    print('-' * 60)    
    for i, (train_index, test_index) in enumerate(rkf.split(X)):
        X_train, X_val = X[train_index], X[test_index]
        y_train, y_val = y[train_index], y[test_index]
        print('Training')
        start = timeit.default_timer()
        model.fit(X_train,y_train)
        stop = timeit.default_timer()
        train_speed += stop - start
            
        print('validation') 
        #Prediction session
        valid_preds = model.predict(X_val)
        conf_matrix = confusion_matrix(y_true=y_val, y_pred=valid_preds)
        print(conf_matrix)
        start = timeit.default_timer()
        test_preds = model.predict(Xtest)
        stop = timeit.default_timer()
        test_speed += stop - start
        print("Evaluate")
        final_preds.append(test_preds)
        #Performance evaluation
        f1, recall, precision, accuracy = metrics(y_val, valid_preds)
        F1.append(f1)
        Recall.append(recall)
        Precision.append(precision)
        Accuracy.append(accuracy)
        print("Fold {} ==> f1: {}, recall: {}, precision: {}, accuracy: {} \n".format(i + 1, f1, recall, precision, accuracy))
    print('-' * 30)
    print('Average F1 score: {}'.format(np.mean(F1)))
    print('Average Recall score: {}'.format(np.mean(Recall)))
    print('Average Precision score: {}'.format(np.mean(Precision)))
    print('Average Accuracy score: {}'.format(np.mean(Accuracy)))
    print("train_speed: {}".format(train_speed))
    print("test_speed: {}".format(test_speed))
    print('-' * 30)   

    return model, final_preds 

def metrics(yvalid, valid_preds):
    f1 = f1_score(yvalid, valid_preds)
    recall = recall_score(yvalid, valid_preds)
    precision = precision_score(yvalid, valid_preds)
    accuracy = accuracy_score(yvalid, valid_preds)
    return f1, recall, precision, accuracy
  

def define_model(key, params):
    if key == "lgb":
        model = lgb.LGBMClassifier(**params)
    elif key ==  "cat":   
        model = cb.CatBoostClassifier(**params)
    else :   
        model = xgb.XGBClassifier(**params)
    return model

def get_model_params(key, config):
    if key == "xgb":
        params = {
            'objective':config.XGB.OBJECTIVE,
            "eval_metric": config.XGB.EVAL_METRIC,
            "learning_rate": config.XGB.LEARNING_RATE,
            "max_depth": config.XGB.MAX_DEPTH,
            "min_child_weight": config.XGB.MIN_CHILD_WEIGHT,
            "colsample_bytree": config.XGB.COLSAMPLE_BYTREE,
            "subsample": config.XGB.SUBSAMPLE,
            "n_estimators": config.XGB.N_ESTIMATORS,
            "predictor": config.XGB.PREDICTOR,
            "random_state": config.XGB.RANDOM_STATE,
            "use_label_encoder": config.XGB.USE_LABEL_ENCODER, 
            "verbosity" : config.XGB.VERBOSITY,
            }
    elif key == "lgb":
        params = {
            "num_leaves": config.LGBM.NUM_LEAVES,
            "objective": config.LGBM.OBJECTIVE,
            "is_unbalance": config.LGBM.IS_BALANCE,
            "learning_rate": config.LGBM.LEARNING_RATE,
            "max_depth": config.LGBM.MAX_DEPTH,
            "n_estimators": config.LGBM.N_ESTIMATORS,
            "boosting_type": config.LGBM.BOOSTING_TYPE,
            "verbose": config.LGBM.VERBOSE,
            }
    else: 
        params = {
            "loss_function": config.CAT.LOSS_FUNCTION,
            "eval_metric": config.CAT.EVAL_METRIC,  
            "learning_rate": config.CAT.LEARNING_RATE,
            "depth": config.CAT.DEPTH,
            "iterations": config.CAT.ITERATIONS,
            "task_type": config.CAT.TASK_TYPE,
            "silent": config.CAT.SILENT,
            }
    return params      