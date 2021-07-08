# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:45:03 2021

@author: noopa
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template
import os

app=Flask(__name__)
pickle_in = open("Fish_Species.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)

    
    return render_template('index.html', prediction_text='The fish belong to species {}'.format(prediction))
    
    
#port = int(os.getenv('PORT'))

if __name__=='__main__':
    app.run()
