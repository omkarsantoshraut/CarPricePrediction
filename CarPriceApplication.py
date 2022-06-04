from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
car_data = pd.read_csv('Data/car_cleaned_data.csv')
model = pickle.load(open('ML_Model/CarPricePredictionModel.pkl', 'rb'))

@app.route('/')
def homeScreen():
    companies = sorted(car_data['name'].unique())
    years = sorted(car_data['year'].unique())[1:]
    fuel = sorted(car_data['fuel'].unique())
    transmission = sorted(car_data['transmission'].unique())
    owner = car_data['owner'].unique()
    sellerType = car_data['seller_type'].unique()
    params = {
        'CompanyName': companies,
        'years': years,
        'fuel': fuel,
        'transmission': transmission,
        'owner': owner,
        'sellerType': sellerType
    }
    return render_template('index.html', params=params)

@app.route('/predict', methods = ['POST'])
def predict():
    company = request.form.get('company')
    year = request.form.get('year')
    fuel = request.form.get('fuel')
    transmission = request.form.get('transmission')
    owner = request.form.get('owner')
    sellerType = request.form.get('sellerType')
    km_driven = request.form.get('km_driven')
    presentPrice = request.form.get('presentPrice')
    prediction = model.predict(pd.DataFrame([[company, year, km_driven, fuel, sellerType, transmission, owner, presentPrice]], columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission','owner', 'present_prize']))
    return str(np.round(prediction[0], 2))

if __name__ == "__main__":
    app.run(debug=True)