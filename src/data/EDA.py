import pandas as pd
from PIL import Image
import streamlit as st
from streamlit import components

from data_processing import data_analysis

processed_data = pd.read_csv("data/processed_data.csv")
(   trans_type,
    transaction_duration,
    orig_transaction_error,
    amount_oldbalanceOrg,
    dest_transaction_error,
    orig_dest,
    flag,
) = data_analysis(processed_data)

st.set_page_config(layout="wide")
apollo = Image.open("images/apollo-farmer.jpg")
st.image(apollo, width=1500)
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
