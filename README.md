# IPL

## 🏏 IPL First Innings Score Predictor

This project is a **web-based machine learning application** built using **Flask** that predicts the **first innings score** of an IPL match based on live match conditions such as teams, runs, wickets, overs completed, and performance in the last 5 overs.

---

## 🚀 Live Demo

To try the app locally:
```bash
git clone https://github.com/yourusername/ipl-first-innings-score-predictor.git
cd ipl-first-innings-score-predictor
python app.py
````

Open your browser and go to `http://localhost:8080`.

---

## 🔍 Project Overview

The application uses **Ridge Regression** (with option to switch to XGBoost) trained on historical IPL match data to forecast the first innings score.

### Input Parameters:

* Batting Team
* Bowling Team
* Current Runs
* Wickets Fallen
* Overs Completed (>= 5.0)
* Runs in Last 5 Overs
* Wickets in Last 5 Overs

### Output:

* Predicted score range (e.g., *"First Innings Predicted Score Range: 145 to 160"*).

---

## 📊 Model Development

The model was built using cleaned and preprocessed IPL ball-by-ball data. Key steps include:

* Dropping irrelevant features (`mid`, `venue`, etc.).
* Filtering consistent teams.
* One-hot encoding of categorical variables (teams).
* Removing early overs data (<5.0 overs).
* Hyperparameter tuning using **GridSearchCV** for Ridge and Lasso.
* **RandomizedSearchCV** used for Random Forest tuning.
* Residual plots used for error visualization.

### Models Trained:

* Linear Regression
* Ridge Regression ✅ *(Final Model)*
* Lasso Regression
* XGBoost Regressor
* Random Forest Regressor *(Commented for future use)*

---

## 📁 File Structure

```
.
├── app.py                         # Flask web application
├── templates/
│   └── index.html                 # Web interface template
├── static/                        # Static assets (optional)
├── first-innings-score-ridge_regressor-model.pkl  # Trained Ridge Regression model
├── ipl.csv                       # Cleaned IPL dataset
└── README.md
```

---

## 🧠 Libraries Used

* **Flask** – For serving the web app
* **scikit-learn** – For training regression models
* **XGBoost** – For advanced regression
* **Pandas, NumPy** – For data preprocessing
* **Matplotlib, Seaborn** – For EDA and residual analysis
* **Pickle** – For saving models

---

## 📈 Performance Metrics

Evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R-squared (R² Score)

Ridge Regression provided a good balance between bias and variance on test data.

---

## 📦 Installation & Requirements

```bash
pip install flask pandas numpy scikit-learn matplotlib seaborn xgboost
```

---

## 📌 Future Enhancements

* Add support for live match data via API
* Extend model to predict match outcome
* Integrate player-specific performance features
* Deploy on Heroku or AWS

---

## 🙌 Acknowledgements

* IPL dataset used from Kaggle
* Inspired by real-time sports analytics projects
