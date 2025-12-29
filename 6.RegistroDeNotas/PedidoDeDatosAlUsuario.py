#Hacemos una funcion que pide al usuario su edad como para practicar, lo devuelve a la funcion y ya se puede utilizar

#Creamos constantes para los minimos y maximos de la edad
EDAD_MINIMA = 1
EDAD_MAXIMA = 120

def PedirEdadUsuario():
    #creamos el bucle para que siga pidiendo la edad hasta que se ingrese un valor valido
    while True:
        #encerramos todo en un bloque try-except para manejar errores de conversion
        try:
            #convertimos la entrada a entero
            edad = int((input("Por favor, ingrese su edad: ")))
            #chequeamos que la edad no sea negativa
            if edad < 0:
                print("La edad no puede ser negativa. Intente nuevamente.")
            elif edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
                print(f"La edad debe estar entre {EDAD_MINIMA} y {EDAD_MAXIMA}. Intente nuevamente.")
            else:
                return edad
        #manejamos el error de conversion
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la edad.")


