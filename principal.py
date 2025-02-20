import pandas as pd
import streamlit as st
import webbrowser as wb
from datetime import datetime


if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv",index_col = 0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.write ("# FIFA 2023 OFFICIAL DATASET!!")
st.sidebar.markdown("Desenvolvido por [xxxxxx](https:www.hello.com.br)")

butao = st.button("Acesse os Dados no Kaggle")

if butao:
    wb.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data?resource=download")
