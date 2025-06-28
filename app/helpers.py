# app/helpers.py

import numpy as np
from PIL import Image

def preprocess_image(image: Image.Image, target_size=(128, 128)):
    """
    Preprocess the image to match model input requirements.
    """
    image = image.resize(target_size)
    image_array = np.array(image)
    
    if image_array.shape[-1] == 4:
        image_array = image_array[:, :, :3]  # Remove alpha if present
    
    image_array = image_array.astype("float32") / 255.0
    return np.expand_dims(image_array, axis=0)
