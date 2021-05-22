import base64
import json

from flask import Flask, render_template, request
#from cnn import ConvolutionalNeuralNetwork
from io import BytesIO

from model import answers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    operation = BytesIO(base64.urlsafe_b64decode(request.form['operation']))
    #CNN = ConvolutionalNeuralNetwork()
    equation = answers(operation)
    return json.dumps({
        'operation': equation,
        'solution': eval(equation)
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0')