from tkinter.tix import IMAGE
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit import components



st.set_page_config(layout="wide")
apollo = Image.open("images/apollo-farmer.jpg")
#st.image(apollo, width=1500)
# =================================================================================== #
#                                Sidebar                                              #
# =================================================================================== #
apollo_img = Image.open("images/apollo.png")
st.sidebar.image(apollo_img)
st.sidebar.title("Case study for transaction fraudulent:")
st.sidebar.markdown("Navigation:")

viz = st.sidebar.checkbox("Data exploration")
res = st.sidebar.checkbox("benchmarking")

# =================================================================================== #
#                                First  page                                          #
# =================================================================================== #
if viz:
    st.title("Data exploration")
    col1, col2, col3 = st.columns(3)
    with col1:
        tp = Image.open('images/name.png')
        st.image(tp)
        st.markdown(
        "figure1: Types of orginates-destination"
        )
        st.dataframe(pd.DataFrame({"orig-dest": ["C-C", "C-M"],
        "isFraud": [100.0, 0.0], "count": [66.185392, 	33.814608]}))
        st.markdown("None of the transaction where M (Merchants) is the destination is fraud, despite it represent 33.8 % of al the data.")
    with col2:
        tp = Image.open('images/type.png')
        st.image(tp)
        st.markdown(
        "figure2: Counts of transaction type"
        )
        st.dataframe(pd.DataFrame({"type": 
        ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'],
        "isFraud": [0.0, 50.11567027882625, 0.0, 0.0, 49.88432972117375], 
        "count": [21.992261049693365, 35.16633085112736,0.6511782881894566,
                    33.81460781879163,8.375621992198184]}))
    with col3:
        tp_f = Image.open('images/type_fraud.png')
        st.image(tp_f)
        st.markdown(
        "figure3: influece of transaction type on target"
        ) 
        st.markdown("None of the transaction where its type is cash_in, debit or payment is fraud, despite they represent 56.45 %  of the data.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        tp = Image.open('images/orig_transaction_error.png')
        st.image(tp)
        st.markdown(
        "figure4: Error in originates account"
        )
        st.dataframe(pd.DataFrame({"orig-tran-error": ['error', 'no error'],
        "isFraud": [0.8401314988432973, 99.1598685011567],
         "count": [93.07657851639733, 6.923421483602667]}))
        st.markdown("Error : oldbalanceOrg - newbalanceOrig != amount")
    with col2:
        tp = Image.open('images/amount_oldbalanceorg.png')
        st.image(tp)
        st.markdown(
        "figure5: Relation between old transaction orig , amount and target"
        )
        st.dataframe(pd.DataFrame({"amount-oldtrans-orig": 
        ['equal', 'not equal'],
        "isFraud": [97.82052843053695, 2.1794715694630464],
        "count": [0.12626873834992502, 99.87373126165008]}))
        st.markdown("It's clear that if the transaction amount is equal to oldtransorig so 97.82 % it's fraud, as a result this feature is leakage.")
    with col3:
        st.dataframe(pd.DataFrame({"isFlaggedFraud": [0, 1],
        "isFraud":[0.12883090005287143, 100.0],
         "count": [99.99974853126542, 0.000251468734577894]}))
        st.markdown(
        "table5: influece of transaction type on target"
        )    
        st.markdown("Only 0.0003 % of the transaction are more than 200.000 and all of the flagged transaction are truly fraud.") 
    tp = Image.open('images/corr.png')
    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    col2.image(tp, use_column_width=True)

    col2.markdown(
        "figure6: Feature corrolation"
        )
# =================================================================================== #
#                                Second  page                                         #
# =================================================================================== #   
st.title("Benchmark Experiences:")
col1, col2, col3 = st.columns([0.2, 1, 0.2])  
col2.dataframe({
" ":["Hardware environment","Xgboost params", "lightgbm params", "catboost params"],
"Description": ["Dual Nvidia TeslaP100(CUDA v= 11, GPU RAM(GB)= 17.1)",
                "learning rate: 0.01, n_estimators: 1000, max_depth: 6, metric: log_loss ...", 
                "learning rate: 0.01, n_estimators: 1000, max_depth: 6 ..." ,
                "learning rate: 0.01, n_estimators: 1000, max_depth: 6, metric: recall ..." ]}) 

st.header("Baselines:")
col1, col2, col3 = st.columns([0.2, 2, 0.2]) 
col2.dataframe({"Model": ["lgbm", "catboost", "xgboost"],
                "Train speed (min) ":[9, 2.35, 61.8],
                "Test speed (min)":[5.85, 0.14,0.03],
                "F1":[0.232, 0.850, 0.843],
                "Recall":[0.905, 0.749, 0.734],
                "Precision":[0.131, 0.982, 0.989],
                "Accuracy":[0.901, 0.956, 0.956],})
col1, col2, col3 = st.columns(3) 
col1.image("./results/baseline/lgbm3.png")   
col1.markdown("figure 7: lgbm confusion matrix (baseline)") 
col2.image("./results/baseline/cat3.png")   
col2.markdown("figure 8: catboost confusion matrix (baseline)")  
col3.image("./results/baseline/xgb3.png")   
col3.markdown("figure 9: xgb confusion matrix (baseline)")    

st.header("Experiement 1:")
col1, col2, col3 = st.columns([0.2, 2, 0.2]) 
col2.dataframe({"Model": ["lgbm", "catboost"],
                "Train speed (min) ":[3.36, 1.28],
                "Test speed (min)":[2.63, 0.05],
                "F1":[0.257, 0.847],
                "Recall":[0.965, 0.756],
                "Precision":[0.147, 0.962],
                "Accuracy":[0.981, 0.992],})
col1, col2 = st.columns(2) 
col1.image("./results/exp1/lgbm3.png")   
col1.markdown("figure 10: lgbm confusion matrix (experiement 1)") 
col2.image("./results/exp1/cat3.png")   
col2.markdown("figure 11: catboost confusion matrix (experiement 1)")  

st.header("Experiement 2:")
col1, col2, col3 = st.columns([0.2, 2, 0.2]) 
col2.dataframe({"Model": ["lgbm", "catboost"],
                "Train speed (min) ":[1.28, 0.83],
                "Test speed (min)":[0.98, 0.01],
                "F1":[0.510, 0.882],
                "Recall":[0.996, 0.804],
                "Precision":[0.343, 0.975],
                "Accuracy":[0.984, 0.998],})
col1, col2 = st.columns(2) 
col1.image("./results/exp2/lgbm3.png")   
col1.markdown("figure 12: lgbm confusion matrix (experiement 2)") 
col2.image("./results/exp2/cat3.png")   
col2.markdown("figure 13: catboost confusion matrix (experiement 2)")  



