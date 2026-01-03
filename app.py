import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("🤖 Simple Chatbot")
st.write("Talk to your friendly chatbot below!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send"):
    if user_input:
        bot_response = get_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", bot_response))

for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
