import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("ruta/donde_lo_tengas/fracture_model.keras")

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    pred = model.predict(img_array)[0][0]

    if pred > 0.9:
        return "Fractura", float(pred)
    else:
        return "No fractura", float(pred)