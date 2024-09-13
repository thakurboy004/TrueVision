import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

def load_ai_model(model_path="model/image_classifier_model.h5"):
    try:
        model = load_model(model_path)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def predict_image(model, image):
    image = image.resize((224, 224)) 
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    return "Real" if prediction[0] > 0.5 else "Fake"
