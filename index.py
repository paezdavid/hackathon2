from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Columnas que voy a mostrar en el front
    datos_que_necesito = ["NOMBRE", "APELLIDO", "MODALIDAD", "direcciones"]
    # Dataframe donde se alojan las columnas extraídas
    df = pd.read_excel("./plantilla_def.xlsx")
    # Dataframe convertido a diccionario para mandarlo al frontend
    tabla_final = df.loc[:, datos_que_necesito].to_dict(orient='dict')

    

    return render_template("index.html", tabla_final=tabla_final)




   