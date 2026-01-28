

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
