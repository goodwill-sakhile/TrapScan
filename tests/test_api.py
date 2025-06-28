# tests/test_api.py

import pytest
from PIL import Image
import numpy as np
from api.predict import classify_image

def test_api_response_structure():
    """
    Validate the response format of the API.
    """
    test_img = Image.fromarray(np.random.randint(0, 255, (128, 128, 3), dtype=np.uint8))
    label, confidence = classify_image(test_img)

    assert isinstance(label, str), "Label should be a string"
    assert isinstance(confidence, float), "Confidence should be a float"
    assert 0.0 <= confidence <= 1.0, "Confidence should be within 0 and 1"
