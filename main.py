import streamlit as st
import pandas as pd
import numpy as np
from signup import user_registration

import streamlit as st
from database import users_collection
from PIL import Image
import base64

def load_user_profiles():
    users = list(users_collection.find())
    return users

def load_css():
   css = """
    <style>
       .user-card {
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 16px;
            margin: 20px 0;
            display: flex;
            align-items: center;
            gap: 20px;
    
       }

       .profile-photo {
           border-radius: 20px; 
            width: 200px;
            height: 250px; 
            object-fit: cover; 
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            margin-left: -10px; 
        }

        .user-info {
            
        }
    </style>

    """
   st.markdown(css, unsafe_allow_html=True)

def display_user_profile(user):
     
     try:
        profile_photo = user['photo']
        first_name = user['firstname']
        last_name = user['lastname']
        age = user['age']
        bio = user['bio']  
        interests = ', '.join(user['interests'])
     except KeyError as e:
        st.error(f"Missing user data: {e}")
        return
 

     st.markdown(f"""
        <div class="user-card">
            <img src='data:image/jpeg;base64,{profile_photo}' class='profile-photo' />
            <div class="user-info">
                <h3>{first_name} {last_name}</h3>
                <p><strong>Age:</strong> {age}</p>
                <p class="bio"><strong>Bio:</strong> {bio}</p>
                <p><strong>Interests:</strong> {interests}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def main():
    st.title("MatchUP - Swipe to Connect")
    load_css()

    users = load_user_profiles()

    if not users:
        st.write("No users to display.")
        return

    # Current user index
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0

    user = users[st.session_state.current_index]

    display_user_profile(user)

    # Buttons for swiping
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ignore"):
            st.session_state.current_index += 1
            if st.session_state.current_index >= len(users):
                st.session_state.current_index = 0  

    with col2:
        if st.button("Connect!"):
           
            st.session_state.current_index += 1
            if st.session_state.current_index >= len(users):
                st.session_state.current_index = 0  

    # Display remaining users
    if st.session_state.current_index < len(users):
        st.write(f"You have {len(users) - st.session_state.current_index} users remaining.")
    else:
        st.write("No more users to swipe!")

if __name__ == "__main__":
    main()






def main():
    st.sidebar.title("MatchUP")
    app_mode = st.sidebar.selectbox("Choose the app mode", ["Sign Up"])

    if app_mode == "Sign Up":
       user_registration()


    

if __name__ == "__main__":
    main()



