from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model from the pickle file
with open("diabetes_ml_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [float(x) for x in request.form.values()]
        input_features = np.array(features).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(input_features)

        # Display the result
        return render_template('index.html', prediction_text=f'The prediction is {prediction[0]}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
