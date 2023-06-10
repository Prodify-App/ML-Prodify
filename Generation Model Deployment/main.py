
import io
import tensorflow as tf

from PIL import Image
from flask import Flask, request, jsonify
from utils.prepare import download_models
from utils.predict import Predict

predictor = Predict()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files.get("image")
        category = request.form.get("category")

        if image is None or image.filename == "" or category is None or category == "":
            return jsonify({"error":"parameters not complete"})

        try:
            image_bytes = image.read()
            pillow_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

            generated_text = predictor.predict(pillow_image, category)
            predicted_title, predicted_descripton = predictor.predict_improvement(generated_text)
            data = {"title": predicted_title, "description": predicted_descripton}

            return jsonify(data)
    
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)})

    return "All Good"


@app.route("/prepare", methods=["GET"])
def prepare():
    download_models()
    return "OK"


@app.route("/check-gpu", methods=["GET"])
def check():
    print(tf.config.list_physical_devices('GPU'))
    return tf.config.list_physical_devices('GPU')
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
