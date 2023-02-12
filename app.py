from flask import *
from flask import render_template
from flask import request
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score
import pickle as pkl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/success",methods=["POST"])
def success():

    success.gender = int(request.form['group1'])
    success.currSmoke = int(request.form['group2'])
    success.bpMeds = int(request.form['group3'])
    success.stroked = int(request.form['group4'])
    success.hypTension = int(request.form['group5'])
    success.diabeters = int(request.form['group6'])

    success.age = int(request.form['age'])
    success.cpd = int(request.form['cpd'])
    success.sys = int(request.form['sys'])
    success.dia = int(request.form['dia'])
    success.bmi = int(request.form['bmi'])
    success.heartRate = int(request.form['heartRate'])

    
    inputs = [[success.gender, success.age, success.currSmoke, success.cpd, success.bpMeds, success.stroked, success.hypTension, success.diabeters, success.sys, success.dia, success.bmi, success.heartRate]]
    
    with open('/Users/nisargpatel/Documents/hacklytics/model_pkl', 'rb') as f:
        obj = pkl.load(f)
    
    num = obj.predict(inputs)
    print(inputs)
    if num == 0:
        return render_template("success.html")
    else:
        return render_template("fail.html")
    
    



if (__name__ == '__main__'):
    app.run()
