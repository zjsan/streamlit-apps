import streamlit as st 

import streamlit as st
import time
"""Trying out first the Streamlit environment - Testing documenations for the development of CogniCraft"""


def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""

def set_send_input():
    st.session_state.send_input = True


def main():



    st.title("ZAI GPT 1.0 - An interactive chatbot for lonely people like me :(")
    chat_container = st.container()

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""

    user_input = st.text_input("Enter your message here", key ="user_input", on_change=set_send_input)    

    
    send_button = st.button("Send", key="send_button")
    if send_button or st.session_state.send_input:
        llm_response = "This is a response from the LLM model"
        
        with chat_container:
            st.chat_message("user").write(user_input)
            st.chat_message("ai").write("here is an answer")

    

if __name__ == "__main__":
    main()