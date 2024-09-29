import streamlit as st

col1, col2 = st.columns([1, 2])

with col1:
    st.image("Emily.jpg", use_column_width=True)
    st.button("Edit photo", use_container_width=True)

with col2:
    st.text_input("First Name", value="Emily")
    st.text_input("Last Name", value="Yee")
    st.number_input("Age", min_value=16, max_value=100, value=18)
    st.text_input("I'm looking for", value="Advice/Mentorship, Networking")
    st.text_input("Industry", value="Technology")
    st.text_input("Occupation", value="Student")
    st.text_input("Company/School", value="University of Waterloo")
    st.text_area("Bio", value="I love hackathons!!")
    st.text_input("Interests", value="Cooking, Traveling, Cycling")
