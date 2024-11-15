import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Create flask app
flask_app = Flask(__name__)

# Load the split model parts and combine them
with open("model_part1.pkl", "rb") as file1:
    part1 = file1.read()

with open("model_part2.pkl", "rb") as file2:
    part2 = file2.read()

# Combine and load the full model
model_bytes = part1 + part2
model = pickle.loads(model_bytes)

# Load the columns used to train the model
model_columns = pickle.load(open("model_columns.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

# Route to the prediction page
@flask_app.route("/predict_page")
def predict_page():
    return render_template("predict.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Retrieve form inputs
        State_Name = request.form['State_Name']
        District_Name = request.form['District_Name']
        Crop_Year = int(request.form['Crop_Year'])
        Season = request.form['Season']
        Crop = request.form['Crop']
        Area = float(request.form['Area'])
        Production = float(request.form['Production'])
        
    except ValueError as e:
        return f"Invalid input: {e}", 400

    # Create a DataFrame with the input features
    input_data = pd.DataFrame([{
        'State_Name': State_Name,
        'District_Name': District_Name,
        'Crop_Year': Crop_Year,
        'Season': Season,
        'Crop': Crop,
        'Area': Area,
        'Production': Production
    }])

    # Apply one-hot encoding to the input data
    dummy_df = pd.get_dummies(input_data)

    # Ensure the input data has the same columns as the model's training data
    dummy_df = dummy_df.reindex(columns=model_columns, fill_value=0)

    # Make the prediction
    prediction = model.predict(dummy_df)

    # Return the result to the template (e.g., index.html)
    return render_template("predict.html", prediction=prediction[0])

# if __name__ == "__main__":
#     flask_app.run(debug=True)
