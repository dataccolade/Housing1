import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
@st.cache_data
def load_data():
    file = "Housing.csv"
    return pd.read_csv(file)

data = load_data()

numeric_columns = data.select_dtypes(exclude=['object']).columns.tolist()
categorical_columns = data.select_dtypes(include=['object']).columns.tolist()

st.write("# Découverte du dataset Housing")
st.write("Cette application permet d'explorer le dataset Housing, qui contient des informations sur les logements.")
st.write("## Informations sur le dataset")
st.write(f"Nombre de lignes : {data.shape[0]}")
st.write(f"Nombre de colonnes : {data.shape[1]}")
st.write("## Informations sur les colonnes")
st.write(data.dtypes.to_frame(name='Type de données').T)
st.write(f"Colonnes numériques : {numeric_columns}")
st.write(f"Colonnes catégorielles : {categorical_columns}")

st.write("## Data Overview")
st.write(data.head())

# Visualisation des colonnes numériques
st.write("## Visualisation des colonnes numériques")
st.selectbox("Sélectionnez une colonne numérique pour visualiser", numeric_columns, key="numeric_col")

col_hist, col_box = st.columns(2)

with col_hist:
    st.write("### Histogramme")
    selected_numeric_col = st.session_state.get("numeric_col", numeric_columns[0])
    fig_hist = px.histogram(data, x=selected_numeric_col)
    st.plotly_chart(fig_hist)
    
with col_box:
    st.write("### Boîte à moustaches")
    fig_box = px.box(data, y=selected_numeric_col)
    st.plotly_chart(fig_box)

# Visualisation des colonnes catégorielles
st.write("## Visualisation des colonnes catégorielles")
st.selectbox("Sélectionnez une colonne catégorielle pour visualiser", categorical_columns, key="categorical_col")

col_bar, col_pie = st.columns(2)

with col_bar:
    st.write("### Diagramme à barres")
    fig_bar = px.bar(data, x=st.session_state.get("categorical_col", categorical_columns[0]), title="Diagramme à barres")
    st.plotly_chart(fig_bar)
    
with col_pie:
    st.write("### Diagramme circulaire")
    fig_pie = px.pie(data, names=st.session_state.get("categorical_col", categorical_columns[0]), title="Diagramme circulaire")
    st.plotly_chart(fig_pie)