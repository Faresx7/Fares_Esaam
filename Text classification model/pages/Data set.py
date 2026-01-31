import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from src.cleaning_text import clean_text

st.set_page_config(page_title="Dataset Viewer", layout="wide")


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
    ">📊 Student Dataset & Preprocessing</h2>
</div>
""", unsafe_allow_html=True)



data=pd.read_excel("Students_Dataset.xlsx", engine="openpyxl")
st.subheader("🔹 Original Dataset")
st.dataframe(data)
st.success(f'The data have **{data.shape[0]}** raws')

st.divider()
st.subheader('♦️Preprocessed Data')

data1=pd.read_excel("cleaned_Dataset.xlsx", engine="openpyxl")

st.dataframe(data1)
st.success('All data loaded successfully🎉')