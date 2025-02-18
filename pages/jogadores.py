import streamlit as st

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
clube = st.sidebar.selectbox ("Clube", clubes)
