import streamlit as st

form = st.form("my_form")

# names: MatchUP, QuickConnect

form.header("Welcome to MatchUP")
form.caption("We want to know all about you!")
firstname = form.text_input("First Name")
lastname = form.text_input("Last Name")
photo = form.file_uploader("Profile photo", type=['png', 'jpg', 'jpeg', 'img', 'heic', 'hevc', 'tiff', 'tif', 'raw', 'webp', 'svp'])
age = form.number_input("Age", min_value=16, max_value=100, value=None)
form.write("I am looking for")
form.checkbox("Advice/Mentorship")
form.checkbox("Share my knowledge")
form.checkbox("Network")

# Every form must have a submit button.
form.form_submit_button("Submit")
