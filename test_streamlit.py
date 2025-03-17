import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello, Streamlit! 👋")
st.write("This is your first web app in Python!")

if st.button("Click me!"):
    st.write("Button clicked!")




st.write("Let´s make teh first dataset")

df = pd.DataFrame({
    'name': ['ciaone', 'scoreggione', 'blabla'],
    'valori':[12, 34, 76]
})

st.dataframe(df)


usertext = st.text_input("Write something here")
if usertext:
    st.write(f'You wrote: {usertext}')

usernumber = st.text_input("Write a number")
if usernumber:
    st.write(f"You wrote {usernumber}")


pd.concat(df, pd.Series([usertext, usernumber]), axis = 0)

st.dataframe(df)
