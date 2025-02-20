import streamlit as st

st.set_page_config(
    layout ='wide',
    page_title ='Times',
    page_icon = '🥇'
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
clube = st.sidebar.selectbox ("Clube", clubes)
