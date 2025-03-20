from flask import Flask, request  
app = Flask(__name__)  

@app.route('/predict', methods=['POST'])  
def predict():  
    text = request.json['text']  
    # Add your model prediction logic here  
    return {'sentiment': 'positive'}  