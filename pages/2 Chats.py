import streamlit as st

import random
import time

st.title("Maria Smith")


# Get question from user
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display "connection" response in chat message container
    with st.chat_message("assistant"):
            st.markdown("Hi Emily! Nice to meet you! Of course, I'm happy to help!")


with st.sidebar:
    titlecol1, titlecol2, titlecol3 = st.columns([1, 3, 1])  # Adjust the column widths as needed

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

    st.image("./assets/logo.png", use_column_width=True)
    