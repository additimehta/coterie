import streamlit as st
import time

st.title("Maria Smith")

# Pre-existing messages
with st.chat_message("user"):
    st.markdown("Hi Maria! I saw your post about your Hackathon last Tuesday and thought it was really cool. I'd love to get coffee sometime!")

with st.chat_message("assistant"):
    st.markdown("Hey Emily! Sure, I'd be down! Does next Monday at the Math C&D work for you?")

with st.chat_message("user"):
    st.markdown("Yes sounds great! See you then!")

# Get question from user
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    time.sleep(1)
    # Display "connection" response in chat message container
    with st.chat_message("assistant"):
            st.markdown("Of course, happy to help :) Let me know if you have any other questions!")


with st.sidebar:
    titlecol1, titlecol2, titlecol3 = st.columns([1, 3, 1])  # Column width ratios

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
    