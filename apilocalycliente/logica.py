#Hacemos los imports necesarios

#Para guardar en formato json, vamos a usar la libreria json que viene incluida en python, no es necesario instalar nada
import json 

#Creamos una funcion que reciba por parametro una lista, nombre y edad de la persona nueva; y devuelva la lista actualizada/creada
def cargar_lista(lista_personas, nombre_persona, edad_persona):
    
    if len(lista_personas) == 0:
        id_persona = 1
    else:
        id_persona = len(lista_personas) + 1

    persona = {
        "id": id_persona,
        "nombre": nombre_persona,
        "edad": edad_persona
    }

    lista_personas.append(persona)

    return lista_personas

# Creamos una funcion que reciba por parametro una lista y un id de persona; y devuelva la persona que coincida con el id
def encontrar_persona_por_id(lista_personas, id_persona):
    for persona in lista_personas:
        if persona["id"] == id_persona:
            return persona
    return None
        
# Creamos una funcion que reciba por parametro una lista e imprima todas las personas en la lista y sus datos
def mostrar_personas(lista_personas):
    #Vamos a hacer que devuelva una copia de la lista para no modificar la original y que se pueda usar en otros contextos
    copia_lista = lista_personas.copy()
    return copia_lista

#Creamos una funcion que reciba por parametro una lista, un id, un nombre y una edad; y modifique la persona que coincida con el id
def modificar_persona(lista_personas, id_persona, nuevo_nombre, nueva_edad):
    persona_modificada = encontrar_persona_por_id(lista_personas, id_persona)
    if persona_modificada is None:
        return None
    if persona_modificada["nombre"] != nuevo_nombre:
        persona_modificada["nombre"] = nuevo_nombre
    if persona_modificada["edad"] != nueva_edad:
        persona_modificada["edad"] = nueva_edad
    return persona_modificada   

#Creamos una funcion que reciba por parametro una lista y un id; y elimine la persona que coincida con el id
def eliminar_persona(lista_personas, id_persona):
    persona_a_eliminar = encontrar_persona_por_id(lista_personas, id_persona)
    if persona_a_eliminar is None:
        return None
    lista_personas.remove(persona_a_eliminar)
    return persona_a_eliminar

#Creamos una funcion para guardar la lista en un archivo
def guardar_en_archivo(lista_personas, nombre_archivo):
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(lista_personas, archivo, indent=4)
            return { "estado": "ok", "accion": "guardar", "mensaje": "Lista guardada exitosamente", "data": lista_personas }
    except Exception as e:
        return { "estado": "error", "accion": "guardar", "mensaje": f"No se pudo guardar la lista: {str(e)}", "data": None }
    
    
#Creamos una funcion para cargar la lista desde un archivo
def cargar_desde_archivo(nombre_archivo):
    try:
            with open(nombre_archivo, "r") as archivo:
                lista_personas = json.load(archivo)
            return { "estado": "ok", "accion": "cargar_desde_archivo", "mensaje": "Lista cargada exitosamente", "data": lista_personas }
    except FileNotFoundError:
        return { "estado": "error", "accion": "cargar_desde_archivo", "mensaje": "No se encontro el archivo", "data": None }



#Creamos una funcion controladora que reciba por parametros, la accion a realizar, los datos y la lista
def controlador(accion, dato, lista_personas):
    
    #Si la accion es cargar, llamamos a la funcion cargar_lista y chequeamos los estados para devolver un mensaje adecuado
    if accion == "cargar":
        nombre_persona = dato.get("nombre")
        edad_persona = dato.get("edad")

        #Encapsulamos el resultado en una variable para luego chequear si es None o no
        result = cargar_lista(lista_personas, nombre_persona, edad_persona)

        #Si el resultado es None, devolvemos un mensaje de error, sino devolvemos un mensaje de exito
        if result is None:
            return { "estado": "error", "accion": "cargar", "mensaje": "No se pudo cargar a la persona", "data": None }
        else:
            return { "estado": "ok", "accion": "cargar", "mensaje": "Persona cargada exitosamente", "data": result }
    
    #Si la accion es encontrar, llamamos a la funcion encontrar_persona_por_id
    elif accion == "encontrar":

        id_persona = dato.get("id")

        #Encapsulamos el resultado en una variable para luego chequear si es None o no
        result = encontrar_persona_por_id(lista_personas, id_persona)
        
        #Si el resultado es None, devolvemos un mensaje de error, sino devolvemos un mensaje de exito
        if result is None:
            return { "estado": "error", "accion": "encontrar", "mensaje": "No se encontro a la persona", "data": None }
        else:
            return { "estado": "ok", "accion": "encontrar", "mensaje": "Persona encontrada exitosamente", "data": result }
   

    #Si la accion es mostrar, llamamos a la funcion mostrar_personas
    elif accion == "mostrar":

        result = mostrar_personas(lista_personas)

        #Si el resultado es None, devolvemos un mensaje de error, sino devolvemos un mensaje de exito
        if result is None:
            return { "estado": "error", "accion": "mostrar", "mensaje": "No se pudieron mostrar las personas", "data": None }
        else:
            return { "estado": "ok", "accion": "mostrar", "mensaje": "Personas mostradas exitosamente", "data": result }
    
    #Si la accion es modificar, llamamos a la funcion modificar_persona
    elif accion == "modificar":

        #Extraemos los datos necesarios del diccionario dato
        id_persona = dato.get("id")
        nuevo_nombre = dato.get("nombre")
        nueva_edad = dato.get("edad")


        result = modificar_persona(lista_personas, id_persona, nuevo_nombre, nueva_edad)

        #Si el resultado es None, devolvemos un mensaje de error, sino devolvemos un mensaje de exito
        if result is None:
            return { "estado": "error", "accion": "modificar", "mensaje": "No se pudo modificar a la persona", "data": None }
        else:
            return { "estado": "ok", "accion": "modificar", "mensaje": "Persona modificada exitosamente", "data": result }

    #Si la accion es eliminar, llamamos a la funcion eliminar_persona    
    elif accion == "eliminar":

        id_persona = dato.get("id")


        result = eliminar_persona(lista_personas, id_persona)

        #Si el resultado es None, devolvemos un mensaje de error, sino devolvemos un mensaje de exito
        if result is None:
            return { "estado": "error", "accion": "eliminar", "mensaje": "No se pudo eliminar a la persona", "data": None }
        else:
            return { "estado": "ok", "accion": "eliminar", "mensaje": "Persona eliminada exitosamente", "data": result }

    #Si la accion no es ninguna de las anteriores, devolvemos un mensaje de error    
    else:
        return { "estado": "error", "accion": accion, "mensaje": "Accion no reconocida", "data": None }
    
