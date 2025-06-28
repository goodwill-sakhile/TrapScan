# app/views.py

import streamlit as st

def render_home():
    st.subheader("Welcome to Trapscan ")
    st.write("""
        Trapscan is an intelligent food identification tool powered by a custom-trained Convolutional Neural Network (CNN).
        Just upload a food image and let AI tell you what's on your plate!
    """)
    st.image("assets/logo.png", use_column_width=True)
