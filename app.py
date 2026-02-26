import streamlit as st

st.title("Mi primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('tequila_sunset.jpeg')
st.image(image, caption='Interfaces multimodales')
