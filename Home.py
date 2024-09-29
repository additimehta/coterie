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
                <h1>Welcome to MatchUP</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.image("./assets/logo.png",use_column_width=True)