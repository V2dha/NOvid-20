from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__,template_folder='templates')
MODEL_PATH = 'model.h5'
model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(244, 244))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    preds = np.argmax(preds,axis=1)
    return preds


@app.route('/')
def home():
    # Main page
    print("1")
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the file from post request
        print("2")
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)   # ImageNet Decode
        class_names =  ["COVID-19","NORMAL","Viral Pneumonia"]
        output = class_names[preds[0]]
        # print(result)
        # if result == 0:
        #     output = 'Corona.'

        # elif result==1:
        #     output = 'Normal.'
        # elif result==2:
        #     output = 'Pneumonia.'
        print(output)
        return render_template('index.html', prediction='{}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
