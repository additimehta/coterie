import streamlit as st
from pymongo import MongoClient

form = st.form("my_form")
CONNECTION_STRING = "mongodb+srv://technova:<db_password>@cluster0.aw8c8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(CONNECTION_STRING)



db = client['data']
collection = db['users']

# names: MatchUP, QuickConnect


form.header("Welcome to MatchUP")
form.caption("We want to know all about you!")


with st.form(key='user-info-form'):
    firstname = form.text_input("First Name")
    lastname = form.text_input("Last Name")
    photo = form.file_uploader("Profile photo", type=['png', 'jpg', 'jpeg', 'img', 'heic', 'hevc', 'tiff', 'tif', 'raw', 'webp', 'svp'])
    age = form.number_input("Age", min_value=16, max_value=100, value=None)
    form.write("I am looking for")
    form.checkbox("Advice/Mentorship")
    form.checkbox("Share my knowledge")
    form.checkbox("Network")



 submit_button = st.form_submit_button("Submit")

 if submit_button:
        user_data = {
            "firstname": firstname,
            "lastname": lastname,
            "age": age,
            "looking_for": {
            "advice": advice,
            "knowledge": knowledge,
            "network": network
            }
        }

if photo is not None:
    photo_bytes = photo.read() 
    encoded_photo = base64.b64encode(photo_bytes).decode('utf-8') 
    user_data["photo"] = encoded_photo 

collection.insert_one(user_data)
st.success("Your information has been saved successfully!")
