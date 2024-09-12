import tensorflow as tf
from tensorflow.keras.models import load_model

def load_ai_model(model_path="model/model_weights.h5"):
    model = load_model(model_path)
    return model

def predict_image(model, image):
    image = image.resize((224, 224))  # Resize image to the input size expected by the model
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image / 255.0  # Normalize image
    image = tf.expand_dims(image, axis=0)  # Add batch dimension
    prediction = model.predict(image)
    return "Real" if prediction[0] > 0.5 else "Fake"
