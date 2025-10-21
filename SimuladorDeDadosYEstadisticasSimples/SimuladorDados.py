#Importamos las librerias necesarias

#La siguiente libreria nos permite generar numeros aleatorios
import random
#La siguiente libreria nos da herramientas para trabajar con colecciones de datos y estadisticas
from collections import Counter


#COMENZAMOS CON EL PROGRAMA

#Pedimos al usuario la cantidad de lanzamientos que desea realizar
try:
    cant_lanzamientos = int(input("Ingrese la cantidad de lanzamientos: "))
except ValueError: 
    print("Por favor, ingrese un numero entero valido.")
    exit()
if cant_lanzamientos <= 0:
    print("Por favor, ingrese un numero entero positivo.")
    exit()    

#Creamos una lista vacia para almacenar los resultados de los lanzamientos
dados_tirados = []

#Creamos la funcion de lanzamiento de dados
def lanzar_dados(cant_lanzamientos, dados_tirados):
    contador = 0
    while contador < cant_lanzamientos:
        dados_tirados.append(random.randint(1, 6))
        contador += 1

#Creamos la funcion que suma los resultados de los lanzamientos
def sumar_dados(dados_tirados):
    suma_parcial = 0
    for i in dados_tirados:
        suma_parcial += i
    return suma_parcial

#Creamos la funcion que calcula la media de los resultados
def promedio(cant_lanzamientos, dados_tirados):
    suma_total = sumar_dados(dados_tirados)
    promedio = suma_total / cant_lanzamientos
    print(f"El promedio de los dados tirados es de: {promedio}")

#Creamos la funcion que devuelve las estadisticas de los resultados
def estadisticas_dados(dados_tirados):
    print("El valor del dado mas repetido fue el siguiente:")
    print(Counter(dados_tirados).most_common()[0][0])

#Imprimimos la lista completa de los resultados
def imprimir_resultados(dados_tirados):
    print("Los resultados de los dados tirados son los siguientes:")
    print(dados_tirados)    

#Definimos la funcion principal que llama a las demas funciones
def main():
    #Llamamos a la funcion de lanzamiento de dados
    lanzar_dados(cant_lanzamientos, dados_tirados)

    #Llamamos a la funcion que devuelve la suma de los resultados
    suma_total = sumar_dados(dados_tirados)
    print(f"La suma total de los dados tirados es de: {suma_total}")

    #Llamamos a la funcion que devuelve el promedio de los resultados
    promedio(cant_lanzamientos, dados_tirados)

    #Llamamos a la funcion que devuelve el numero mas repetido de los dados tirados
    estadisticas_dados(dados_tirados)

    #Llamamos a la funcion que imprime la lista completa de los resultados
    imprimir_resultados(dados_tirados)

    #Devolvemos un mensaje de despedida
    print("Hasta la proxima!")

#Llamamos a la funcion principal
main()

#FIN DEL PROGRAMA