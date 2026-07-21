from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the LinearRegression model provided in the source
with open('Houes_Price_Prediction.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting the 17 features required by the model
        features = [
            float(request.form['bedrooms']),
            float(request.form['bathrooms']),
            float(request.form['living_area']),
            float(request.form['lot_area']),
            float(request.form['floors']),
            float(request.form['waterfront']),
            float(request.form['views']),
            float(request.form['condition']),
            float(request.form['grade']),
            float(request.form['area_excluding_basement']),
            float(request.form['area_basement']),
            float(request.form['built_year']),
            float(request.form['renovation_year']),
            float(request.form['postal_code']),
            float(request.form['lot_area_renov']),
            float(request.form['schools_nearby']),
            float(request.form['distance_airport'])
        ]
        
        # Reshape for a single prediction and predict
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'$ {output}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    # Flask development server
    app.run(debug=True, host='0.0.0.0')
