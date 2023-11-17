from flask import Flask, render_template, request, Response
from flask_restful import Resource, Api
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import json
# Our modules.
import data
from mod_plots import *

app = Flask(__name__)
api = Api(app)

df = data.df

# WEB SERVICES 
class PersonResource(Resource):

    def get(self, id):
        data = df[df['Patient ID'] == id]
        if data.empty:
            return {"error": "patient id not found", "id": id}, 404

        return Response(
            data.to_json(orient="records"),
            mimetype='application/json')
    
    def update_person_data(self, id, data_json):
        # Verifica que les dades proporcionades són correctes i compleixen amb les columnes del DataFrame
        required_columns = ["Age", "Sex", "Cholesterol", "Blood Pressure", "Heart Rate"]
        for column in required_columns:
            if column not in data_json:
                return {"error": f"{column} is required in the request body"}, 400

        # Obté les dades existents de la persona amb l'ID proporcionat
        existing_person_data = df[df["Patient ID"] == id].to_dict(orient="records")[0]

        # Actualitza les dades existents amb les noves dades proporcionades
        existing_person_data.update(data_json)

        # Retorna les dades actualitzades
        return existing_person_data

    def post(self, id):
        global df  # Afegit per indicar que estem fent referència a la variable global df
        data_json = request.get_json()

        # Crida al mètode update_person_data per afegir o actualitzar la persona
        new_person_data = self.update_person_data(id, data_json)

        # Crea un nou DataFrame amb les dades actualitzades
        new_df = pd.DataFrame([new_person_data])

        # Afegeix la nova persona al DataFrame
        df = pd.concat([df, new_df], ignore_index=True)

        return {"message": "Person added successfully", "data": new_person_data}, 201


    def put(self, id):
        global df  # Afegit per indicar que estem fent referència a la variable global df
        data_json = request.get_json()
        # Verifica que les dades proporcionades són correctes i compleixen amb les columnes del DataFrame
        required_columns = ["Age", "Sex", "Cholesterol", "Blood Pressure", "Heart Rate"]
        for column in required_columns:
            if column not in data_json:
                return {"error": f"{column} is required in the request body"}, 400

         # Obté les dades existents de la persona amb l'ID proporcionat
        existing_person_data = df[df["Patient ID"] == id].to_dict(orient="records")[0]

        # Filtra les claus del diccionari perquè coincideixin amb les columnes del DataFrame
        filtered_data_json = {column: data_json[column] for column in required_columns}

        # Actualitza les dades existents amb les noves dades proporcionades
        existing_person_data.update(filtered_data_json)

        # Retorna les dades actualitzades
        return {"message": "Person updated successfully", "data": existing_person_data}, 200


    def delete(self, id):
        global df  # Afegit per indicar que estem fent referència a la variable global df

        # Obté les dades de la persona que es vol eliminar
        existing_person_data = df[df["Patient ID"] == id].to_dict(orient="records")[0]

        # Elimina la persona del DataFrame
        df = df[df["Patient ID"] != id]

        return {"message": "Person deleted successfully", "data": existing_person_data}, 200


    def options(self, id):
        # Exemple de com processar les sol·licituds OPTIONS
        # Pots personalitzar això segons les teves necessitats
        return {'Allow': 'GET, POST, PUT, DELETE, OPTIONS'}, 200

api.add_resource(PersonResource, "/patient/<id>")


@app.route("/patient")
def patients():
    print("Hey!")
    data = df.head(50)
    return Response(
        data.to_json(orient="records"),
        mimetype='application/json')


@app.route("/patient/<field>/<value>")
def query(field, value):
    if field == "Age":
        value = int(value)

    print('value=',value)
    data = df[df[field] == value]
    if data.empty:
        return {"error": "no data found", "field": field, "value": value}, 404

    # data = data.to_json(orient="records")
    return Response(
        data.to_json(orient="records"),
        mimetype='application/json')


# WEB PAGE ROUTES
@app.route("/")
def index():
    return render_template("index.html",title="Pt2-Landing page")

@app.route("/apis")
def apis():
    return render_template("apis.html",title="Pt2-APIs")

#PLOTS
@app.route("/plots")
def plots():
    grafic1 = plot1(df)
    grafic2 = plot2(df)
    return render_template("plots.html",title="Pt2-Plots",grafic1=grafic1,grafic2=grafic2)

@app.route("/maps")
def maps():
    fig = map1(df)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("maps.html",title="Pt2-Map", graphJSON=graphJSON)
    
# MAIN

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
