import streamlit as st

import numpy as np
import pandas as pd

import plotly.express as px


st.title("Data analysis")
st.subheader("This page is to upload a file and visualize it and understand it better")


@st.cache_data
def load_data_csv(file):
    return pd.read_csv(file)
def load_data_xls(file):
    return pd.read_excel(file)

### what is this uploader allowing? 
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = load_data_csv(uploaded_file)
    else:
        df = load_data_xls(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df.head())  # Show first 5 rows

st.write("### Data Summary and Description")
with st.expander("See more details"):
    st.write("This is hidden until expanded.")

    ## what is locals()?
    if 'df' in locals():
        st.write(df.describe().T)
        st.write(df.info())
    else:
        st.write("No data uploaded yet")



if uploaded_file is not None:
    column = st.selectbox("Choose a column to plot",
                           df.select_dtypes(include=np.number).columns)

    ## visualize distribution of the numerical column
    fig = px.histogram(df, x=column, marginal="rug",hover_data=df.columns)
    st.plotly_chart(fig)
    ## define categorical and numerical columns
    categorical_columns = df.select_dtypes(include='object').columns
    numerical_columns = df.select_dtypes(include=np.number).columns
    cat_col = st.selectbox("Choose categorical columnms:", categorical_columns)
    st.write(f"You selected: {cat_col} to be used as color")

    num_col = st.selectbox("Choose numerical columns:", numerical_columns)
    st.write(f"You selected: {num_col}")

    fig_num = px.histogram(df, x=num_col, color = cat_col,  marginal="rug",hover_data=df.columns)
    st.plotly_chart(fig_num)
    

if uploaded_file is not None:   
    st.write("### Visualize the categorical")
    st.bar_chart(df[cat_col].value_counts())



if uploaded_file is not None:

    st.write("### Pairplot")
    target_var = st.selectbox("Choose a target variable", df.columns)
    dimensions = st.multiselect("Choose dimensions", numerical_columns)
    fig_pairplot = px.scatter_matrix(df, 
                dimensions = dimensions, 
                color = target_var)
    st.plotly_chart(fig_pairplot)



if uploaded_file is not None:
    st.write("### Correlation Plot")
    corr = df[dimensions].corr()
    fig_corr = px.imshow(corr, aspect='auto', 
                         color_continuous_scale='RdBu', title='Correlation Plot')   
    st.plotly_chart(fig_corr)
    
## voglio avere la visualizzazione scrollabile delle info e delle desacrizioni 
## voglio estrarre le colonne dividendo tra numeriche e categoriche
## dare la possibilita´ di creare grafici di un tipo per le numeriche 
### grafici di un altro per le categoriche

## di sicuro ci sono selector da mettere e qualcosa con il change state

