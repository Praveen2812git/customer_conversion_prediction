![GitHub](https://img.shields.io/github/license/Praveen2812git/customer_conversion_prediction)
# customer_conversion_prediction
A Data Science [application](https://praveenpython.pythonanywhere.com/) to predict if a client will subscribe to the insurance beforehand so that they can be specifically targeted via call.<br>

<!-- Image 1 -->
![alt text](https://github.com/Praveen2812git/customer_conversion_prediction/blob/main/cus_conv_pred1.jpg?raw=true)<br>

## Technologies and Frameworks Used
### .py file:
- Python 3.10 (Technology)
- Html (Technology)
- Css (Technology)
- Scikit Learn
- Flask
- Pickle
### .ipynb file:
- Pandas
- Numpy
- Matplotlib
- Seaborn
- XgBoost

## Installation
Install all Flask requirements by run the following command
```
pip install -r requirements.txt
```

## Run Flask
To access and use the application,donwoload or clone the repository and then run the command below.
```
app.py
```
Finally browse the link provided in your browser.

## Run application in cloud
The application has been deployed in the pythonanywhere.com
You can clone your repository to pythonanywhere or copy paste the files in pythonanywhere to run the app in cloud.

## How the model is developed
- The dataset - train is a history of customers who accepted or rejected the insurance when called via phone.
- The data is highly imbalanced because of a reason that only a few will accept insurance.
- With the details of the customer provided, six features that affect acceptance percentage the most were selected.
- Classification models (Logistic Regression, K-Nearest Neighbors, Decision Tree, Random Forest, XgBoost) are used for training.
- XgBoost comes out to be the best model.
- I am using free cloud service which provides limited ROM. So, I used the Decision Tree pickle file to predict the customers who accept the insurance beforehand.
- **Note:** If you are also using a Decision Tree pickle file like me and using a free cloud service remove xgboost==1.6.2 from the requirements.txt file.

## Deployed model will look like below

<!-- Image 2 -->
![alt text](https://github.com/Praveen2812git/customer_conversion_prediction/blob/main/cus_conv_pred2.png?raw=true)
