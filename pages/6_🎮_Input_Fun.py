import streamlit as st
import numpy as np
import pandas as pd


# Initialize session state for text input
if "input_text" not in st.session_state:
    st.session_state.input_text = ""


if "input_num" not in st.session_state:
    st.session_state.input_num = ""

if "df" not in st.session_state:  # Persist the dataframe across reruns
    st.session_state.df = pd.DataFrame({'name': ['ciaone', 'scoreggione', 'blabla'], 'valori': [12, 34, 76]})


# Reset function
def reset_input_text():
    st.session_state.input_text = ""
    st.session_state.text_key += 1

def reset_input_number():
    st.session_state.input_num = ""
    st.session_state.num_key += 1


# Unique keys for forcing reruns
if "text_key" not in st.session_state:
    st.session_state.text_key = 0

if "num_key" not in st.session_state:
    st.session_state.num_key = 0

st.write("Let´s make teh first dataset")

usertext = st.text_input("Write something here", value=st.session_state.input_text, key=f"text_{st.session_state.text_key}")
if usertext:
    st.write(f'You wrote: {usertext}')

# Submit text button
if st.button("Submit text"):
    st.write(f"You entered: {usertext}")
    st.session_state.input_text = ""  # Reset input text immediately
    reset_input_text()  # Force refresh to clear input

# Number input
usernumber = st.text_input("Write a number", value=st.session_state.input_num, key=f"num_{st.session_state.num_key}")
if usernumber:
    st.write(f"You wrote {usernumber}")

# Submit number button
if st.button("Submit number"):
    st.write(f"You entered: {usernumber}")
    st.session_state.input_num = ""  # Reset input number immediately
    reset_input_number()  # Force refresh to clear input

# Append new entry to DataFrame
if usertext and usernumber:
    line = pd.Series([usertext, usernumber], index=st.session_state.df.columns)
    st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame(line).T], ignore_index=True)

# Display dataframe
st.dataframe(st.session_state.df)