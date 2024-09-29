import streamlit as st
from datetime import datetime


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Edu+AU+VIC+WA+NT+Guides:wght@400..700&family=Fredoka:wght@300..700&display=swap');

    
    .network-title {
     font-family: 'Fredoka';
     font-size: 50px;
     font-weight:300
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="network-title">MatchUP: Grow your network, one match at a time</h1>', unsafe_allow_html=True)




def add_notifications(message):
    st.session_state.notifications.append(message)


def show_notifications():
    st.title("Notifications")
    if "notifications" not in st.session_state or not st.session_state.notifications:
        st.info("No notifications yet.")
        return
    
    for notification in st.session_state.notifications:
        st.success(notification)


def send_request():
   
   notifications = {
       "message": f"You have received a connection request from Chloe Wei.",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "connection_request"
   }

   add_notifications(notifications['message'])

show_notifications()


with st.container():
    st.write("You have a new connection request!")
    st.write("Message: You have received a connection request from Chloe Wei.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Accept", use_container_width=True):
            st.success("You accepted the connection request!")

    with col2:
        if st.button("Decline", use_container_width=True):
            st.warning("You declined the connection request.")




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
