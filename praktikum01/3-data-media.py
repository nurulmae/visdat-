import streamlit as st

st.write("Displaying an Images")

# Displaying Image by specifying path
st.image("D:/GreenSeaTurtle-2.jpg")

# Image Courtesy by unplash
st.write("Image Courtesy: unplash.com")

import streamlit as st

# Image Courtesy
st.write("Displaying Multiple Images")

# listing out animal images
animal_images = [
    'D:/animal1.jpg',
    'D:/animal2.jpg',
    'D:/animal3.jpg',
    'D:/animal4.jpg',
]

# Displaying Multiple images with width 150
st.image(animal_images, width=150)

# Image Courtesy
st.write("Image Courtesy: Unsplash")

import streamlit as st
import base64

# function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()

    st.write("Image Courtesy: unplash")
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

st.write("Background Image")

# Calling Image in function
# NOTE: Replace the path with your actual image path
add_local_background_image('D:/animal1.jpg')

import streamlit as st
from PIL import Image

# St.title: Original Image
original_image = Image.open("D:/animal1.jpg")
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600x400
resized_image = original_image.resize((600, 400))

# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)
