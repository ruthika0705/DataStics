# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import requests
import pickle
import io
import sklearn
from sklearn.preprocessing import StandardScaler
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model


# Loading crop recommendation model

crop_recommendation_model_path = 'models/Agro-NBClassifier.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


# =========================================================================================

# Custom functions for calculations

# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/',methods=['GET'])
def home():
    title = 'D@taStics'
    return render_template('index.html', title=title)

@ app.route('/contact')
def contact():
    title = 'D@taStics'
    return render_template('contact.html', title=title)


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'D@taStics'
    return render_template('crop.html', title=title)


# ===============================================================================================


@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'D@taStics'
    if  request.method=="POST":
        Nitrogen = int(request.form['Nitrogen'])
        Phosphorous=int(request.form['Phosphorous'])
        Pottasium=int(request.form['Pottasium'])
        Temperature=float(request.form['Temperature'])
        Humidity=float(request.form['Humidity'])
        ph_level=float(request.form['ph_level'])
        Rainfall=float(request.form['Rainfall'])
    prediction=crop_recommendation_model.predict([[Nitrogen,Phosphorous,Pottasium,Temperature,Humidity,ph_level,Rainfall]])
    #output=rou
    #return render_template("index.html",prediction_text="You Should grow {}".format(prediction))
    return render_template('crop-result.html', prediction=prediction, title="D@taStics")


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)
