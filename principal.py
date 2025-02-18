import pandas as pd
import streamlit as st
import webbrowser as wb
from datetime import datetime as dttm

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col = 0)
    df_data = df_data[df_data["Contrat Valid Until"] >= dttm.today().year]
    df_data = df_data[df_data["Value(€)"] > 0]
    df_data = df_data.sortvalues(by="Overall", Ascending=False)
    st.session_state["data"] = df_data

st.write ("# FIFA 2023 OFFICIAL DATASET!!")
st.sidebar.markdown("Desenvolvido por [xxxxxx](https:www.hello.com.br)")

buttonn = st.button("Acesse os Dados no Kaggle")

if buttonn:
    wb.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data?resource=download")

st.subheader("Contexto")

st.markdown("O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes de contratos e afiliações de clubes. "
            
"**Com mais de 17.000 registos**, este conjunto de dados oferece um recurso valioso para analistas de futebol, investigadores e entusiastas interessados ​​em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo.")

