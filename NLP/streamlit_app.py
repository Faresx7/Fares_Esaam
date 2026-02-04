import streamlit as st
from src.user_predicting import user_prediction
from streamlit_chatbox import *
import pickle
import src
import os
import random

from src import clean_text 



# ===== PURE BLUE GLASS UI (NO BACKGROUND) =====
st.markdown("""
<style>

/* ---------- Remove App Background ---------- */
.stApp {
    background: transparent;
}

/* ---------- Glass Welcome Banner ---------- */
.glass-banner {
    margin: 25px 0 30px 0;
    padding: 28px;
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    letter-spacing: 1px;
    color: #e8f6ff;

    border-radius: 26px;

    background: linear-gradient(
        135deg,
        rgba(0, 140, 255, 0.22),
        rgba(0, 90, 200, 0.10)
    );

    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);

    border: 1px solid rgba(120, 200, 255, 0.45);

    box-shadow:
        0 0 25px rgba(0, 160, 255, 0.65),
        inset 0 0 25px rgba(180, 230, 255, 0.25);

    animation: blueGlow 3s ease-in-out infinite alternate;
}

/* ---------- Blue Glow Animation ---------- */
@keyframes blueGlow {
    from {
        box-shadow:
            0 0 18px rgba(0, 140, 255, 0.45),
            inset 0 0 18px rgba(180, 230, 255, 0.20);
    }
    to {
        box-shadow:
            0 0 45px rgba(0, 180, 255, 0.95),
            inset 0 0 32px rgba(200, 240, 255, 0.35);
    }
}

/* ---------- Glass Buttons ---------- */
.stButton>button {
    width: 100%;
    border-radius: 18px;
    padding: 12px 14px;
    font-size: 16px;
    font-weight: 600;
    color: #eaf7ff;

    background: linear-gradient(
        135deg,
        rgba(0, 150, 255, 0.25),
        rgba(0, 90, 200, 0.12)
    );

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    border: 1px solid rgba(140, 210, 255, 0.5);

    box-shadow:
        0 0 18px rgba(0, 150, 255, 0.55),
        inset 0 0 18px rgba(200, 240, 255, 0.25);

    transition: all 0.3s ease-in-out;
}

/* Button Hover Glow */
.stButton>button:hover {
    transform: scale(1.06);
    box-shadow:
        0 0 40px rgba(0, 180, 255, 1),
        inset 0 0 26px rgba(220, 245, 255, 0.4);
}

/* ---------- Sidebar Glass ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        rgba(0, 140, 255, 0.22),
        rgba(0, 90, 200, 0.10)
    ) !important;

    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);

    border-right: 1px solid rgba(120, 200, 255, 0.45);
}

/* ---------- Sidebar Text ---------- */
section[data-testid="stSidebar"] * {
    color: #eaf7ff;
}

</style>
""", unsafe_allow_html=True)

# ---------- Welcome Banner ----------
st.markdown('<div class="glass-banner">Welcome 👨🏼‍💻</div>', unsafe_allow_html=True)





# Home screen
#! Chat Box
chat_box = ChatBox(
    use_rich_markdown=True,
    user_theme="green",
    assistant_theme="blue"
)

chat_box.init_session()

with st.sidebar:
    st.title('Settings')


    st.divider()
    if st.button("Clear chat"):
        chat_box.init_session(clear=True)
        st.rerun()
    
    
    if st.button("🎈🎈🎈"):
        st.balloons()

    st.divider()
    st.info("This model uses the ***Logistic regression*** model for predicting you future field based on you text")


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