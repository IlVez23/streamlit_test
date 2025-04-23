# Login Form

import streamlit as st

import requests
from datetime import datetime, timedelta


API_URL = "https://your-cloud-run-app-url"  # Update with deployed FastAPI backend

st.title("User Page")

# Registration Form
st.subheader("Register New User")
new_email = st.text_input("New Email")
new_password = st.text_input("New Password", type="password")

if st.button("Register"):
    res = requests.post(f"{API_URL}/register", json={"email": new_email, "password": new_password})
    if res.status_code == 200:
        st.success("User created successfully!")
    else:
        st.error(res.json().get("detail", "Registration failed"))


st.subheader("Login")
login_email = st.text_input("Email")
login_password = st.text_input("Password", type="password")

if st.button("Login"):
    res = requests.post(f"{API_URL}/login", json={"email": login_email, "password": login_password})
    if res.status_code == 200:
        token = res.json()["access_token"]
        st.session_state["token"] = token
        st.success("Logged in successfully!")
    else:
        st.error("Invalid credentials")

# Get protected data
if "token" in st.session_state:
    headers = {"Authorization": f"Bearer {st.session_state['token']}"}
    res = requests.get(f"{API_URL}/users", headers=headers)
    if res.status_code == 200:
        st.json(res.json())
    else:
        st.error("Access denied")
