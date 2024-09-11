import cv2
import numpy as np
from PIL import Image
import streamlit as st

# Load the pre-trained face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_and_crop_face(image_pil):
    # Convert PIL image to OpenCV format
    img = np.array(image_pil)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Convert the image to grayscale (Haar Cascade requires grayscale images)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If no faces are detected, return None
    if len(faces) == 0:
        st.write("No faces detected.")
        return None

    # Otherwise, crop the first detected face
    (x, y, w, h) = faces[0]
    cropped_face = img[y:y+h, x:x+w]

    # Convert the cropped face to a PIL Image
    cropped_face_pil = Image.fromarray(cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB))

    return cropped_face_pil

def preprocess_image(image_pil):
    # Convert the image to grayscale
    img = image_pil.convert('L')
    # Resize the image to 128x128 pixels
    img = img.resize((128, 128), Image.BILINEAR)  # Use Image.ANTIALIAS if using older PIL versions

    # Convert the image to a NumPy array
    img = np.array(img)
    
    # Normalize and reshape the image for model input
    img = img.reshape(1, 128, 128, 1) / 255.0

    return img
