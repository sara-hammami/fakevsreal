import streamlit as st
from PIL import Image
import numpy as np
import cv2 
import tensorflow as tf 
from tensorflow.keras.models import load_model
# Custom CSS for styling the title

def preprocess_image(image_path):
                img = Image.open(image_path)
                img = img.resize((128, 128))  # Resize the image to 128x128
                img = np.array(img)  # Convert the PIL image to a NumPy array

                img = img / 255.0
                img = np.expand_dims(img, axis=0)  # Add batch dimension
                return img
def main():
    
    title_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">AI Generated Image Face Detection</h2>

    </div>
    """
    st.markdown(title_temp, unsafe_allow_html=True)
    st.title("")
    st.write("This is a demo of a AI generated  detection app using a CNN model trained on the REAL/FAKE Image Faces  dataset.")
    st.write("Upload aFace image to see if it's fake or not.")
    st.write("")
    model = load_model('fakevsreal_weights.h5')

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Preprocess the uploaded image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        img = preprocess_image(uploaded_file)
        if st.button("Test"):
        # Make prediction using the loaded model
            prediction = model.predict(img)

            # Convert the prediction to human-readable labels
            class_labels = ["Real", "Fake"]
            result = class_labels[np.argmax(prediction)]

            # Display the result
            with st.markdown(
                f'<div style="background-color:#f4f4f4;padding:10px;border-radius:10px;">'
                f'<h2 style="color:#333;font-size:18px">Result: {result}</h2>'
                f'<p style="color:#555;">Probability: {prediction[0][np.argmax(prediction)]:.2f}</p>'
                f'</div>',
                unsafe_allow_html=True
            ):
                pass
        #st.write(f"Prediction: {result} (Probability: {prediction[0][np.argmax(prediction)]:.2f})")
   
if __name__ == '__main__':
    main()