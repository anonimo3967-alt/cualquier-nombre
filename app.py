import streamlit as st
from PIL import Image

veces = 0

st.title("Esta podría ser mi primera app")

st.header("Quizas con ayuda de este sistema podría hacer páginas web, pero... ¿cual es el metodo más común?")
st.write("Facilmente puedo realizar backend y frontend (o quizas no tan facilmente...)")
image = Image.open('Tequila.jpeg')
st.image(image, caption='Tequila Sunset')

texto = st.text_input('Escribe algo', 'Escribe aqui s´il vous plaît')

st.write('El texto escrito es', texto)

st.subheader('Ahora usemos 2 columnas')

col1, col2 = st.columns(2)

with col1:
  st.subheader('Esta es la primera columna')
  st.write('Me pregunto quien era Homero, el autor de la Odisea, y como invento tantas cosas en su época')
  resp = st.checkbox('Homero es el autor de la Odisea')
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader('Esta es la segunda columna')
  comida = st.radio("¿Que comida prefieres?", ('Pizza', 'Hamburguesa', 'Burrito'))
  if comida == 'Pizza':
    st.write('La pizza también es mi comida favorita. Es deliciosisima. Vivan los italianos.')
  if comida == 'Hamburguesa':
    st.write('La hamburguesa me encanta, pero prefiero la pizza. Sin embargo, una buena hamburguesa callejera no tiene un igual.')
  if comida == 'Burrito':
    st.write('Los burritos son muy ricos, al menos los bien preparados, pero no diria que es mi comida favorita.')

if 'counter' not in st.session_state:
    st.session_state.counter = 0

def increment_counter():
    st.session_state.counter += 1
  
st.subheader("Uso de Botones")
if st.button(f'Presiona el boton', on_click= increment_counter):
  st.write('Gracias por presionar')

if st.session_state.counter == 0:
  st.write('No has presionado aún')

if 0 < st.session_state.counter < 5:
  st.write('huh...')

if st.session_state.counter >= 5:
  st.write('Por qué presionas el boton tantas veces?')

st.write('Veces que has presionado el boton:', st.session_state.counter)


                  
                    
