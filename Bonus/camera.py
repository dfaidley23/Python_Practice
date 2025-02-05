import streamlit as st
from PIL import Image


with st.expander("Start Camera"):

    # starts camera
    camera_image = st.camera_input("Camera")


if camera_image:

    # create an image 
    img  = Image.open(camera_image)

    # converts image to grey scale
    gray_img = img.convert("L")

    # displayes image converted
    st.image(gray_img)