
from flask import Flask, render_template, url_for, session, redirect, request
import pandas as pd
import requests


app = Flask(__name__)

@app.route("/")
def index():

   return render_template("landing.html")


@app.route("/lista")
def lista():
    # Columnas que voy a mostrar en el front
    datos_que_necesito = ["NOMBRE", "APELLIDO", "MODALIDAD", "LATITUD", "LONGITUD", "direcciones", "REG NRO"]
    # Dataframe donde se alojan las columnas extraídas
    df = pd.read_excel("./plantillaa.xlsx")
    # Dataframe convertido a diccionario para mandarlo al frontend
    tabla_final = df.loc[:, datos_que_necesito].to_dict(orient='dict')

    

    return render_template("lista.html", tabla_final=tabla_final)
    




@app.route("/perfiles/<string:perfil_id>")
def perfil(perfil_id):

    # Leer el excel
    df = pd.read_excel("./plantillaa.xlsx")
    
    # Buscar una fila con el valor del id y guardarla en una variable
    fila = df.loc[df["REG NRO"] == int(perfil_id)]

    print(fila)
    
    # Convertir fila df a dict
    fila_dict = fila.to_dict(orient='list')

    print(fila_dict)

    return render_template("perfil.html", fila=fila_dict)
    # return render_template("landing.html")
    # return render_template("filtros.html")

    

    # session['my_var'] = 'my_value'
    # return redirect(url_for('b'))

@app.route("/perfiless", methods = ['POST'])
def perfiil():

    check = request.form.to_dict()
    print(check)

    return "hola"


