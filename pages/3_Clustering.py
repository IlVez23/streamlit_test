import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/users/"

st.title("User Management")

new_user = st.text_input("Enter new user name")

if st.button("Add User"):
    response = requests.post(API_URL, json={"name": new_user})
    if response.status_code == 200:
        st.success(f"User {new_user} added!")
    else:
        st.error("Error adding user")

if st.button("Load Users"):
    response = requests.get(API_URL)
    if response.status_code == 200:
        users = response.json()
        for user in users:
            st.write(f"👤 {user['name']}")
    else:
        st.error("Error fetching users")
