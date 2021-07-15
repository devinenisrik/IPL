# Importing essential libraries
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd

# Load the Random Forest CLassifier model
#filename = 'first-innings-score-xgb-model.pkl'
#regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

regressor = pickle.load(open('first-innings-score-ridge_regressor-model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    #temp_array = list()
    
    if request.method == 'POST':
        temp_array = list()
        batting_team = request.form['Batting_Team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        else:
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['Bowling_Team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        else:
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        overs = float(request.form['Overs'])
        runs = int(request.form['Runs'])
        wickets = int(request.form['Wickets'])
        runs_last_5 = int(request.form['runs_last5overs'])
        wickets_last_5 = int(request.form['wickets_last5overs'])
        
        #temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        #temp_array = [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5] + temp_array
        xx=[runs, wickets, overs, runs_last_5, wickets_last_5]
        yy=temp_array
        zz=[xx+yy]
        df=pd.DataFrame(zz,columns=['runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5',
                                       'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils',
                                       'bat_team_Kings XI Punjab', 'bat_team_Kolkata Knight Riders',
                                       'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
                                       'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
                                       'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils',
                                       'bowl_team_Kings XI Punjab', 'bowl_team_Kolkata Knight Riders',
                                       'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
                                       'bowl_team_Royal Challengers Bangalore',
                                       'bowl_team_Sunrisers Hyderabad'])
        
        my_prediction = regressor.predict(df)
        output=round(my_prediction[0])
        #data = np.array([temp_array])
        #my_prediction = int(regressor.predict(data)[0])
              
        #return render_template('index.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)
        if my_prediction>0:
            return render_template('index.html',prediction_text=f'First Innings Predicted Score Range : {output-5} to {output+10}')
        else:
            return render_template('index.html',prediction_text= 'Nill')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
	#app.run(debug=True)