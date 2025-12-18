import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config('Main', layout='wide')
st.sidebar.title('This is sidebar')

tab1,tab2,tab3=st.tabs(['Tab 1','Tab 2','Tab 3'])

with tab1:
    st.write('# This is Tab 1')
    st.text('this is text')
    st.divider()
    col1,col2=st.columns(2)
    with col1:
        st.write('# This column 1')
    with col2:
        st.write('# This column ')


with tab2:
    st.write('# This is Tab 2')
    st.text('this is text')
    st.divider()
    st.balloons()
with tab3: 
    st.write('# What the fuck are you doing here?!!!!!!!, one man')