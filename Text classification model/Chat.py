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

st.markdown("""
<div style="
    border: 2px solid rgba(255, 255, 255, 0.25);
    padding: 25px;
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    text-align: center;
    font-family: 'Arial', sans-serif;
">
    <h2 style="
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.5), 0 0 15px rgba(255,255,255,0.3);
    ">👨‍💻 Student Career Prediction</h2>
</div>
""", unsafe_allow_html=True)




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
    
    if st.button("❓❓❓❓"):
        st.balloons()
        
    st.divider()
    st.success("This model uses the ***Logistic regression*** model for predicting your future field based on your text")
chat_box.output_messages()



st.markdown("""
<style>
/* تعديل زر الإدخال في Chat Input */
div[data-testid="stForm"] button, 
div.stButton>button {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    border: 2px solid rgba(255, 255, 255, 0.25);
    border-radius: 20px;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    transition: all 0.3s ease;
    cursor: pointer;
}

/* تأثير عند المرور على الزر */
div[data-testid="stForm"] button:hover, 
div.stButton>button:hover {
    background: rgba(255, 255, 255, 0.2);
    box-shadow: 0 12px 40px rgba(31, 38, 135, 0.5);
}
</style>
""", unsafe_allow_html=True)


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