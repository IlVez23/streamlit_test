import streamlit as st



st.title("About Me")
# Set a custom background with a Japanese-style print pattern
def set_background():
    st.markdown(
        """
        <style>
        body {
            background-image: '/Users/andreaverbaro/Documents/GitHub/streamlit_test/images/background.jpg';
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()
st.header("Welcome to My First Streamlit App!")
st.write("""
Hi, I'm Andrea! I'm taking my first steps into the world of app development with Streamlit. 
My ultimate goal is to create a **Dream's Carousel Diary App**, where users can record, revisit, and cherish their dreams.

This journey is all about learning, experimenting, and bringing my ideas to life. 
Thank you for stopping by and being part of this exciting adventure!
""")