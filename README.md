# 🩺 Pneumonia Detection using CNN

This is a beginner-level deep learning project where I built a simple Convolutional Neural Network (CNN) to detect pneumonia from chest X-ray images. The project includes a basic Flask web app to upload and predict images using the trained model.

---

## 🧠 What It Does

- Trains a CNN on chest X-ray images to classify them as:
  - **Normal**
  - **Pneumonia**
- Provides a minimal web interface to:
  - Upload a chest X-ray
  - Predict and display the result

---

## 📂 Dataset

The dataset used is [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) from Kaggle.

```
Structure:
DataSet/
└── chest_xray/
    ├── train/
    ├── val/
    └── test/
```
## 🛠️ Tech Stack

- **Python**
- **TensorFlow / Keras**
- **Flask**
- **HTML / CSS** (basic)

---
### Train or Use the Model

You can run the `Pneumonia.ipynb` notebook to train the model.  
After training, it will save the model as `model.h5` in the project directory.

---

### Run the Flask App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

Upload a chest X-ray image to test the prediction.
### 📌 Notes

- The web app is very basic — just a functional interface to test predictions.
- This project is part of my learning journey in **Deep Learning** and **Flask**.
- Suggestions and feedback are welcome!

