import streamlit as st

# Display a title
st.title("MatchUP: Grow your network, one match at a time")

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
    