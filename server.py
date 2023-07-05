from flask import *
import numpy as  np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
app=Flask(__name__)

@app.route('/')
def weather():
  return render_template("index.html")

@app.route("weather",methods=['post'])
def page():
  temp_max=eval(request.form.get("temp_max"))
  temp_min=eval(request.form.get("temp_min"))
  wind=eval(request.form.get("wind"))
  
  url="C:\Users\91980\Downloads\reshavweatherdataset.csv"
  data=pd.read_csv(url, header=None)
  weather=data.values
  x=weather[:,0:3]
  y=weather[:,-1]
  
  model=DecisionTreeClassifier
  
  
  
  
  