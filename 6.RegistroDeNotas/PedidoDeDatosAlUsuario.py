def PedirEdadUsuario():
    while True:
        try:
            edad = int((input("Por favor, ingrese su edad: ")))
            if edad < 0:
                print("La edad no puede ser negativa. Intente nuevamente.")
            else:
                return edad
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la edad.")


