#Agregamos los imports necesarios para crear el servidor con Flask
from flask import Flask, jsonify
from logica import controlador
from flask import request


#Creamos una lista vacia para pasar por parametro, luego se eliminará para cargarla y descargarla desde un archivo
lista_personas = []

#Creamos la instancia de la aplicación Flask
app = Flask(__name__)

#Definimos una ruta para el endpoint raíz que devolverá un mensaje indicando que el servidor está funcionando correctamente
@app.route("/")
def inicio():
    return "Servidor funcionando correctamente"

#Definimos una ruta para el endpoint "/personas" que devolverá la lista de personas en formato JSON utilizando la función controlador para obtener los datos
@app.route("/personas", methods=["GET"])
def obtener_personas():
    
    resultado = controlador("mostrar", {}, lista_personas)
    
    return jsonify(resultado)

#Definimos una ruta para el endpoint "/personas" que permitirá agregar una nueva persona a la lista utilizando la función controlador para procesar los datos recibidos en formato JSON
@app.route("/personas", methods=["POST"])
def agregar_persona():

    datos = request.get_json()

    resultado = controlador("cargar", datos, lista_personas)

    return jsonify(resultado)

#Hacemos que el servidor ejecute en modo debug para que se reinicie automáticamente cada vez que hagamos cambios en el código
if __name__ == "__main__":
    app.run()

