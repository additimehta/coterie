import streamlit as st
from PIL import Image

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

   
    st.image("./assets/logo.png",use_column_width=True)

image = Image.open("./assets/resourcehub.png")
st.image(image, use_column_width=True)