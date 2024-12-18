import pickle
from flask import Flask,app,request,render_template,redirect,flash,session,jsonify,url_for
import numpy as np
import pandas as pd

app=Flask(__name__)
#load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text="The predicted price is : ${}".format(output))
    
@app.route('/aboutus')
def about():
    return render_template("aboutus.html")

@app.route('/contact')
def con():
    return render_template("contactus.html")
if __name__=="__main__":
    app.run(debug=True)