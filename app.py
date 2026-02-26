import streamlit as st
from PIL import Image

st.title("Mi primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('Tequila.jpeg')
st.image(image, caption='Interfaces multimodales')

texto = st.text_input()
