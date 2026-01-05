#Importamos las funciones necesarias desde Validaciones.py
from RegistroDeNotas.Validaciones import PedirDato, ValidarNombre, ValidarEdad, GuardarEnJson

personas = []

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
