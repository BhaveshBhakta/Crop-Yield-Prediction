# Indian Crop Yield Prediction Using Machine Learning

This repository contains a machine learning-based solution to predict crop yield in India, considering multiple input parameters. The project leverages a Random Forest Regressor model and includes an interactive and visually appealing website to enhance user experience.

---

## Project Overview

Indian agriculture depends heavily on precise crop yield predictions. This project helps farmers, policymakers, and agricultural stakeholders make informed decisions by predicting crop yield based on key input parameters. 

### Features:
- **Extensive Data**: Covers all states and over 600 districts of India.
- **User Inputs**: Crop Type, Season, Area, Crop Year, and more.
- **Machine Learning**: Random Forest Regressor for accurate yield predictions.
- **Dynamic Website**: A user-friendly interface featuring animations using GSAP and smooth scrolling powered by Lenis.

---

## Tech Stack

### Backend:
- **Machine Learning**: Random Forest Regressor
- **Python Libraries**: Pandas, NumPy, Scikit-learn

### Frontend:
- **UI Enhancements**: GSAP for animations and Lenis for smooth scrolling
- **Web Framework**: Flask
- **HTML/CSS/JavaScript**: For responsive and dynamic user interface

---

## How It Works

1. **Input Parameters**: Users input crop type, season, area, crop year, and other relevant details.
2. **Prediction Model**: The Random Forest Regressor processes the input and predicts the crop yield.
3. **Output**: The predicted yield is displayed on the website in a clean and interactive format.

---

## Highlights

- **Comprehensive Data**: A wide dataset ensures accurate predictions for different regions and conditions.
- **Intuitive Design**: The website combines functionality with aesthetics for a seamless user experience.
- **Dynamic Animations**: GSAP and Lenis make the interface engaging and modern.

---

## Setup Instructions

1. Clone this repository:  
   ```bash
   git clone https://github.com/BhaveshBhakta/Crop-Yield-Prediction.git
   cd Crop-Yield-Prediction
   ```

2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:  
   ```bash
   python app.py
   ```

4. Open the app in your browser at `http://127.0.0.1:5000/`.

---

## Project Structure

```
📦 indian-crop-yield-prediction
├── app.py                # Flask application
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── models/               # Machine learning model files
├── data/                 # Dataset used for training and testing
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Dataset

The dataset includes:
- **State-level Data**: Comprehensive data for all Indian states.
- **District-level Data**: Covers over 600 districts for granular analysis.

---

