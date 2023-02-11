import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("model.h5")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    result = model.predict(img_array)
    
    argmax_index = np.argmax(result, axis = 1)
    
    if argmax_index[0] == 0:
        st.image(image, caption="predicted: Cat")
    else:
        st.image(image, caption="predicted: Dog")
    