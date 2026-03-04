#Agregamos los imports necesarios para crear el servidor con Flask
from flask import Flask, jsonify
from logica import controlador
from flask import request
from logica import cargar_desde_archivo

#Cargamos la lista de personas desde el archivo al iniciar el servidor para tener los datos disponibles en memoria
lista_personas = cargar_desde_archivo()

#Creamos la instancia de la aplicación Flask
app = Flask(__name__)

#Definimos una ruta para el endpoint raíz que devolverá un mensaje indicando que el servidor está funcionando correctamente
@app.route("/")
def inicio():
    return "Servidor funcionando correctamente"

#Definimos una ruta para el endpoint "/personas" que devolverá la lista de personas en formato JSON utilizando la función controlador para obtener los datos
@app.route("/personas", methods=["GET"])
def obtener_personas():
                                    #Diccionario vacio para pasar por parametro a la funcion controlador, luego se eliminará para cargarlo con los datos necesarios
    resultado = controlador("mostrar",{}, lista_personas)
    
    return jsonify(resultado)

#Definimos una ruta para el endpoint "/personas" que permitirá agregar una nueva persona a la lista utilizando la función controlador para procesar los datos recibidos en formato JSON
@app.route("/personas", methods=["POST"])
def agregar_persona():

    datos = request.get_json()

    resultado = controlador("cargar", datos, lista_personas)

    return jsonify(resultado)

#Definimos una ruta para el endpoint "/personas/<int:id>" que permitirá ver una persona específica por su ID utilizando la función controlador para procesar el ID recibido como parámetro en la URL
@app.route("/personas/<int:id_persona>", methods=["GET"])
def obtener_persona_por_id(id_persona):

    datos = {"id": id_persona}

    resultado = controlador("encontrar", datos, lista_personas)

    if resultado["estado"] == "error":
        return jsonify(resultado), 404

    return jsonify(resultado), 200

#Hacemos un endpoint para eliminar una persona por su ID utilizando la función controlador para procesar el ID recibido como parámetro en la URL
@app.route("/personas/<int:id_persona>", methods=["DELETE"])
def eliminar_persona(id_persona):

    datos = {"id": id_persona}

    resultado = controlador("eliminar", datos, lista_personas)

    if resultado["estado"] == "error":
        return jsonify(resultado), 404

    return jsonify(resultado), 200

#Hacemos un endpoint para actualizar una persona por su ID utilizando la función controlador para procesar el ID recibido como parámetro en la URL y los datos recibidos en formato JSON
@app.route("/personas/<int:id_persona>", methods=["PUT"])
def modificar_persona(id_persona):

    datos = request.get_json()
    datos["id"] = id_persona

    resultado = controlador("modificar", datos, lista_personas)

    if resultado["estado"] == "error":
        return jsonify(resultado), 404

    return jsonify(resultado), 200

#Hacemos que el servidor ejecute en modo debug para que se reinicie automáticamente cada vez que hagamos cambios en el código
if __name__ == "__main__":
    app.run()

