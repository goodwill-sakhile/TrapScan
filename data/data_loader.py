# data/data_loader.py

import os
from glob import glob

def get_image_paths(base_dir="data/images"):
    """
    Returns a dictionary with class names as keys and list of image paths as values.
    """
    class_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    image_map = {}

    for cls in class_dirs:
        path_pattern = os.path.join(base_dir, cls, "*.jpg")
        image_map[cls] = glob(path_pattern)

    return image_map

def count_images(base_dir="data/images"):
    """
    Count all images across all classes.
    """
    image_map = get_image_paths(base_dir)
    total = sum(len(paths) for paths in image_map.values())
    print(f"Total images found : {total}")
    return total
