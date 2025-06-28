# app/routes.py

import streamlit as st
from app.views import render_home
from PIL import Image

def start_app():
    st.set_page_config(page_title="Trapscan", layout="centered")
    st.title(" Trapscan - Food Image Identifier")

    menu = ["Home", "Upload", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        render_home()

    elif choice == "Upload":
        st.subheader("Upload a Food Image")
        uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "png", "jpeg"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            st.write("Classifying...")

            from api.predict import classify_image
            label, confidence = classify_image(image)

            st.success(f"Prediction: **{label}** ({confidence*100:.2f}%)")

    elif choice == "About":
        st.info("Trapscan uses a custom CNN model to detect food items from images.")
