import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, static_folder="static")
model = pickle.load(open('ml.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    result = prediction[0]

    if (result == 1):
        output = 'You have severe symptoms, you should consult a doctor.'

    # elif(result == 2):
    #      output = 'You have moderate symptoms you may consult the doctor and take required precautions' 

    # elif(result == 1):
    #      output = 'You have mild symptoms you should take required precautions'   
    
    else:
        output = 'You have no symptoms. Keep taking precautionary measures.'

    return render_template('home.html', prediction_text='{}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)