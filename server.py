from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def weather():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def page():
    temp_max = eval(request.form.get("temp_max"))
    temp_min = eval(request.form.get("temp_min"))
    wind = eval(request.form.get("wind"))

    url = "weatherd.csv"
    data = pd.read_csv(url)
    X = data[['temp_max', 'temp_min', 'wind']]
    y = data['weather']

    model = RandomForestClassifier()
    model.fit(X, y)

    arr = model.predict([[temp_max, temp_min, wind]])
    return render_template("index.html", result=arr[0])

if __name__ == '__main__':
    app.run()
