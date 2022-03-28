
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf 
from tensorflow import keras
from keras import datasets, layers, models


# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = 10
stroke_color = "white"
bg_color = "black"

cnn = tf.keras.models.load_model('cnn_essai')    
st.set_page_config(layout="centered", initial_sidebar_state="auto")   

st.header(" :slot_machine: Application de reconnaissance de chiffres")
st.subheader("Veuillez dessiner un chiffre compris entre 0 et 9")
st.text("")
st.text("")
# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=280,
    width=280,
    drawing_mode=drawing_mode,
    key="canvas",
)

done = st.button("Dessin terminé", help="Appuyez sur ce bouton pour valider votre dessin et voir la prédiction")
if done:
    st.balloons()
    im = Image.fromarray(canvas_result.image_data)
    print(im.size)
    im = tf.image.resize(im, [28, 28])
    #print(im.size)
    im = np.asarray(im)[:,:,:3]
    im = np.expand_dims(im, axis=0)

    print(im.shape)
    #im.save("image.png")
    pred = cnn.predict(im)
    st.write("Le chiffre prédit est :" , np.argmax(pred))

    st.write([x for x in pred.tolist()[0]])
    fig = plt.figure(figsize=(12, 12))
    plt.barh(range(10), [x for x in pred.tolist()[0]], align='center')
    plt.yticks(range(10), [x for x in range(10)])
    plt.xlabel("Score")
    plt.ylabel("Chiffres")
    plt.title("Prédictions")
    st.pyplot(fig)

