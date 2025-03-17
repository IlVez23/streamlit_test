import streamlit as st
import numpy as np
import pandas as pd

page = st.sidebar.selectbox("Go to:", ["Home", "Settings", "About"])
st.write(f"You're on the {page} page!")

st.title("Hello, Streamlit! 👋")
st.write("This is your first web app in Python!")

if st.button("Click me!"):
    st.write("Button clicked!")


# Initialize session state for text input
if "input_text" not in st.session_state:
    st.session_state.input_text = ""


if "input_number" not in st.session_state:
    st.session_state.input_num = ""

# Reset function
def reset_input():
    st.session_state.input_text = ""



st.write("Let´s make teh first dataset")

df = pd.DataFrame({
    'name': ['ciaone', 'scoreggione', 'blabla'],
    'valori':[12, 34, 76]
})

st.dataframe(df)


usertext = st.text_input("Write something here", st.session_state.input_text)
if usertext:
    st.write(f'You wrote: {usertext}')

# Submit button
if st.button("Submit"):
    st.write(f"You entered: {usertext}")
    reset_input()  # Clear input field after submitting

usernumber = st.text_input("Write a number", st.session_state.input_num)
if usernumber:
    st.write(f"You wrote {usernumber}")

# Submit button
if st.button("Submit"):
    st.write(f"You entered: {usernumber}")
    reset_input()  # Clear input field after submitting

line = pd.Series([usertext, usernumber], index = df.columns)

df = pd.concat([df, pd.DataFrame(line).T], axis = 0, ignore_index=True)

st.dataframe(df)
