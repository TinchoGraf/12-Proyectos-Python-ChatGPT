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
        return datos

def agregar_persona(personas):

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

def listar_personas(personas):
    if not personas:
        print("No hay personas para listar.")
        return
    
    print("\nListado completo de personas:")
    for idx, persona in enumerate(personas, start=1):
        print(f"{idx}. Nombre: {persona['nombre']}, Edad: {persona['edad']}")

def editar_persona(personas):
    if not personas:
        print("No hay personas para editar.")
        return
    
    while True:
        listar_personas(personas)
        indice = input("\nIngrese el número de la persona a editar (o 'salir' para terminar): ")
        
        if indice.lower() == 'salir':
            break
        
        if not indice.isdigit() or int(indice) < 1 or int(indice) > len(personas):
            print("Índice inválido. Intente nuevamente.")
            continue
        
        indice = int(indice) - 1
        persona = personas[indice]
        
        print(f"Editando persona: {persona['nombre']}, Edad: {persona['edad']}")
        
        nuevo_nombre = PedirDato("Ingrese el nuevo nombre (o presione Enter para mantener el actual): ", ValidarNombre)
        if nuevo_nombre["estado"] == "error":
            print(nuevo_nombre["mensajeError"])
            continue
        elif nuevo_nombre["estado"] != "corte" and nuevo_nombre["valor"] != "":
            persona['nombre'] = nuevo_nombre["valor"]
        
        nueva_edad = PedirDato("Ingrese la nueva edad (o presione Enter para mantener la actual): ", ValidarEdad)
        if nueva_edad["estado"] == "error":
            print(nueva_edad["mensajeError"])
            continue
        elif nueva_edad["estado"] != "corte" and nueva_edad["valor"] != "":
            persona['edad'] = nueva_edad["valor"]
        
        print("Persona actualizada exitosamente.")

def eliminar_personas(personas):
    if not personas:
        print("No hay personas para eliminar.")
        return
    
    while True:
        listar_personas(personas)
        indice = input("\nIngrese el número de la persona a eliminar (o 'salir' para terminar): ")
        
        if indice.lower() == 'salir':
            break
        
        if not indice.isdigit() or int(indice) < 1 or int(indice) > len(personas):
            print("Índice inválido. Intente nuevamente.")
            continue
        
        indice = int(indice) - 1
        persona_eliminada = personas.pop(indice)
        print(f"Persona eliminada: {persona_eliminada['nombre']}, Edad: {persona_eliminada['edad']}")

def menu_interactivo(personas):
    
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar persona")
        print("2. Listar personas") 
        print("3. Eliminar persona")
        print("4. Procesar datos")
        print("5. Editar persona")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")
        if opcion == '1':
            agregar_persona(personas)
        elif opcion == '2':
            listar_personas(personas)
        elif opcion == '3':
            eliminar_personas(personas)
        elif opcion == '4':
            procesamiento_de_datos(personas)
        elif opcion == '5':
            editar_persona(personas)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def main():
    personas = CargarDesdeJson("personas.json")
    menu_interactivo(personas)
    if personas:
        GuardarEnJson("personas.json", personas)
        print("Datos guardados en 'personas.json'.")

if __name__ == "__main__":
    main()
