#Importamos la clase JSON para manejar archivos JSON

import json
import os

#Asignamos una constante para el nombre del archivo que contiene las preguntas y respuestas

# Siempre usa la ruta del script, no la del entorno de ejecución
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_PREGUNTAS = os.path.join(BASE_DIR, 'preguntas.json')

#Definimos una función para cargar las preguntas desde el archivo JSON
def cargar_preguntas():
    try:
         #Abrimos el archivo en modo lectura y cargamos su contenido en una variable
         with open(ARCHIVO_PREGUNTAS, 'r', encoding='utf-8') as archivo:
             preguntas = json.load(archivo)
         return preguntas  
    except FileNotFoundError:
        print(f"Error: El archivo {ARCHIVO_PREGUNTAS} no fue encontrado.")
        return []  

#Definimos una función para ejecutar el quiz
def ejecutar_quiz():
    #Damos un mensaje de bienvenida al usuario
    print("¡Bienvenido al Quiz Interactivo!\n")

    #Cargamos las preguntas y inicializamos el puntaje
    preguntas = cargar_preguntas()

    #Verificamos si se cargaron preguntas
    if not preguntas:
        print("No hay preguntas disponibles.")
        return


    puntaje = 0

    #Iteramos sobre cada pregunta en la lista de preguntas
    for pregunta in preguntas:
        #Mostramos la pregunta y las opciones de respuesta
        print(pregunta['pregunta'])
        for i, opcion in enumerate(pregunta['opciones'], start=1):
            print(f"{i}. {opcion}")
        
        #Solicitamos la respuesta del usuario
        #Encerramos en un bloque de try y except para manejar entradas inválidas
        try:
            respuesta_usuario = input("Seleccione el número de su respuesta: ")
            if int(respuesta_usuario) < 1 or int(respuesta_usuario) > len(pregunta['opciones']):
                raise ValueError
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.\n")
            continue

        #Verificamos si la respuesta es correcta y actualizamos el puntaje
        respuesta_correcta = pregunta['respuesta_correcta']
        letra_elegida = pregunta['opciones'][int(respuesta_usuario) - 1][0]  # toma la letra antes del paréntesis
        if letra_elegida == respuesta_correcta:
            print("¡Correcto!\n")
            puntaje += 1

        else:
            print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}\n")


    
    #Luego de todas las preguntas, mostramos el puntaje final
    print(f"Tu puntaje final es: {puntaje} de {len(preguntas)}")

    #Tambien lo imprimimos como porcentaje
    #Calculamos el porcentaje y lo mostramos
    porcentaje = (puntaje / len(preguntas)) * 100   

    print(f"Porcentaje de aciertos: {porcentaje:.2f}%")


#Ejecutamos el quiz si el archivo es ejecutado directamente
if __name__ == "__main__":
    ejecutar_quiz()

