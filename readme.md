## Flask, Pandas and plots project.

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


