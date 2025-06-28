# model/preprocess.py

import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_data_generators(data_dir="data", img_size=(128, 128), batch_size=32):
    """
    Prepares ImageDataGenerators for training and validation.
    """
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,
        horizontal_flip=True,
        zoom_range=0.1
    )

    train_gen = datagen.flow_from_directory(
        os.path.join(data_dir, "images"),
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    val_gen = datagen.flow_from_directory(
        os.path.join(data_dir, "images"),
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    return train_gen, val_gen
