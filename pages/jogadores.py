import streamlit as st

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
clube = st.sidebar.selectbox ("Clube", clubes)

df_jogadores = df_data[df_data["Club"] == clube]
jogadores = df_jogadores["Name"].value_counts().index
jogador = st.sidebar.selectbox ("Jogador", jogadores)

estatistica_jogador = df_data[df_data["Name"] == jogador].iloc[0]

st.image(estatistica_jogador["Photo"])
st.title(f"{estatistica_jogador['Name']}")