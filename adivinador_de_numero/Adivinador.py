# Importamos la libreria de math para usar funciones matematicas

import random

# Definimos la funcion principal
def main():
    # Definimos las variables

    contador = 0
    encontro = False

    # Generamos un numero aleatorio entre 1 y 100

    numero_random = random.randint(1, 100) 
    
    #Imprimimos mensajes de bienvenida
    print("Bienvenido al juego de adivinanza!")
    print("El numero ha sido elegido")

    # Pedimos al usuario que ingrese su primer intento

    numero_elegido = int (input("Ingrese su primer intento: "))
    
    # Comenzamos el ciclo de adivinanza
    while encontro==False:

        # Aumentamos el contador de intentos
        contador = contador + 1

        # Opcion True del bucle
        if (numero_elegido == numero_random):
            encontro = True 
            print("Felicidades! Adivinaste el numero en " + str(contador) + " intentos!")

        # Opcion de si el numero elegido es MENOR al numero aleatorio
        elif (numero_elegido < numero_random):  
            numero_elegido = int (input("El numero es mayor. Intenta de nuevo: "))

        # Opcion de si el numero elegido es MAYOR al numero aleatorio   
        else:   
            numero_elegido = int (input("El numero es menor. Intenta de nuevo: "))      

#Ejecutamos la funcion principal
main()