"""
Esta función valida que la opción elegida por el usuario esté dentro de un conjunto de opciones válidas.
Si el usuario ingresa una opción no válida, se le pedirá que ingrese una opción correcta hasta que lo haga.

"""


def validate(opciones, eleccion):
    """
    - validate(opciones, eleccion):
        Comprueba si la elección del usuario está dentro de las opciones válidas. Si no lo está,
        solicita al usuario que ingrese una opción válida hasta que lo haga correctamente.

        Args:
            opciones (list): Una lista de opciones válidas que el usuario puede elegir.
            eleccion (str): La opción seleccionada por el usuario.

        Returns:
            str: La elección válida del usuario después de pasar la validación.
    """
    # Definir validación de eleccion
    while eleccion not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        eleccion = input("Ingresa una opción válida: ").lower()

    return eleccion


if __name__ == "__main__":
    """
    if __name__ == '__main__':
        eleccion = input('Ingresa una Opción: ').lower()
        numeros = ['0', '1']
        validate(numeros, eleccion)
    """

    eleccion = input("Ingresa una Opción: ").lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ["0", "1"]
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
