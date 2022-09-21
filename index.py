
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

    selecciones = []
    for key in check.keys():
        selecciones.append(key)

    print(selecciones)

    print("-----------------")
    datos_que_necesito = ["NOMBRE", "APELLIDO", "MODALIDAD", "DEPARTAMENTO", "direcciones", "REG NRO"]

    tabla_final = df.loc[:, datos_que_necesito]

    dataf = pd.DataFrame()
    

    # for ciudad in selecciones:
    #     fila_df = tabla_final.loc[df["DEPARTAMENTO"] == ciudad]
        

    #     if not fila_df.empty:
            
    #         print(ciudad)
    #         print(fila_df)
    #         dataf = pd.concat([dataf, fila_df])
    #         print("asjkdhaksjdhaskdhaksjda")
    #         print(dataf)


    # dataf = dataf.reset_index(drop=True)
    # tabla_final = dataf.to_dict()

    # print(tabla_final)

    for ciudad in selecciones:
        fila_df_ciudad = tabla_final.loc[df["DEPARTAMENTO"] == ciudad]
        fila_df_modalidad = tabla_final.loc[df["MODALIDAD"] == ciudad]
        


        if not fila_df_ciudad.empty:
            
            print(ciudad)
            print(fila_df_ciudad)
            dataf = pd.concat([dataf, fila_df_ciudad])
            print("asjkdhaksjdhaskdhaksjda")
            print(dataf)
        
        if not fila_df_modalidad.empty:
            
            print(ciudad)
            print(fila_df_modalidad)
            dataf = pd.concat([dataf, fila_df_modalidad])
            print("asjkdhaksjdhaskdhaksjda")
            print(dataf)


    dataf = dataf.reset_index(drop=True)
    tabla_final = dataf.to_dict()

    print(tabla_final)




    # return redirect(url_for('lista', tabla_final=tabla_final))
    return render_template("lista.html", tabla_final=tabla_final)
    # return "hola"


