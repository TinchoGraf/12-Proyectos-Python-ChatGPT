#Importamos los modulos necesarios para trabajar con JSON y manejo de archivos
import json

#Definimos como constante el archivo donde se guardaran los contactos
ARCHIVO_CONTACTOS = 'agenda.json'

#Funcion para cargar los contactos desde el archivo JSON
def cargar_contactos():
    try:
        with open(ARCHIVO_CONTACTOS, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

#Funcion para guardar los contactos en el archivo JSON
def guardar_contactos(contactos):
    with open(ARCHIVO_CONTACTOS, 'w') as archivo:
        json.dump(contactos, archivo, indent=4)

#Funcion para agregar un nuevo contacto
def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    email = input("Ingrese el email del contacto: ")
    
    contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }
    
    contactos.append(contacto)

    print("Contacto agregado exitosamente.")

#Funcion para buscar un contacto por nombre
def buscar_contacto(contactos):
    criterio = input("Ingrese el nombre del contacto a buscar: ")
    encontrados = [c for c in contactos if c['nombre'].lower() == criterio.lower()]
    
    if encontrados:
        for contacto in encontrados:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
    else:
        print("No se encontraron contactos con ese nombre.")

#Funcion para eliminar un contacto por nombre
def eliminar_contacto(contactos):
    criterio = input("Ingrese el nombre del contacto a eliminar: ")
    
    for c in contactos:
        if c['nombre'].lower() == criterio.lower():
            contactos.remove(c)
            print("Contacto eliminado exitosamente.")
            return
    
    print("No se encontró ningún contacto con ese nombre.")

#Funcion para mostrar todos los contactos
def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos en la agenda.")
        return
    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")    

#Funcion principal que maneja el menu y las opciones
def main():
    contactos = cargar_contactos()
    
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar Contacto")
        print("2. Buscar Contacto")
        print("3. Eliminar Contacto")
        print("4. Mostrar Todos los Contactos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_contacto(contactos)
        elif opcion == '2':
            buscar_contacto(contactos)
        elif opcion == '3':
            eliminar_contacto(contactos)
            guardar_contactos(contactos)
        elif opcion == '4':
            mostrar_contactos(contactos)
        elif opcion == '5':
            guardar_contactos(contactos)
            print("Saliendo de la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

#Ejecutamos la funcion principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
    