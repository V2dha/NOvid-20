import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
from flask.views import MethodView

app = Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')
def out():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        result = prediction[0]

        if result == 1:
            output = 'You have severe symptoms, you should consult a doctor.'

        else:
            output = 'You have no symptoms. Keep taking precautionary measures.'
        #return redirect(url_for('success', name=user))
        return render_template('index.html', prediction_text='{}'.format(output))

@app.route('/predict_api', methods=['POST','GET'] )
def predict_api():
    '''
    For direct API calls trought request
    '''
    if request.method == 'POST':
        data = request.get_json(force=True)
        prediction = model.predict([np.array(list(data.values()))])

        output = prediction[0]
        return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
