from PIL import Image
import streamlit as st


def load_image(image_file):
    try:
        img = Image.open(image_file)
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
