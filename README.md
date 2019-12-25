# Air-Passengers-Time-Series-Analysis
Forecasting number of passengers for airlines using ARIMA model in python

You can view the project demo on [YouTube](https://www.youtube.com/watch?v=qamLBQQZP14).
   
## Table of contents

* [General info](#general-info)
* [Screenshots](#screenshots)
* [Demo](#demo)
* [Technologies and Tools](#technologies-and-tools)
* [Code Examples](#code-examples)
* [Status](#status)
* [Contact](#contact)

## General info

Project was binary classification (Supervised Learning) problem.
Major steps involved were as follow :                                 
* STEP: 1 - Data Cleaning 
* STEP: 2 - Feature Engineering and Feature Creation 
* STEP: 3 - Transformation and Outlier Removal 
* STEP: 4 - Exploratory Data Analysis and Sampling
* STEP: 5 - Model Building and Evaluation 
* STEP: 6 - Best Model and Deployment
* STEP: 7 - Interpretations and Insights 
* STEP: 8 - Improvements and Future Work 

## Demo

![Example screenshot](./images/Demo.gif)

**The entire demo of the project can be found on [YouTube](https://www.youtube.com/watch?v=qamLBQQZP14).**

## Screenshots

![Example screenshot](./images/Interface.png)
![Example screenshot](./images/Outline.png)
![Example screenshot](./images/Insights.png)
![Example screenshot](./images/Heatmap.png)

## Technologies and Tools
* Python 
* Flask
* Scikit-learn
* HTML

## Code Examples

````
# Code for creating pickle file of model and transform  

import pickle

pickle.dump(scaler, open('tranform.pkl','wb'))
pickle.dump(rf_clf, open('model.pkl','wb'))

X_test=scaler.transform(X_test_unscaled[:1])

predictions=rf_clf.predict(X_test)
print("Predicted Result : ",predictions)

predictions = rf_clf.predict_proba(X_test)
print("Predicted Result probability : ",predictions)

````
````
# Flask code for using deployed pickle file and connecting to interface

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
scaler = pickle.load(open('tranform.pkl','rb'))
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('interface.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    
    final_features = [np.array(int_features)]
    
    final_features = np.pad(final_features, (0, 63), 'constant')
    
    final_features = scaler.transform(final_features)
    
    prediction = model.predict_proba(final_features)

    output = prediction[0]

    return render_template('interface.html', prediction_text='Readmission probability is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

````


## Status
Project is: _finished_.

## Contact
If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on 
<a href="mailto:manishshukla.ms18@gmail.com">email</a> or 
<a href="https://www.linkedin.com/in/manishshukla-ms/" target="_blank">LinkedIn</a>
