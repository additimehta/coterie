import streamlit as st
from pymongo import MongoClient
import base64
import hashlib
from database import users_collection

collection = users_collection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@st.dialog("Welcome to MatchUP")
def signUp():
    form = st.form("user_info_form")
    form.header("Welcome to MatchUP")
    form.caption("We want to know all about you!")

    firstname = form.text_input("First Name")
    lastname = form.text_input("Last Name")
    email = form.text_input("Email")
    location = form.text_input("Location")
    photo = form.file_uploader("Profile photo", type=['png', 'jpg', 'jpeg', 'img', 'heic', 'hevc', 'tiff', 'tif', 'raw', 'webp', 'svp'])
    age = form.number_input("Age", min_value=16, max_value=100, value=None)
    form.write("I am looking for")
    advice = form.checkbox("Advice/Mentorship")
    knowledge = form.checkbox("Sharing my knowledge")
    network = form.checkbox("Networking")

    industry_options = ['Aerospace', 'Agriculture', 'Automotive', 'Business', 'Banking', 'Biotechnology', 
                        'Chemicals', 'Construction', 'Consulting', 'Consumer Goods', 'Cybersecurity', 
                        'Defense', 'Education', 'Energy', 'Entertainment', 'Environmental Services', 
                        'Fashion', 'Finance', 'Food and Beverage', 'Government', 'Healthcare', 
                        'Hospitality', 'Information Technology', 'Insurance', 'Logistics', 
                        'Manufacturing', 'Media', 'Mining', 'Nonprofit', 'Pharmaceuticals', 
                        'Private Equity', 'Professional Services', 'Real Estate', 'Retail', 
                        'Technology', 'Telecommunications', 'Tourism', 'Transportation', 'Utilities', 
                        'Venture Capital', 'Waste Management', 'Wholesale']

    industry = form.multiselect("Industry", industry_options)
    occupation = form.text_input("Current occupation")
    company = form.text_input("Company/School")
    bio = form.text_area("Tell us about yourself!")

    interests_list = ['Reading', 'Traveling', 'Cooking', 'Gardening', 'Photography', 'Music', 
                    'Sports', 'Hiking', 'Art', 'Writing', 'Fitness', 'Technology', 
                    'Video Games', 'Dancing', 'Fishing', 'Crafting', 'Fashion', 'Theater', 
                    'Volunteering', 'Yoga', 'Birdwatching', 'Knitting', 'Painting', 
                    'Cooking', 'Camping', 'Swimming', 'Cycling', 'Running', 'Podcasting', 
                    'Martial Arts', 'Sculpting', 'Surfing', 'Travel Blogging', 'Astronomy', 
                    'Collecting', 'Board Games', 'Wine Tasting', 'Journaling', 'Mindfulness', 
                    'Homebrewing', 'Rock Climbing', 'Pottery', 'Graphic Design', 
                    'Interior Design', 'History', 'Languages', 'Animal Care', 
                    'Motorsports', 'Sailing', 'Scuba Diving', 'Calligraphy', 'Stand-up Comedy']

    interests = form.multiselect("Interests", interests_list)

    password = form.text_input("Password", type="password")
    submit_button = form.form_submit_button("Submit")

    if submit_button:
        user_data = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "location": location,
            "age": age,
            "looking_for": {
                "advice": advice,
                "knowledge": knowledge,
                "network": network
            },
            "industry": industry,
            "occupation": occupation,
            "company": company,
            "bio": bio,
            "interests": interests,
            "password": hash_password(password)  # Hash the password before saving
        }
        
        if photo is not None:
            photo_bytes = photo.read()
            encoded_photo = base64.b64encode(photo_bytes).decode('utf-8')
            user_data["photo"] = encoded_photo

        collection.insert_one(user_data)
        st.success("Your information has been saved successfully!")
        st.session_state.show_signup = False
        st.session_state.show_login = True


@st.dialog("Welcome to MatchUP")
def login():
    st.header("Login")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = collection.find_one({"email": email})
        
        if user and user["password"] == hash_password(password):
            st.success(f"Welcome back, {user['firstname']}!")
            st.session_state.user = user
#            st.session_state.is_logged_in = True
    
#            if st.session_state.is_logged_in:
#                print("is logged in")
        else:
            st.error("Invalid email or password")

    st.subheader("New user?")
    newsignup = st.button("Sign up")

    if newsignup:
        st.session_state.show_signup = True
        st.session_state.show_login = False
        st.rerun()



def display_users():
    if st.checkbox("Show existing users"):
        users = collection.find()
        for user in users:
            st.write(f"Name: {user['firstname']} {user['lastname']}, Age: {user['age']}, Location: {user['location']}")
            st.write(f"Industry: {user['industry']}, Occupation: {user['occupation']}, Company/School: {user['company']}")
            st.write(f"Bio: {user['bio']}, Interests: {user['interests']}")
            if 'photo' in user:
                st.image(base64.b64decode(user['photo']), caption='Profile Photo', use_column_width=True)
