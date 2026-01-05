#Vamos a crear una funcion generica que pida los datos, arme el bucle, y devuelva el dato correcto
#Tambien vamos a crear funciones especificas que le pasen las reglas a esta funcion generica

#creamos constantes para los minimos y maximos de la edad
EDAD_MINIMA = 1
EDAD_MAXIMA = 120
#agregamos una constante de corte para los bucles de ingreso
CORTE = "*"

#Funcion generica que pide un dato y lo valida con una funcion de validacion pasada por parametro
def PedirDato(mensaje, funcionValidacion):
    
            #pedimos el dato al usuario recordandole la opcion de corte
            dato = input(mensaje)

            if dato == CORTE:
                return {"valido": False, "estado": "corte"}

            #enviamos el dato a validar a la funcion de validacion
            datoValido = funcionValidacion(dato)

            return datoValido
            

#Funcion especifica que valida el nombre
def ValidarNombre(nombre):

    
    #limpiamos espacios en blanco al inicio y al final
    nombreLimpio = nombre.strip()


    #chequeamos que el nombre no este vacio
    if nombreLimpio == "":
        #devolvemos un diccionario con el estado de la validacion
        return {"valido": False,
                "estado": "error",
                 "mensajeError": "El nombre no puede ser solo espacios en blanco. Intente nuevamente."
        }    
    
    #chequeamos que el nombre no tenga numeros
    elif any(char.isdigit() for char in nombreLimpio):
        #devolvemos un diccionario con el estado de la validacion
        return {"valido": False,
                "estado": "error",
                 "mensajeError": "El nombre no puede contener números. Intente nuevamente."
        }
    

    #si todo esta bien, devolvemos el nombre limpio en un diccionario
    return {"valido": True,
            "estado": "ok",
             "valor": nombreLimpio}

#Funcion especifica que valida la edad
def ValidarEdad(edad):


    #Hacemos el try-except para manejar errores de conversion
    try:    
       
        #convertimos la entrada a entero
        edadInt = int(edad)

        #chequeamos que la edad no sea negativa
        if edadInt < 0:
            return {"valido": False,
                    "estado": "error", 
                    "mensajeError": "La edad no puede ser negativa. Intente nuevamente."}
        #chequeamos que la edad este dentro de los limites
        elif edadInt < EDAD_MINIMA or edadInt > EDAD_MAXIMA:
            return {"valido": False,
                    "estado": "error",
                     "mensajeError": f"La edad debe estar entre {EDAD_MINIMA} y {EDAD_MAXIMA}. Intente nuevamente."
            }
        #si todo esta bien, devolvemos la edad en un diccionario
        return {"valido": True,
                "estado": "ok",
                "valor": edadInt}

    #manejamos el error de conversion    
    except ValueError:
        return {"valido": False,
                "estado": "error",
                 "mensajeError": "Entrada inválida. Por favor, ingrese un número entero para la edad."
        }
    
#Ahora armamos un main para probar las funciones
def main():

    #agregamos una lista vacia donde guardaremos los datos
    edades = []

    print("Ingrese las edades de las personas que quiera guardar.")
    print(f"Para finalizar el ingreso, ingrese '{CORTE}'.")

    #metemos todo en un bucle para permitir multiples ingresos
    while True:
        """
        #pedimos el nombre al usuario usando la funcion generica
        nombre = PedirDato("Por favor, ingrese su nombre: ", ValidarNombre)
        """
        #pedimos la edad al usuario usando la funcion generica
        edad = PedirDato("Por favor, ingrese las edades que quiera guardar: ", ValidarEdad)

        if edad["estado"] == "corte":
            print("Ingreso finalizado.")
            break

        elif edad["estado"] == "error":
            print(edad["mensajeError"])
            continue
        
        elif edad["estado"] == "ok":
            #agregamos las edades validas a la lista
            edades.append(edad["valor"])


    """"
    #mostramos los datos ingresados
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}") 
    """
    #Imprimimos todas las edades ingresadas
    print("Edades ingresadas:")
    for e in edades:
        print(f"- {e} años")

    #Mostramos la cantidad de edades ingresadas
    # Procesamiento de la lista (6.4.1)
    if len(edades) == 0:
        print("La lista está vacía.")
    else:
        print(f"Cantidad de edades ingresadas: {len(edades)}")
        print(f"Edad mínima registrada: {min(edades)}")
        print(f"Edad máxima registrada: {max(edades)}")
        #Se calcula el promedio de edades
        promedio = sum(edades) / len(edades)
        print(f"Promedio de edades: {promedio:.2f}")




#llamamos al main
if __name__ == "__main__":
    main()