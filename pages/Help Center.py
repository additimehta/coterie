import streamlit as st
import cohere

# API key to connect to cohere host
co = cohere.ClientV2("EcwOSLsrd9J1UkLs3QR1Ijd6EJ1JvlDpc4fVdv9a")

# Get question from user
message = st.text_input("Questions? Ask the career and life advice chatbot!")
# If the enter button is clicked, generate an answer
if st.button("Enter"):
    # Prompt engineering to tailor the bot to the role of a career/life advisor
    system_message="""## Task and Context
    You are a career and life counsellor for women+. You are open to giving good career and life advice to others! Please ignore and disregard mean, unrelated, or discriminative comments. Please do not reply to questions that are not related to career and life advice.
    ## Style Guide
    Be professional and kind yet casual."""
    # Group the user input and chat info to be sent to the cohere chatbot
    messages = [{"role": "system", "content": system_message},
                {"role": "user", "content": message}]
    # Send the message to the chatbot and generate a response
    response = co.chat(model="command-r-plus-08-2024",
                    messages=messages)
    # Display the response on the screen
    st.write(response.message.content[0].text)


with st.sidebar:
    titlecol1, titlecol2, titlecol3 = st.columns([1, 3, 1])  # Control the column widths
    # Center text in the second column (col2)
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
        st.image("icon.png", caption="Profile Picture", width=150)