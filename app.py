  
import numpy as np
import os
from keras.preprocessing import image 
import pandas as pd
import cv2
import tensorflow as tf
# Flask utils
from flask import Flask,request, render_template
from werkzeug.utils import secure_filename
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model



# Define a flask app
app = Flask(__name__)
# run_with_ngrok(app)
# Load your trained model
model = load_model('braintumor.h5')

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('brainintro.html')

@app.route('/predict1', methods=['GET'])
def predict1():
    # Main page
    return render_template('brainpred2.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        df= pd.read_csv('patient.csv')
        f = request.files['image']
        name=request.form['name']
        age=request.form['age']
        
        # Save the file to ./uploads
        basepath = os.path.dirname('/content')
        file_path = os.path.join(
            basepath, '/content/uploads', secure_filename(f.filename))
        f.save(file_path)
        img = image.load_img(file_path, target_size=(64, 64))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        
        
        prediction = model.predict_classes(x)[0][0]
        print(prediction)
        if prediction==0:
            text = "You are perfectly fine"
            inp = "No tumor"
        else:
            text = "You are infected! Please Consult Doctor"
            inp="Tumor detected"

        df=df.append(pd.DataFrame({'name':[name],'age':[age],'status':[inp]}),ignore_index=True)
        df.to_csv('patient.csv',index = False)
        return text

if __name__ == '__main__':
    app.run()