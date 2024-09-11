# Gender and Age Prediction App

This project is a web-based application built with Streamlit that predicts the gender and age of a person from a provided image. It uses a Convolutional Neural Network (CNN) model trained using Keras to perform the predictions. The app leverages OpenCV for face detection, and TensorFlow for deep learning predictions.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Gender Prediction**: Predicts whether a person is male or female.
- **Age Prediction**: Estimates the age of the person.
- **Face Detection**: Uses Haar Cascade Classifier to detect and crop the face from the uploaded image.
- **Interactive UI**: Built with Streamlit for an easy-to-use interface.

## Tech Stack

- **Programming Languages**: Python
- **Framework**: Streamlit
- **Libraries**: OpenCV, PIL (Python Imaging Library), TensorFlow, NumPy, Matplotlib

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/peeyushdutt01/Age-and-gender-prediction.git
    cd Age-and-gender-prediction
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download the Haar Cascade XML file for face detection**:

    The `haarcascade_frontalface_default.xml` file will be automatically loaded using OpenCV's data.

5. **Download the pre-trained Keras model**:

    Ensure you have your trained model file `AGpredv2.keras` in the appropriate directory or update the path in `model.py`.

## Usage

1. **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```

2. **Upload an Image**:

    - Click on "Choose an image..." and select a `.jpg`, `.jpeg`, or `.png` file from your device.
    - Press the "Predict" button to see the predicted gender and age.

3. **View Predictions**:

    - The app will display the uploaded image, cropped face, predicted gender, and estimated age.

## Project Structure

```plaintext
Age-and-gender-prediction/
│
├── app.py                  # Main Streamlit application file
├── model.py                # Contains functions to load model and make predictions
├── image_utils.py          # Contains helper functions for image processing
├── style.py                # Contains custom CSS styles for Streamlit
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
