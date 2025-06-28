# model/evaluate.py

from tensorflow.keras.models import load_model
from model.preprocess import get_data_generators
import matplotlib.pyplot as plt
import numpy as np
import os

def evaluate_model(model_path="model/trapscan_model.h5"):
    """
    Loads and evaluates the model on the validation set.
    """
    _, val_gen = get_data_generators()
    model = load_model(model_path)

    loss, acc = model.evaluate(val_gen)
    print(f"Validation Accuracy: {acc * 100:.2f}%")

    # Plot some predictions
    images, labels = next(val_gen)
    predictions = model.predict(images)
    pred_classes = np.argmax(predictions, axis=1)
    true_classes = np.argmax(labels, axis=1)

    for i in range(5):
        plt.imshow(images[i])
        plt.title(f"Pred: {val_gen.class_indices_inv[pred_classes[i]]}, True: {val_gen.class_indices_inv[true_classes[i]]}")
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    evaluate_model()
