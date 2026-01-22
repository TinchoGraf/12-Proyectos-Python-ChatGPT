#Importamos las funciones necesarias desde Validaciones.py
from registro_de_notas.Validaciones import PedirDato, ValidarNombre, ValidarEdad, GuardarEnJson
import os
import json

CORTE = "*"

def CargarDesdeJson(nombreArchivo):

    if not os.path.exists(nombreArchivo):
        return []

    with open(nombreArchivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos.get("personas", [])

personas = CargarDesdeJson("personas.json")

print("Ingrese los datos de las personas.")
print(f"Para finalizar, ingrese '{CORTE}' como nombre.")

while True:
    nombre = PedirDato("Ingrese el nombre: ", ValidarNombre)

    if nombre["estado"] == "corte":
        print("Ingreso finalizado.")
        break

    elif nombre["estado"] == "error":
        print(nombre["mensajeError"])
        continue

    edad = PedirDato("Ingrese la edad: ", ValidarEdad)

    if edad["estado"] == "error":
        print(edad["mensajeError"])
        continue

    persona = {
        "nombre": nombre["valor"],
        "edad": edad["valor"]
    }

    personas.append(persona)

def procesamiento_de_datos(personas):
    if not personas:
        print("No hay personas cargadas para procesar.")
        return
    
    print("\nProcesando datos de las personas ingresadas:")

    print(f"\nTotal de personas ingresadas: {len(personas)}")

    print("\nListado de personas:")
    for idx, persona in enumerate(personas, start=1):
        print(f"{idx}. Nombre: {persona['nombre']}, Edad: {persona['edad']}")

procesamiento_de_datos(personas)

if not personas:
    print("No hay datos guardados en la lista.")
else:
    GuardarEnJson("personas.json", personas)
    print("Datos guardados en 'personas.json'.")