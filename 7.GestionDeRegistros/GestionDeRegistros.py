#Importamos las funciones necesarias desde Validaciones.py
from registro_de_notas.Validaciones import PedirDato, ValidarNombre, ValidarEdad, GuardarEnJson

CORTE = "*"

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

