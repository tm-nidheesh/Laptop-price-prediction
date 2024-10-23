# Laptop-price-prediction

## Business Objective
The goal of this project is to develop a machine learning model that can accurately predict the price of a laptop based on its features, such as processor, RAM, storage capacity, graphics card, screen size,touchscreen, weight and brand.<br>

## Dataset description
Input Features
* Company - Manufacturer of the laptop
* TypeName - Category of laptop
* Inches - Screen size diagonal measurement
* ScreenResolution - Display resolution specifications
* CPU - Processor specifications
* RAM - Memory capacity
* Memory - Storage specifications
* GPU - Graphics card specifications
* OpSys - Operating System
* Weight - Laptop weight<br>

Target Variable

* Price - Laptop price in specified currency<br>

# Approach 
Applying machine learing tasks like Data Exploration, Data Cleaning, Feature Engineering, Model Building and model testing to build a solution that should able to predict the price of the laptop.<br>

* Data Exploration : Exploring the dataset using pandas, numpy, matplotlib and seaborn.
* Exploratory Data Analysis : Plotted different graphs to get more insights about dependent and independent variables/features.
* Feature Engineering : Numerical features scaled down and Categorical features encoded.
* Model Building : In this step, first dataset Splitting is done. After that model is trained on different Machine Learning Algorithms such as:
  * Linear Regression
  * SVR
  * KNN Regressor
  * Random forest Regressor
  * Ensemble methods 
* Model Selection : Tested all the models to check the RMSE & R-squared and selected a model with the highest performance metrics.
* Pickle File : The model is saved using pickle library.
* Web Application & Deployment : Created a web application using Streamlit that takes all the necessary inputs from the user & shows the output. <br>

# Requirements
* Pandas
* Numpy
* Sklearn
* Streamlit
* Pickle

# Outcome
The outcome was a highly robust predictive model that successfully identifies laptop prices with exceptional accuracy (R² = 0.89). The vottting ensemble model effectively captured complex relationships between hardware specifications and pricing patterns, enabling precise price estimations across diverse market segments. The system's ability to weigh multiple features, particularly hardware specifications (RAM, CPU, GPU) and brand value, makes it a valuable tool for both retailers and consumers in making informed pricing decisions.<br>



![lap1](https://user-images.githubusercontent.com/124424862/225579770-6859d85d-d03b-4291-b3a7-afa549e1bc3f.jpg)

![lap2](https://user-images.githubusercontent.com/124424862/225579853-b0bed7f7-3783-408b-b98d-961e36f68b45.jpg)

![lap3](https://user-images.githubusercontent.com/124424862/225579927-03ffc356-c498-4f44-8c90-225d4194acb9.jpg)

<br>

# Business Applications
Use Cases
* Pricing strategy development.
* Inventory valuation.
* Competitive analysis.
* Market positioning. <br>

Implementation Scenarios
* E-commerce platforms
* Retail pricing
* Trade-in value estimation
* Market analysis
