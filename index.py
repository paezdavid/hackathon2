
from flask import Flask, render_template, url_for, session, redirect, request
import pandas as pd
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    # Columnas que voy a mostrar en el front
    datos_que_necesito = ["NOMBRE", "APELLIDO", "MODALIDAD", "LATITUD", "LONGITUD", "direcciones", "REG NRO"]
    # Dataframe donde se alojan las columnas extraídas
    df = pd.read_excel("./testeo_markers.xlsx")
    # Dataframe convertido a diccionario para mandarlo al frontend
    tabla_final = df.loc[:, datos_que_necesito].to_dict(orient='dict')

    

    return render_template("index.html", tabla_final=tabla_final)




@app.route("/perfiles/<string:perfil_id>")
def perfil(perfil_id):

    # Leer el excel
    df = pd.read_excel("./testeo_markers.xlsx")
    
    # Buscar una fila con el valor del id y guardarla en una variable
    fila = df.loc[df["REG NRO"] == int(perfil_id)]
    
    # Convertir fila df a dict
    fila_dict = fila.to_dict(orient='dict')

    return render_template("perfil.html", fila=fila_dict)

    

    # session['my_var'] = 'my_value'
    # return redirect(url_for('b'))