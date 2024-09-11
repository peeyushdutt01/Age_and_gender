import numpy as np
from tensorflow.keras.models import load_model
from image_utils import detect_and_crop_face, preprocess_image
import streamlit as st

# Define the image size and gender dictionary
IMG_SIZE = (128, 128)
gender_dict = {0: "Female", 1: "Male"}

def load_prediction_model():
    # Load the trained model
    model = load_model(r"E:\Peeyush\coding\Python\project\Gender&Age\models\AGpredv2.keras")
    return model

def predict_image(image_pil, model):
    # Detect and crop the face
    cropped_face_image = detect_and_crop_face(image_pil)

    if cropped_face_image is None:
        st.write("Face detection failed. Please try another image.")
        return

    # Preprocess the cropped face
    custom_ip = preprocess_image(cropped_face_image)

    # Predict gender and age
    pred = model.predict(custom_ip)
    pred_gender = gender_dict[int(round(pred[0][0][0]))]
    pred_age = round(pred[1][0][0])

    # Display the results
    st.write(f"**Predicted Gender:** {pred_gender}")
    st.write(f"**Predicted Age:** {pred_age} years")
    
    # Display the cropped face image with predictions
    st.image(cropped_face_image, caption=f'Gender: {pred_gender}, Age: {pred_age}')
