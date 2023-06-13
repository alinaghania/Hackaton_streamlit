import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

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
        "Main page",
        "Interpretation of the data",
        "Statistics",
    ]
)

# Display image in Main page
if pages == "Main page":
    image_path = "/Users/alina/Desktop/Hackaton/Affiche Hackathon LMG Efrei V2.png"
    display_image(image_path)

# Display image in Interpretation of the data page
if pages == "Interpretation of the data":
    image_path1 = "/Users/alina/Desktop/Hackaton/1.png"
    display_image(image_path1)
    image_path2 = "/Users/alina/Desktop/Hackaton/2.png"
    display_image(image_path2)
    image_path3 = "/Users/alina/Desktop/Hackaton/3.png"
    display_image(image_path3)
    image_path4 = "/Users/alina/Desktop/Hackaton/4.png"
    display_image(image_path4)
    image_path5 = "/Users/alina/Desktop/Hackaton/6.png"
    display_image(image_path5)

# Display dataset download link and text in Statistics page
if pages == "Statistics":
    dataset_path = "/Users/alina/Desktop/Hackaton/data_1.csv"
    st.write("Here the clean dataset ^^")

    # Add "Le pétrole est notre target" in pink above the graphs
    st.markdown('<p style="text-align:center; color:pink; font-size:20px;">La consommation du pétrole est notre target</p>', unsafe_allow_html=True)

    st.download_button("Download Dataset", dataset_path)
    
    data = pd.read_csv(dataset_path, delimiter=',')
    sum_oil_consumption = data.groupby('year')['oil_consumption'].sum()

    fig, ax = plt.subplots()
    sum_oil_consumption.plot(kind='bar', ax=ax)
    ax.set_title('Consommation du pétrole par an')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Oil Consumption')

    st.pyplot(fig)

    continents = ['Africa', 'Asia Pacific', 'Australia', 'Central America', 'Eastern Africa',
                  'Europe (other)', 'Middle Africa', 'North America', 'South & Central America', 'World',
                  'Other Asia & Pacific', 'Other CIS', 'Other Caribbean', 'Other Middle East',
                  'Other Northern Africa', 'Other South America', 'Other Southern Africa', 'Europe']

    df_countries = data[~data['country'].isin(continents)]
    pays = ['France', 'United States', 'China', 'Germany', 'India']

    df_countries = df_countries[df_countries['country'].isin(pays)]

    fig2, ax2 = plt.subplots(figsize=(14, 6))
    ax2.bar(df_countries['country'], df_countries['oil_consumption'])
    ax2.set_title('Consommation de pétrole par pays')
    ax2.set_xlabel('Pays')
    ax2.set_ylabel('Consommation de pétrole')
    plt.xticks(rotation=90)
    st.pyplot(fig2)

    image_path13 = "/Users/alina/Desktop/Hackaton/7.png"
    display_image(image_path13)
    image_path14 = "/Users/alina/Desktop/Hackaton/8.png"
    display_image(image_path14)
    image_path15 = "/Users/alina/Desktop/00.png"
    display_image(image_path15)
