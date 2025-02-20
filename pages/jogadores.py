import streamlit as st

st.set_page_config(
    layout ='wide',
    page_title ='Jogadores',
    page_icon = '🏃‍♂️'
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
clube = st.sidebar.selectbox ("Clube", clubes)

df_jogadores = df_data[df_data["Club"] == clube]
jogadores = df_jogadores["Name"].value_counts().index
jogador = st.sidebar.selectbox ("Jogador", jogadores)

estatistica_jogador = df_data[df_data["Name"] == jogador].iloc[0]

st.image(estatistica_jogador["Photo"])
st.title(f"{estatistica_jogador['Name']}")

st.markdown = (f"**Clube:** {estatistica_jogador['Club']}")
st.markdown = (f"**Posição:** {estatistica_jogador['Position']}")

col1, col2, col3 = st.columns(3)

col1.markdown = (f"**Idade:** {estatistica_jogador['Age']}")
col2.markdown = (f"**Altura:** {estatistica_jogador['Height(cm.)'] /100}")
col3.markdown = (f"**Peso:** {estatistica_jogador['Weight(lbs.)'] / 0.453:.2f}")

st.divider()

st.subheader= (f"Overall{estatistica_jogador['Overall']}")
st.progress(int(estatistica_jogador['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de Mercado", value=f"£{estatistica_jogador['Value(£)']:,}")
col2.metric(label="Remunerção Semanal", value=f"£{estatistica_jogador['Wage(£)']:,}")
col3.metric(label="Clásula da Rescisão", value=f"£{estatistica_jogador['Release Clause(£)']:,}")

