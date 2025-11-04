import streamlit as st
import plotly.express as px

def mostra_dashboard(data):
    """
    Visualizza i risultati in una dashboard interattiva Streamlit.
    """
    st.title("Analisi Clienti - Decision Support System")

    st.sidebar.header("Filtri")
    cluster = st.sidebar.selectbox("Seleziona Cluster", sorted(data['Cluster'].unique()))
    categoria = st.sidebar.selectbox("Categoria Prodotto", ['Tutte'] + list(data['Categoria'].unique()))

    df = data[data['Cluster'] == cluster]
    if categoria != 'Tutte':
        df = df[df['Categoria'] == categoria]

    st.write(f"### Cluster selezionato: {cluster}")
    st.dataframe(df[['ClienteID', 'Categoria', 'Quantità', 'SpesaTot', 'Strategia']])

    fig = px.scatter(df, x='Quantità', y='SpesaTot', color='Strategia', title="Distribuzione Clienti nel Cluster")
    st.plotly_chart(fig)

    st.bar_chart(df['Strategia'].value_counts())
