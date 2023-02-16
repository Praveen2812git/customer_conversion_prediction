from flask import Flask, render_template, request, jsonify
import pickle, numpy as np

app = Flask(__name__)

# Loading the model and scaler
model = pickle.load(open('CCP_XGBClassication.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Home Page
@app.route("/")
def home():
    return render_template('index.html')

# Post api with json
@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    data_f_sc = np.array(list(data.values())).reshape(1, -1)
    sc_data = scaler.transform(data_f_sc)
    op = model.predict(sc_data)
    op_prob = model.predict_proba(sc_data)[0][1]
    return jsonify(int(op[0]), float(round(op_prob*100, 2)))

# Responsive web app
@app.route('/predict', methods = ['POST'])
def predict():
    try:
        data = list(map(float, request.form.values()))
        sc_data = scaler.transform(np.array(data).reshape(1, -1))
        pred = model.predict(sc_data)[0]
        prob_pred = model.predict_proba(sc_data)[0][1]
        return render_template('index.html',
                               error_message = '',
                               prediction_result = f"The targeting customer is {'less' if pred == 0 else 'more'} likely to subscribe.",
                               prediction_chance = f'The customer is having {round(prob_pred * 100, 2)}% chance to subscribe to the insurance.')
    except ValueError:
        error_message = '\nEnter Interger values in the boxes. Strings not accepted.'
        return render_template('index.html', error_message=error_message, data_given='', prediction_result='', prediction_chance='')



if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0')