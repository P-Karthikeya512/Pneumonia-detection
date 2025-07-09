from flask import Flask, request, render_template_string
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Load your trained model
model = load_model("model.h5")

app = Flask(__name__)

# HTML Template with inline prediction display
HTML_PAGE = '''
    <h2>Pneumonia Detection</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*" required><br><br>
        <input type="submit" value="Upload and Predict">
    </form>
    {% if prediction %}
        <h3>Result: {{ prediction }}</h3>
        <p>Confidence: {{ confidence }}</p>
    {% endif %}
'''

# Preprocessing function
def preprocess(image):
    image = image.resize((150, 150))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    confidence = None

    if request.method == "POST":
        if 'file' not in request.files:
            prediction = "No file uploaded"
        else:
            file = request.files["file"]
            image = Image.open(file.stream).convert("L")  # grayscale
            img_array = preprocess(image)
            pred = model.predict(img_array)[0][0]
            prediction = "Pneumonia" if pred > 0.5 else "Normal"
            confidence = f"{pred:.4f}"

    return render_template_string(HTML_PAGE, prediction=prediction, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
