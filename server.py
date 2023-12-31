from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def breast_cancer():
    return render_template("Breast_cancer.html")

@app.route("/prediction", methods=["POST"])
def predict():
    radius_mean = float(request.form.get("radius_mean"))
    texture_mean = float(request.form.get("texture_mean"))
    smoothness_mean = float(request.form.get("smoothness_mean"))
    compactness_mean = float(request.form.get("compactness_mean"))
    symmetry_mean = float(request.form.get("symmetry_mean"))
    radius_se = float(request.form.get("radius_se"))
    smoothness_se = float(request.form.get("smoothness_se"))
    compactness_se = float(request.form.get("compactness_se"))
    radius_worst = float(request.form.get("radius_worst"))
    texture_worst = float(request.form.get("texture_worst"))

    url = "bdata.csv"  
    data = pd.read_csv(url)
    X = data[['radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean', 'radius_se', 'smoothness_se', 'compactness_se', 'radius_worst', 'texture_worst']]
    y = data['diagnosis']

    model = LogisticRegression()
    model.fit(X, y)

    arr = model.predict([[radius_mean, texture_mean, smoothness_mean, compactness_mean, symmetry_mean, radius_se, smoothness_se, compactness_se, radius_worst, texture_worst]])
    result = arr
    
    return render_template("Breast_cancer.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
