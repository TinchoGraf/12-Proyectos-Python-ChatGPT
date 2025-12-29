#Vamos a crear una funcion generica que pida los datos, arme el bucle, y devuelva el dato correcto
#Tambien vamos a crear funciones especificas que le pasen las reglas a esta funcion generica

#Funcion generica que pide un dato y lo valida con una funcion de validacion pasada por parametro
def PedirDato(dato, funcionValidacion):
    #ciclamos hasta que el dato sea valido
    while True:
            #pedimos el dato al usuario
            dato = input("Por favor, ingrese su dato: ")
            #enviamos el dato a validar a la funcion de validacion
            datoValido = funcionValidacion(dato)

            #si el dato es valido, lo devolvemos
            if datoValido["valido"]:
                return datoValido["valor"]
            
            #si no es valido, mostramos el mensaje de error
            else:
                print(datoValido["mensajeError"])

#Funcion especifica que valida el nombre
def ValidarNombre(nombre):
    #limpiamos espacios en blanco al inicio y al final
    nombreLimpio = nombre.strip()

    #chequeamos que el nombre no este vacio
    if nombreLimpio == "":
        #devolvemos un diccionario con el estado de la validacion
        return {"valido": False, "mensajeError": "El nombre no puede ser solo espacios en blanco. Intente nuevamente."}
    
    #chequeamos que el nombre no tenga numeros
    elif any(char.isdigit() for char in nombreLimpio):
        #devolvemos un diccionario con el estado de la validacion
        return {"valido": False, "mensajeError": "El nombre no puede contener números. Intente nuevamente."}
    else:
        #si todo esta bien, devolvemos el nombre limpio en un diccionario
        return {"valido": True, "valor": nombreLimpio}

#Funcion especifica que valida la edad
def ValidarEdad(edad):
    #creamos constantes para los minimos y maximos de la edad
    EDAD_MINIMA = 1
    EDAD_MAXIMA = 120

    #Hacemos el try-except para manejar errores de conversion
    try:    
        #convertimos la entrada a entero
        edadInt = int(edad)
        #chequeamos que la edad no sea negativa
        if edadInt < 0:
            return {"valido": False, "mensajeError": "La edad no puede ser negativa. Intente nuevamente."}
        #chequeamos que la edad este dentro de los limites
        elif edadInt < EDAD_MINIMA or edadInt > EDAD_MAXIMA:
            return {"valido": False, "mensajeError": f"La edad debe estar entre {EDAD_MINIMA} y {EDAD_MAXIMA}. Intente nuevamente."}
        else:
            #si todo esta bien, devolvemos la edad en un diccionario
            return {"valido": True, "valor": edadInt}

    #manejamos el error de conversion    
    except ValueError:
        return {"valido": False, "mensajeError": "Entrada inválida. Por favor, ingrese un número entero para la edad."}