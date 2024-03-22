import pickle
import numpy as np
from tensorflow.keras.preprocessing import image

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match batch size
    img_array /= 255.0  # Normalize pixel values
    return img_array

def predict_image(model_path, image_path):
    # Load the model from pickle file
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    new_image = preprocess_image(image_path)
    prediction = model.predict(new_image)
    predicted_class = "pizza" if prediction[0][0] < 0.5 else "steak"
    return predicted_class
