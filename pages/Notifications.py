import streamlit as st
from datetime import datetime

# Display a title
st.title("MatchUP: Grow your network, one match at a time")





def add_notifications(message):
    st.session_state.notifications.append(message)


def show_notifications():
    st.title("Notifications")
    if "notifications" not in st.session_state or not st.session_state.notifications:
        st.info("No notifications yet.")
        return
    
    for notification in st.session_state.notifications:
        st.success(notification)


def send_request(target_email, sender_email):
   user = collection.find_one({"email": target_email})
   sender_email = collection.find_one({"email": sender_email})
   
   notifications = {
       "message": f"You have received a connection request from Chloe.",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "connection_request"
   }


show_notifications()



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
       st.image("./assets/icon.png", caption="Profile Picture", width=150)