# tests/test_model.py

import pytest
from PIL import Image
import numpy as np
from api.predict import classify_image

def test_model_prediction_on_dummy_image():
    """
    Test CNN classification on a dummy white image.
    """
    dummy_image = Image.fromarray(np.ones((128, 128, 3), dtype=np.uint8) * 255)
    label, confidence = classify_image(dummy_image)

    assert isinstance(label, str)
    assert 0.0 <= confidence <= 1.0
