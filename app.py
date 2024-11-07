import os
import gdown
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Create flask app
flask_app = Flask(__name__)

# Check if the model file is already downloaded
if not os.path.exists('model.pkl'):
    # Replace FILE_ID with your actual file ID from Google Drive
    url = 'https://drive.google.com/uc?export=download&id=1PyuomXpz5qYGUnexPF7p-smnlDuHjMkr'
    output = 'model.pkl'
    gdown.download(url, output, quiet=False)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle
# import pandas as pd

# # Create flask app
# flask_app = Flask(__name__)
# model = pickle.load(open("model.pkl", "rb"))

# Load the columns that were used to train the model (make sure you have saved them)
model_columns = pickle.load(open("model_columns.pkl", "rb")) 

@flask_app.route("/")
def Home():
    return render_template("index.html")

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

    # Define feature names as they were used during training
    # feature_names = ['State_Name', 'District_Name', 'Crop_Year', 'Season', 'Crop', 'Area', 'Production']
    
    # Create a DataFrame with the same feature names as the model was trained with
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
    return render_template("index.html", prediction=prediction[0])

   




    #     # Adjust this line to match your model's expected features
    #     features = np.array([[State_Name, District_Name, Crop_Year, Season, Crop, Area, Production]])  
    #     prediction = model.predict(features)

    #     # Render template with prediction
    #     return render_template("index.html", prediction=prediction)
    # except Exception as e:
    #     return f"An error occurred: {e}", 400
    
# @flask_app.route("/predict", methods = ["POST"])
# def predict():
#     if request.method == 'POST':
#         State_Name = request.form['State_Name']
#         District_Name = request.form['District_Name']
#         Crop_Year = request.form['Crop_Year']
#         Season = request.form['Season']
#         Crop = request.form['Crop']
#         Area  = request.form['Area']
#         Production  = request.form['Production']

#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template("index.html", prediction_text = "Predicted Yield  {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)