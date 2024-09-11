import streamlit as st
from PIL import Image
from model import load_prediction_model, predict_image
from style import apply_custom_style

# Load the trained model
model = load_prediction_model()

# Streamlit app title
st.title("Gender and Age Prediction App")

# Apply custom styles
apply_custom_style()

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
button_pressed = st.button("Predict")

if button_pressed:
    if uploaded_file is not None:
        # Open the uploaded image
        img = Image.open(uploaded_file)
        
        # Display the uploaded image
        st.image(img, caption='Uploaded Image', use_column_width=True)
        
        # Predict and display results
        predict_image(img, model)
    else:
        st.write("Please upload an image file to get predictions.")
