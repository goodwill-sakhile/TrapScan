# tests/test_dataset.py

import pytest
from data.data_loader import get_image_paths

def test_image_structure():
    """
    Verify that dataset is organized by class labels with images.
    """
    image_map = get_image_paths()
    
    assert isinstance(image_map, dict)
    assert len(image_map) > 0, "No class folders found"

    for label, paths in image_map.items():
        assert isinstance(paths, list)
        assert all(path.endswith(".jpg") or path.endswith(".png") for path in paths)
