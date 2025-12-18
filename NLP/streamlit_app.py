import streamlit as st
from src.user_predicting import user_prediction
from streamlit_chatbox import *
import pickle
import src
import os
import random

from src import clean_text 

# Home screen
st.set_page_config(page_title="Career Advisor", page_icon="🤖")

#! Chat Box
chat_box = ChatBox(
    use_rich_markdown=True,
    user_theme="green",
    assistant_theme="blue"
)

chat_box.init_session()

with st.sidebar:
    st.title("Settings")
    if st.button("Clear chat"):
        chat_box.init_session(clear=True)
        st.rerun()
    
    st.divider()
    st.info("This model uses the ***Logistic regression*** model for predicting you future field based on you text")


st.title("Welcome 🤖")
chat_box.output_messages()

query=st.chat_input('Please enter you interest')
if query:
    chat_box.user_say(query)
    
    prediction=user_prediction(query)

        
    responses = [
            f"Based on my analysis, the perfect field for you is **{prediction}**! 🚀",
            f"I've crunched the numbers, and it looks like you belong in **{prediction}**. 🧠",
            f"Your interests strongly point towards a successful career in **{prediction}**. ✨",
            f"Exciting news! Your profile matches the requirements for **{prediction}** perfectly. 🎉",
            f"If I were you, I'd definitely explore the world of **{prediction}**. It suits you!",
            f"My AI brain suggests that you would thrive in the field of **{prediction}**. 🤖",
            f"You have the right mindset for **{prediction}**. Go for it!",
            f"It's clear from your description that **{prediction}** is your calling. 📞",            f"I've found a match! Your skills and interests lead straight to **{prediction}**.",
            f"Ready to start your journey?\nMy recommendation for you is **{prediction}**. 🏁"
]

        
    chat_box.ai_say([
        Markdown(random.choice(responses))
        ])

cols = st.columns(2)