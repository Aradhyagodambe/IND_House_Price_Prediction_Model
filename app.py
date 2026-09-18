from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the LinearRegression model provided in the source
with open('Houes_Price_Prediction.pkl', 'rb') as file:
    model = pickle.load(file)

# Feature order must match the order used when the model was trained
FEATURES = [
    'bedrooms', 'bathrooms', 'living_area', 'lot_area', 'floors',
    'waterfront', 'views', 'condition', 'grade',
    'area_excluding_basement', 'area_basement', 'built_year',
    'renovation_year', 'postal_code', 'lot_area_renov',
    'schools_nearby', 'distance_airport',
]


@app.route('/')
def home():
    return render_template('index.html', form_data={})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[name]) for name in FEATURES]

        # Reshape for a single prediction and predict
        prediction = model.predict([np.array(features)])
        output = round(float(prediction[0]), 2)

        # form_data keeps the user's inputs in the form after prediction
        return render_template('index.html', prediction=output, form_data=request.form)

    except KeyError as e:
        return render_template('index.html', form_data=request.form,
                               error=f'Missing field: {e.args[0]}. Please complete every field.')
    except ValueError:
        return render_template('index.html', form_data=request.form,
                               error='One or more values are not valid numbers. Please check your entries.')
    except Exception as e:
        return render_template('index.html', form_data=request.form, error=f'Prediction failed: {e}')


if __name__ == "__main__":
    # Flask development server
    app.run(debug=True, host='0.0.0.0')
