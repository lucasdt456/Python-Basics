import os

import cv2
import numpy as np
import tensorflow as tf
from streamlit_drawable_canvas import st_canvas

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA Digit Recognizer")
st.title("Reconocedor de Dígitos en Tiempo Real")
st.write("Dibuja un número del 0 al 9 en el recuadro negro.")

# 1. Cargar el modelo guardado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model_mnist.keras")


@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model(MODEL_PATH)


model = load_my_model()
# 2. Crear el lienzo (Canvas) para dibujar
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=20,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    return_image_data=True,
    key="canvas",
)

# 3. Procesar el dibujo y predecir
if canvas_result is not None and hasattr(canvas_result, "image_data") and canvas_result.image_data is not None:
    try:
        # 1. Extraer la matriz de la imagen (viene en formato RGBA de 4 canales)
        img_data = canvas_result.image_data.astype(np.uint8)

        # 2. Convertir de RGBA a Escala de Grises PRIMERO
        gray_img = cv2.cvtColor(img_data, cv2.COLOR_RGBA2GRAY)

        # 3. Redimensionar a 28x28 píxeles (formato MNIST) usando INTER_AREA para mejor calidad
        img_resized = cv2.resize(gray_img, (28, 28), interpolation=cv2.INTER_AREA)

        # 4. Normalizar entre 0 y 1
        img_normalized = img_resized / 255.0 

        # Predicción
        pred = model.predict(img_normalized.reshape(1, 28, 28, 1))
        clase = np.argmax(pred)
        confianza = np.max(pred)

        # 4. Mostrar resultados con Umbral de Seguridad
        st.subheader(f"Resultado: {clase}")

        if confianza < 0.80:
            st.warning(f"Confianza baja ({confianza:.2%}). ¿Podrías dibujar más claro?")
        else:
            st.success(f"Confianza alta: {confianza:.2%}")

        st.bar_chart(pred[0])  # Visualización de probabilidades

    except Exception as e:
        st.info("Dibuja un número en el cuadro negro para comenzar la predicción.")
