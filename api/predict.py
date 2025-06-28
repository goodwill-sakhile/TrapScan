# api/predict.py

import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from app.helpers import preprocess_image
from api.schema import PredictionResult

# Load once globally
MODEL_PATH = "model/trapscan_model.h5"
CLASS_NAMES_PATH = "model/class_names.txt"

model = None
class_names = []

def load_class_names():
    global class_names
    with open(CLASS_NAMES_PATH, "r") as f:
        class_names = [line.strip() for line in f.readlines()]

def load_trapscan_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = load_model(MODEL_PATH)
        print("Trapscan model loaded successfully.")
    else:
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

# Initialize on import
load_trapscan_model()
load_class_names()

def classify_image(image: Image.Image) -> PredictionResult:
    """
    Accepts a PIL image and returns a prediction.
    """
    processed = preprocess_image(image)
    prediction = model.predict(processed)[0]  # Get first batch result
    predicted_index = np.argmax(prediction)
    label = class_names[predicted_index]
    confidence = float(prediction[predicted_index])
    return label, confidence
