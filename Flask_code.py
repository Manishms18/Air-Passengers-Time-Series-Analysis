import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
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
     
    prediction = model.forecast(steps=final_features)

    output = np.exp(prediction[0])

    return render_template('interface.html', prediction_text='Forecast for Air passengers are {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

