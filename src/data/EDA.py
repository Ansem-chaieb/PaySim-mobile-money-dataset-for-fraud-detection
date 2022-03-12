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
res = st.sidebar.checkbox("Experiences benchmark")

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