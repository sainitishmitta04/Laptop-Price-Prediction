import streamlit as st
import pandas as pd
from PIL import Image
from matplotlib import image
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "laptop.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "laptop_price.csv")


#Title of the home page
st.title(":blue[Flipkart Laptop Price Prediction Data App :desktop_computer]")
#Using header
st.header('By: :red[Mitta Sai Nitish]')


img = image.imread(IMAGE_PATH1)
st.image(img)

st.header("List of Laptops available in the Flipkart")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)


