import streamlit as st
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://technova:additi123@cluster0.aw8c8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(CONNECTION_STRING)
db = client['data']
collection = db['users']

# Display a title
st.title("MatchUP: Grow your network, one match at a time")

# Main app content
st.write("Main app content goes here.")

with st.sidebar:
    titlecol1, titlecol2, titlecol3 = st.columns([1, 3, 1])  # Adjust the column widths as needed
    # Center text in the second column (col2)
    with titlecol2:
        st.markdown(
            """
            <style>
            .center-text {
                text-align: center;
            }
            </style>
            <div class="center-text">
                <h1>Welcome</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Create columns
    col1, col2 = st.columns([2, 1])

    # Center text in the second column (col2)
    with col2:
        st.markdown(
            """
            <style>
            .center-text {
                text-align: center;
            }
            </style>
            <div class="center-text">
                <h2>Emily Yee</h2>
                <h2>Emily Yee</h2>
                <p>Welcome to MatchUP</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # You can add content to other columns as well
    with col1:
        st.image("icon.png", caption="Profile Picture", width=150)