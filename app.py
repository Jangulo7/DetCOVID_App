import streamlit as st
from PIL import Image
import requests
from datetime import datetime
import os

st.set_page_config(page_title="DetCOVID App v2", page_icon="🩺", layout="centered")

# --- Hero ---
hero_image = "https://images.unsplash.com/photo-1584036561566-baf8f5f1b144?fit=crop&w=1200&q=80"
st.image(hero_image, use_container_width=True)
st.markdown("<h1 style='text-align: center;'>Tecnología de Salud Predictiva</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- Body ---
st.markdown("## DetCOVID App")
st.markdown("La aplicación DetCOVID es una aplicación web fácil de usar que utiliza Redes neuronales convolucionales (CNN) avanzadas para clasificar las imágenes de radiografías de tórax en tres categorías distintas: SANO, COVID-19 y NEUMONÍA.")
st.markdown("También proporciona el porcentaje de confianza para cada predicción, lo que permite a los usuarios comprender qué tan seguro está el modelo sobre la clasificación dada.")
st.markdown("Cargue una imagen de radiografía de tórax para obtener el resultado de la predicción.")
st.markdown("---")

uploaded_image = st.file_uploader("📁 Cargar radiografía", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Cargue una radiografía", use_container_width=True)

    if st.button("Predict Result"):
        with st.spinner("Analyzing the image..."):
            url_backend = "https://covid-backend-x534.onrender.com/predict"
            files = {"file": (uploaded_image.name, uploaded_image.read(), uploaded_image.type)}

            try:
                response = requests.post(url_backend, files=files, timeout=30)  # Added timeout
                response.raise_for_status()
                result = response.json()
                st.success(f"**Clasificación:** {result['classification']}")
                st.info(f"**Confianza:** {result['confidence']}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error de comunicación con el backend: {e}")

# --- Feedback Section ---
st.markdown("---")
st.markdown("## 📝 Feedback")

st.markdown("""
Si tienes comentarios, sugerencias o encontraste algún problema, por favor envíanos tu opinión:
""")

form_html = """
<form action="https://formspree.io/f/xwplvgob" method="POST">
  <label>Tu correo:</label><br>
  <input type="email" name="email" required><br><br>
  <label>Comentario:</label><br>
  <textarea name="message" rows="5" required></textarea><br><br>
  <button type="submit">Enviar Feedback</button>
</form>
"""

st.markdown(form_html, unsafe_allow_html=True)
st.markdown("Tu correo no será compartido. El feedback será enviado de forma segura.")

# --- Footer --- (lo de abajo igual)

st.markdown("---")
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    footer_logo = "https://img.icons8.com/fluency/96/stethoscope.png"
    st.image(footer_logo, width=50)

with col2:
    st.markdown(
        f"""
        **Developed by:** [Johanna](https://www.linkedin.com/in/johannaangulo)  
        📅 March, {datetime.now().year}  
        **Contact:** [![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/johannaangulo)
        """,
        unsafe_allow_html=True
    )

with col3:
    st.write(" ")


