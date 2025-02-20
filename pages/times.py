import streamlit as st

st.set_page_config(
    layout ='wide',
    page_title ='Times',
    page_icon = '🥇'
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
clube = st.sidebar.selectbox ("Clube", clubes)

df_filtro = df_data[df_data["Club"] == clube].set_index("Name")

st.image(df_filtro.iloc[0]["Club Logo"])
st.markdown (f"## {clube}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Height(cm.)', 'Weight(lbs.)',
           'Joined', 'Contract Valid Until', 'Release Clause(£)',]

st.dataframe(df_filtro[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", format='%d', min_value=0, max_value=100),
                 "Value(£)": st.column_config.NumberColumn(),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", min_value=0, max_value=df_filtro["Wage(£)"].max()),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),}, height=1000)

df_data["Flag"]
