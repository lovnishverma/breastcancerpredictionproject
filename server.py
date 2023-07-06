from flask import *
import numpy as  np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
app=Flask(__name__)

@app.route('/')
def weather():
  return render_template("index.html")

@app.route("/weather",methods=["POST"])
def page():
  temp_max=eval(request.form.get("temp_max"))
  temp_min=eval(request.form.get("temp_min"))
  wind=eval(request.form.get("wind"))
  
  url="weatherd.csv"
  data=pd.read_csv(url, header=None)
  weather=data.values
  x=weather[:,1:4]
  y=weather[:,-1]
  
  model=DecisionTreeClassifier()
  model.fit(x,y)
  
  arr=model.predict([[temp_max,temp_min,wind]])
  result=str(arr[0])
  return render_template("index.html",result2)
if __name__ == '__main__':
  app.run()
    
  
  
  