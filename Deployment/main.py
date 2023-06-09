import tensorflow as tf
import numpy as np
import io

from PIL import Image
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image
from utils.prepare import download_models
from utils.predict import Predict

predictor = Predict()

model = tf.keras.models.load_model('product_categorizing_model.h5')

label = [
    "aksesoris_fashion",
    "buku_alat_tulis",
    "elektronik",
    "fashion_bayi_anak",
    "fashion_muslim",
    "fotografi",
    "handphone_aksesoris",
    "hobi_koleksi",
    "ibu_bayi",
    "jam_tangan",
    "kesehatan",
    "komputer_aksesoris",
    "makanan_minuman",
    "olahraga_outdoor",
    "otomotif",
    "pakaian_pria",
    "pakaian_wanita",
    "perawatan_kecantikan",
    "perlengkapan_rumah",
    "sepatu_pria",
    "sepatu_wanita",
    "souvenir_party_supplies",
    "tas_pria",
    "tas_wanita",
]


def transform_image(pillow_img):
    img = pillow_img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def predict(x):
    predictions = model.predict(x)
    predicted_class = np.argmax(predictions)
    return label[predicted_class]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files.get("image")

        if image is None or image.filename == "":
            return jsonify({"error":"no file"})
        
        try:
            image_bytes = image.read()

            pillow_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
            transformed_img = transform_image(pillow_image)

            predicted_category = predict(transformed_img)

            generated_text = predictor.predict(pillow_image, predicted_category)
            predicted_title, predicted_descripton = predictor.predict_improvement(generated_text)
            data = {"category": predicted_category, "title": predicted_title, "description": predicted_descripton}

            return jsonify(data)
    
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)})
        
    return "All Good"


@app.route("/prepare", methods=["GET"])
def prepare():
    download_models()
    return "OK"

    
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
