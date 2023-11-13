## Flask, Pandas and plots project.

Aquest projecte inclou com carregar dataframes (Pandas), serveis web (Flask, request), gràfics amb llibreries (Seaborn, Plotly) i plantilles 
Jinja per tal de tenir una base per crear un portal de dades obertes atractiu.

Li faltarien mecanismes com els formularis, la gestió d'usuaris i sessions securitzades per a ser una plantilla per a projectes de DAWBIO completa; que 
quedarà pendent crear-la a inicis del 2024.

### Install venv environment.

```bash
$ sudo apt update
$ sudo apt install python3-venv -y
$ python3 -m venv .venv
$ (venv) source .venv/bin/activate
$ (venv) pip install -r requirements.txt
```

### Run project 

Start the web app in reload mode:

```bash
$ flask run --reload -h 0.0.0.0
* Environment: production
...
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open a terminal and get IP addr:

$ ip --brief addr
Fire up a web browser and navigate to http://<ip>:5000

### Dataset source

<a href="https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/">🌍 Original source and examples, Kaggle website.🌍</a>

#### Columns

Patient ID,Age,Sex,Cholesterol,Blood Pressure,Heart Rate,Diabetes,Family History,Smoking,Obesity,Alcohol Consumption,Exercise Hours Per Week,Diet,Previous Heart Problems,Medication Use,Stress Level,Sedentary Hours Per Day,Income,BMI,Triglycerides,Physical Activity Days Per Week,Sleep Hours Per Day,Country,Continent,Hemisphere,Heart Attack Risk


### Test POST, PUT, DELETE without forms or external plugins:

In Linux:


curl -X POST -H "Content-Type: application/json" -d '{"Age": 21, "Sex": "Male", "Cholesterol": 389, "Blood Pressure": "165/93", "Heart Rate": 98, "Diabetes": 1, "Family History": 1, "Smoking": 1, "Obesity": 1, "Alcohol Consumption": 1, "Exercise Hours Per Week": 1.8132416178634458, "Diet": "Unhealthy", "Previous Heart Problems": 1, "Medication Use": 0, "Stress Level": 1, "Sedentary Hours Per Day": 4.963458839757678, "Income": 285768, "BMI": 27.1949733519874, "Triglycerides": 235, "Physical Activity Days Per Week": 1, "Sleep Hours Per Day": 7, "Country": "Canada", "Continent": "North America", "Hemisphere": "Northern Hemisphere", "Heart Attack Risk": 0}' http://localhost:5000/patient/CZE1117

curl -X DELETE http://localhost:5000/patient/BMW7812

curl -X PUT -H "Content-Type: application/json" -d '{"Age": 35, "Sex": "Male", "Cholesterol": 220, "Blood Pressure": "130/85", "Heart Rate": 75, "Diabetes": 0, "Family History": 1, "Smoking": 0, "Obesity": 1, "Alcohol Consumption": 1, "Exercise Hours Per Week": 3, "Diet": "Healthy", "Previous Heart Problems": 0, "Medication Use": 0, "Stress Level": 5, "Sedentary Hours Per Day": 8, "Income": 60000, "BMI": 25, "Triglycerides": 200, "Physical Activity Days Per Week": 4, "Sleep Hours Per Day": 7, "Country": "Spain", "Continent": "Europe", "Hemisphere": "Northern Hemisphere", "Heart Attack Risk": 0}' http://localhost:5000/patient/BMW7812


