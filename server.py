from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def Breast Cancer():
    return render_template("Breast cancer.html")

@app.route("/breast cancer", methods=["POST"])
def page():
    radius_mean = eval(request.form.get("radius_mean"))
    texture_mean = eval(request.form.get("texture_mean"))
    smoothness_mean = eval(request.form.get("smoothness_mean"))
    compactness_mean = eval(request.form.get("compactness_mean"))
    symmetry_mean = eval(request.form.get("symmetry_mean"))
    radius_se = eval(request.form.get("radius_se"))
    smoothness_se = eval(request.form.get("smoothness_se"))
    compactness_se = eval(request.form.get("compactness_se"))
    radius_worst = eval(request.form.get("radius_worst"))
    texture_worst = eval(request.form.get("texture_worst"))

    url = "New_.csv(1)"
    data = pd.read_csv(url)
    X = data[['radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean', 'radius_se', 'smoothness_se', 'compactness_se', 'radius_worst', 'texture_worst']]
    y = data['diagnosis']

    model = LogisticRegression()
    model.fit(X, y)

    arr = model.predict([[temp_max, temp_min, wind]])
    return render_template("Breast cancer.html", result=arr[0])

if __name__ == '__main__':
    app.run()
