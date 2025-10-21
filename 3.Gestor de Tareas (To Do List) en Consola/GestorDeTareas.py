#Creamos la funcion que agrega tareas a la lista de pendientes
def agregar_tarea(tareas_pendientes):
    tarea = input("Ingrese la tarea que desea agregar: ")
    tareas_pendientes.append(tarea)
    print(f"Tarea '{tarea}' agregada a la lista de pendientes.")

#Creamos la funcion que permite ver las tareas pendientes y completadas
def ver_tareas(tareas_pendientes, tareas_completadas):
    print("\nTareas Pendientes:")
    #En caso de que no haya tareas pendientes, indicamos que no hay tareas
    if not tareas_pendientes:
        print("No hay tareas pendientes.")
    else:
        #Mostramos las tareas pendientes con su indice
        for idx, tarea in enumerate(tareas_pendientes, 1):
            print(f"{idx}. {tarea}")

    print("\nTareas Completadas:")
    #En caso de que no haya tareas completadas, indicamos que no hay tareas
    if not tareas_completadas:
        print("No hay tareas completadas.")
    else:
        #Mostramos las tareas completadas con su indice
        for idx, tarea in enumerate(tareas_completadas, 1):
            print(f"{idx}. {tarea}")

#Creamos la funcion que elimina tareas de lista de pendientes
def eliminar_tarea(tareas_pendientes):
    #Mostramos las tareas pendientes para que el usuario pueda elegir cual eliminar
    ver_tareas(tareas_pendientes, [])
    try:
        #Le pedimos al usuario el numero de la tarea que desea eliminar
        indice = int(input("Ingrese el numero de la tarea que desea eliminar: "))
        #Controlamos que el indice sea valido
        if 1 <= indice <= len(tareas_pendientes):
            #Eliminamos la tarea de la lista de pendientes
            tarea_eliminada = tareas_pendientes.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada}' eliminada de la lista de pendientes.")
        else:
            #En caso de que el indice no sea valido, mostramos un mensaje de error
            print("Indice invalido.")
    except ValueError:
        #En caso de que el usuario ingrese un valor no numerico, mostramos un mensaje de error
        print("Por favor, ingrese un numero valido.")

#Creamos la funcion que marca una tarea como completada
def completar_tarea(tareas_pendientes, tareas_completadas):
    #Mostramos las tareas pendientes para que el usuario pueda elegir cual completar
    ver_tareas(tareas_pendientes, [])
    try:
        #Le pedimos al usuario el numero de la tarea que desea completar
        indice = int(input("Ingrese el numero de la tarea que desea completar: "))
        #Controlamos que el indice sea valido
        if 1 <= indice <= len(tareas_pendientes):
            #Movemos la tarea de la lista de pendientes a la lista de completadas
            tarea_completada = tareas_pendientes.pop(indice - 1)
            tareas_completadas.append(tarea_completada)
            print(f"Tarea '{tarea_completada}' marcada como completada.")
        else:
            #En caso de que el indice no sea valido, mostramos un mensaje de error
            print("Indice invalido.")
    except ValueError:
        #En caso de que el usuario ingrese un valor no numerico, mostramos un mensaje de error
        print("Por favor, ingrese un numero valido.")

#Definimos la funcion que guarda las tareas en los archivos correspondientes
def guardar_tareas(tareas_pendientes, tareas_completadas):
    #Abrimos el archivo de tareas pendientes en modo escritura
    with open("tareas_pendientes.txt", "w") as archivo_pendientes:
        #Escribimos cada tarea pendiente en una nueva linea del archivo
        for tarea in tareas_pendientes:
            archivo_pendientes.write(tarea + "\n")
    
    #Abrimos el archivo de tareas completadas en modo escritura
    with open("tareas_completadas.txt", "w") as archivo_completadas:
        #Escribimos cada tarea completada en una nueva linea del archivo
        for tarea in tareas_completadas:
            archivo_completadas.write(tarea + "\n")

#Cerramos los archivos y guardamos las tareas al salir del programa
def salir(tareas_pendientes, tareas_completadas):
    guardar_tareas(tareas_pendientes, tareas_completadas)
    print("Tareas guardadas. Saliendo del programa.")
   
    exit()

#Creamos un menu para que el usuario pueda elegir que accion realizar
def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Eliminar Tarea")
    print("4. Completar Tarea")
    print("5. Salir")
    eleccion = input("Seleccione una opcion (1-5): ")
    return eleccion

#Defininimos el proceso principal de la aplicacion MAIN
def main():

    #Creamos las listas vacias para las tareas
    tareas_pendientes = []
    tareas_completadas = []

    #Abrimos los archivos donde se guardan las tareas, en caso de que no existan los creamos
    #En caso de que si existan, leemos las tareas y las almacenamos en las listas correspondientes

    try:
        #Abrimos el archivo de tareas pendientes en modo lectura
        with open("tareas_pendientes.txt", "r") as archivo_pendientes:
            #Por cada linea en el archivo, la agregamos a la lista de tareas pendientes
            for linea in archivo_pendientes:
                tareas_pendientes.append(linea.strip())
    #En caso de que no exista el archivo, lo creamos en modo escritura
    except FileNotFoundError:
        with open("tareas_pendientes.txt", "w") as archivo_pendientes:
            pass
    
    try:
        #Abrimos el archivo de tareas completadas en modo lectura
        with open("tareas_completadas.txt", "r") as archivo_completadas:
            #Por cada linea en el archivo, la agregamos a la lista de tareas completadas
            for linea in archivo_completadas:
                tareas_completadas.append(linea.strip())
    #En caso de que no exista el archivo, lo creamos en modo escritura
    except FileNotFoundError:
        with open("tareas_completadas.txt", "w") as archivo_completadas:
            pass

#Creamos un bucle infinito para mostrar el menu y procesar las opciones del usuario hasta que el usuario decida salir
    while True:
        eleccion = mostrar_menu()
        if eleccion == "1":
            agregar_tarea(tareas_pendientes)
        elif eleccion == "2":
            ver_tareas(tareas_pendientes, tareas_completadas)
        elif eleccion == "3":
            eliminar_tarea(tareas_pendientes)
        elif eleccion == "4":
            completar_tarea(tareas_pendientes, tareas_completadas)
        elif eleccion == "5":
            salir(tareas_pendientes, tareas_completadas)
        else:
            print("Opcion invalida. Por favor, seleccione una opcion del 1 al 5.")

#Llamamos a la funcion main para iniciar la aplicacion
main()  