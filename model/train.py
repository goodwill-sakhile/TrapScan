# model/train.py

from model.cnn_model import build_trapscan_cnn
from model.preprocess import get_data_generators
import os

def train_model():
    """
    Trains and saves the Trapscan CNN model.
    """
    train_gen, val_gen = get_data_generators()
    model = build_trapscan_cnn(input_shape=(128, 128, 3), num_classes=train_gen.num_classes)

    print("Starting training...")
    model.fit(train_gen, validation_data=val_gen, epochs=10)

    # Save model
    os.makedirs("model", exist_ok=True)
    model.save("model/trapscan_model.h5")

    # Save class labels
    with open("model/class_names.txt", "w") as f:
        for class_name in train_gen.class_indices:
            f.write(f"{class_name}\n")

    print("Training complete. Model and class names saved.")

if __name__ == "__main__":
    train_model()
