**Breast Cancer Prediction using Logistic Regression** Flask app:

# 🧬 Breast Cancer Prediction App

A Flask-based web application that predicts the presence of breast cancer using Logistic Regression, based on patient tumor characteristics.

## 🔍 Overview

- **Input**: 10 tumor measurement features
- **Model**: Logistic Regression (`scikit-learn`)
- **Dataset**: `bdata.csv`
- **Output**: Predicted diagnosis (`M` = Malignant, `B` = Benign)

## 🧪 Features Used for Prediction

- `radius_mean`
- `texture_mean`
- `smoothness_mean`
- `compactness_mean`
- `symmetry_mean`
- `radius_se`
- `smoothness_se`
- `compactness_se`
- `radius_worst`
- `texture_worst`

## 🛠️ How to Run

1. **Clone the repo & navigate to the project directory:**

```bash
git clone https://github.com/yourusername/breast-cancer-predictor.git
cd breast-cancer-predictor
````

2. **Install dependencies:**

```bash
pip install flask pandas scikit-learn
```

3. **Run the Flask app:**

```bash
python app.py
```

4. **Visit in browser:**

```
http://127.0.0.1:5000
```

## 🖥️ Project Structure

```
.
├── app.py                   # Main Flask application
├── bdata.csv                # Dataset used for training
├── templates/
│   └── Breast_cancer.html   # HTML form & result display
└── README.md                # Project documentation
```

## 📈 Note

* The model is trained every time the form is submitted. For production use, consider training once and saving the model using `joblib` or `pickle`.

## 🧪 Sample Output

* **Input** → `radius_mean = 14.2, texture_mean = 20.1, ...`
* **Output** → `Prediction: Malignant`

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---
