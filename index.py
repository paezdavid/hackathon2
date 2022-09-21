
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
    datos_que_necesito = ["NOMBRE", "APELLIDO", "MODALIDAD", "DEPARTAMENTO", "direcciones", "REG NRO"]
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

@app.route("/lista", methods = ['POST'])
def lista_filt():
    check = request.form.to_dict()
    print(check)
    

    # Leer el excel
    df = pd.read_excel("./plantillaa.xlsx")
    
    # departamentos = ['central', 'asuncion', 'concepcion', 'cordillera', 'guaira', 'caaguazu', 'caazapa', 'itapua', 'misiones', 'paraguari', 'alto parana', 'ñeembucu', 'amambay', 'canindeyu', 'presidente hayes', 'boqueron', 'alto paraguay']
    
    # for column in df:
        # fila = df.loc[df["DEPARTAMENTO"] == check["central"]]

        
        # print(df[column].values)

        # if df.loc[df["DEPARTAMENTO"] == check[depa]]:
        #     print(check[lista[depa]])

    selecciones = []
    for key in check.keys():
        selecciones.append(key)

    print(selecciones)
    # # Buscar una fila con el valor del id y guardarla en una variable
    # fila = df.loc[df["DEPARTAMENTO"] == selecciones[0]]

    print("-----------------")
    datos_que_necesito = ["NOMBRE", "APELLIDO", "MODALIDAD", "DEPARTAMENTO", "direcciones", "REG NRO"]

    tabla_final = df.loc[:, datos_que_necesito]

    dataf = pd.DataFrame()
    

    for ciudad in selecciones:
        fila_df = tabla_final.loc[df["DEPARTAMENTO"] == ciudad]
        

        # if fila_df.equals(tabla_final.loc[df["DEPARTAMENTO"] == ciudad]):
        
        # if tabla_final.loc[df["DEPARTAMENTO"] == ciudad].equals(fila_df):
        #     print("igual")
        #     print(fila_df)

        if not fila_df.empty:
            
            print(ciudad)
            print(fila_df)
            dataf = pd.concat([dataf, fila_df])
            print("asjkdhaksjdhaskdhaksjda")
            print(dataf)


    dataf = dataf.reset_index(drop=True)
    tabla_final = dataf.to_dict()

    print(tabla_final)





    # tabla_final = fila.to_dict(orient='list')

    # print(fila)

    # EL ERROR ESTÁ EN EL CASING DE LAS LETRAS
    

    # return redirect(url_for('lista', tabla_final=tabla_final))
    return render_template("lista.html", tabla_final=tabla_final)
    # return "hola"


