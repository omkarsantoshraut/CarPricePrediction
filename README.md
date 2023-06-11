# CarPricePrediction

The Car Price Prediction project is a **machine learning** based web application developed using flask framework that predicts the price of used cars. It utilizes historical car data, including features such as the car's maker, model, year of manufacture, kilometers driven, fuel type, and other relevant factors, to provide an estimate of the car's market value.

The project aims to assist both car buyers and sellers in making informed decisions by providing an accurate estimation of a car's price. By leveraging machine learning algorithms and data analysis techniques, the application offers a reliable and objective assessment of a car's value, taking into account various influential factors.

# Table of contents:

- [Installation](#install)
- [Usage](#use)
- [Features](#features)
- [Technologies](#tech)
- [Dataset](#dataset)
- [Live Demo](#demo)


<a id="install">
  
  # Installation:
  
  - Clone this project in the the directory.
  - Create a virtual environment in order to keep the project dependencies separate.
  - How ro create virtual environment?
      - Install virtualenv package in order to use it: `pip install virtualenv`
      - Create a new virtual env: `python<version> -m venv <virtual-environment-name>`
  - Install all requirements from requirements.txt file in order to run project: `pip install -r requirements.txt`
  - Open `CarPriceApplication.py` file and run it as a python file.
  - Flask will run on the url something like `http://127.0.0.1:5000/`.
  - Navigate to that url and you will get the project interface.
  
<a id="use">
  
  # Usage:
  
  As mentioned, this project will guide you to calculate the price of cars which you want to buy from buyer.
  If you will run the project you will see the interface like below:
  
  <img width="1053" alt="Screenshot 2023-06-11 at 4 21 44 PM" src="https://github.com/omkarsantoshraut/CarPricePrediction/assets/83705143/3699b460-ecf4-4f8f-bfd9-d577c680157f">
  
As you can see in the above image you will need to provide a few amount of data as input to machine learning model in order to get predicted car price.

<a id="features">
  
  # Features:
  
  - **Car Price Prediction:** The core feature of the application is to predict the price of a used car based on various factors.
  - **User-friendly Interface:** The application provides a user-friendly interface, making it easy for users to input car details and obtain price predictions.
  - **Historical Data Analysis:** The machine learning algorithms analyze historical car data to identify patterns and trends that influence car prices.
  - **Model Accuracy:** The predictive models used in the application are trained on a large dataset to ensure accurate and reliable price predictions.
  - **Customizable Inputs:** Users can adjust the input parameters, such as kilometer driven or fuel type, to see how these factors affect the predicted price.

<a id="tech">
  
  # Technologies:
  
  The Car Price Prediction project utilizes the following technologies: 
  - **Python:** The core programming language used for developing the machine learning models and the application's backend.
  - **Machine Learning Libraries:** Libraries such as scikit-learn, TensorFlow, or PyTorch are employed to train and deploy the predictive models.
  - **Web Development:** Frontend development technologies like HTML, CSS, and JavaScript are used to create a user-friendly web interface.   - **Flask:** A Python web framework used to build the backend of the application and handle user requests. MongoDB: A NoSQL database used to store and manage the car data for training and predictions.

<a id="dataset">
  
  # Dataset
  
  Follow: https://github.com/omkarsantoshraut/CarPricePrediction/edit/main/README.md#:~:text=Data-,car_cleaned_data,-.csv

<a id="demo">
  
  # Live Demo:
  
  Please follow https://carpriceprediction-d8hi.onrender.com/ in order to see the live demo of this project.
