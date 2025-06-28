# data/prepare_dataset.py

import os
import shutil
from PIL import Image
from tqdm import tqdm

def validate_and_clean_images(data_dir="data/images", min_size=(64, 64)):
    """
    Walk through all images and delete corrupted or too-small ones.
    """
    total_checked = 0
    total_deleted = 0

    for root, _, files in os.walk(data_dir):
        for fname in tqdm(files, desc=f"Checking in {root}"):
            if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            fpath = os.path.join(root, fname)
            try:
                with Image.open(fpath) as img:
                    if img.size[0] < min_size[0] or img.size[1] < min_size[1]:
                        os.remove(fpath)
                        total_deleted += 1
            except Exception:
                os.remove(fpath)
                total_deleted += 1
            total_checked += 1

    print(f"Checked {total_checked} files, removed {total_deleted} invalid images.")

def structure_dataset(input_dir="raw_data", output_dir="data/images"):
    """
    Takes images from raw_data/[label]/image.jpg and copies to data/images/[label]/image.jpg.
    """
    if not os.path.exists(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        return

    os.makedirs(output_dir, exist_ok=True)

    for label in os.listdir(input_dir):
        label_path = os.path.join(input_dir, label)
        if not os.path.isdir(label_path):
            continue

        target_label_dir = os.path.join(output_dir, label)
        os.makedirs(target_label_dir, exist_ok=True)

        for img in os.listdir(label_path):
            src = os.path.join(label_path, img)
            dst = os.path.join(target_label_dir, img)
            try:
                shutil.copy2(src, dst)
            except Exception as e:
                print(f"Error copying {img}: {e}")

    print("Dataset structured successfully.")

if __name__ == "__main__":
    structure_dataset()
    validate_and_clean_images()
