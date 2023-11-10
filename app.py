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

@app.route("/plots")
def plots():
    grafic1 = plot1(df)
    grafic2 = plot2(df)
    return render_template("plots.html",title="Pt2-Plots",grafic1=grafic1,grafic2=grafic2)

@app.route("/maps")
def maps():
    return render_template("maps.html",title="Pt2-Map")

# PLOTS

@app.route('/map1')
def notdash():
   df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
   fig = px.bar(df, x='Fruit', y='Amount', color='City',    barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('notdash.html', graphJSON=graphJSON)

# MAIN

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)