import streamlit as st
import pandas as pd
from PIL import Image

st.title("Hello welcome to the Hackaton- Day")
st.write('Hello, ! ' ' :sunglasses: ', 20, 'or nothing')

# Function to display image
def display_image(image_path):
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

# Sidebar selection
pages = st.sidebar.selectbox(
    "CHOOSE A PAGE",
    [
        "Interpretation of the data",
        "Statistics",
    ]
)

# Display image in Interpretation of the data page
if pages == "Interpretation of the data":
    image_path = "/Users/alina/Desktop/Hackaton/Affiche Hackathon LMG Efrei V2.png"
    display_image(image_path)

    st.write("")

    image_path1 = "/Users/alina/Desktop/Hackaton/1.png"
    display_image(image_path1)

    st.write("")

    image_path2 = "/Users/alina/Desktop/Hackaton/2.png"
    display_image(image_path2)

    st.write("")

    image_path3 = "/Users/alina/Desktop/Hackaton/3.png"
    display_image(image_path3)

    st.write("")

    image_path4 = "/Users/alina/Desktop/Hackaton/4.png"
    display_image(image_path4)

    st.write("")

    image_path5 = "/Users/alina/Desktop/Hackaton/6.png"
    display_image(image_path5)
