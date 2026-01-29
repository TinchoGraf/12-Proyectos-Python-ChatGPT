

#Creamos una lista vacia para pasar por parametro, luego se eliminará para cargarla y descargarla desde un archivo
lista_personas = []

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


