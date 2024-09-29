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
                <p>Welcome to MatchUP</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # You can add content to other columns as well
    with col1:
        st.image("icon.png", caption="Profile Picture", width=150)