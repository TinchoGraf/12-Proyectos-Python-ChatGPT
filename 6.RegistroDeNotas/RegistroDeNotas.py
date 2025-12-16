#Vamos a generar un programa que permita registrar las notas de los estudiantes en un curso.
#El programa debe permitir agregar estudiantes, registrar sus notas y calcular el promedio de cada estudiante.

#Primero codificaremos el menu principal del programa 
def mostrar_menu():
    print("----- Registro de Notas -----")
    print("1. Agregar estudiante")
    print("2. Registrar nota a estudiante existente")
    print("3. Mostrar estudiantes y sus notas")
    print("4. Calcular promedio y notas mas altas y bajas")
    print("5. Guardar los datos a un archivo")
    print("6. Salir")

#Luego pedimos al usuario que elija una opcion del menu
def obtener_opcion():
    #Envolvemos la entrada en un bloque try-except para manejar errores de entrada
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 6: "))

            if numero < 1 or numero > 6:
                raise ValueError  # error lógico: fuera de rango

            break  # si llegó acá, el número es válido

        except ValueError:
            print("Entrada inválida. Debe ser un número entre 1 y 6.")

    return numero



#Creamos la funcion principal que segun la opcion que elija el usuario, llamara a las funciones correspondientes
def main():
    estudiantes = {}

    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == '1':
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            registrar_nota(estudiantes)
        elif opcion == '3':
            mostrar_estudiantes(estudiantes)
        elif opcion == '4':
            calcular_promedios(estudiantes)
        elif opcion == '5':
            guardar_datos(estudiantes)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
