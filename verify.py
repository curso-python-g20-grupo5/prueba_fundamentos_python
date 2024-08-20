import preguntas as p

"""
Este módulo proporciona una función para verificar si la respuesta seleccionada por el usuario
en una trivia es correcta.
"""


def verificar(alternativas, eleccion):
    """
    - verificar(alternativas, eleccion):
        Compara la elección del usuario con la respuesta correcta para determinar si es correcta
        o incorrecta.

        Args:
            alternativas (list): Una lista de alternativas, donde cada alternativa es una lista que
                                contiene el texto de la alternativa (str) y un indicador (int) que
                                señala si la alternativa es correcta (1) o incorrecta (0).
            eleccion (str): La letra que representa la elección del usuario ('a', 'b', 'c', 'd').

        Returns:
            bool: Devuelve True si la respuesta es correcta, y False si es incorrecta.

        Raises:
            ValueError: Si la elección no está en la lista de letras válidas ('a', 'b', 'c', 'd').
    """
    # Convertir la letra de elección a índice
    letras = ["a", "b", "c", "d"]
    if eleccion not in letras:
        raise ValueError("Elección no válida. Debe ser 'a', 'b', 'c', o 'd'.")
    indice = letras.index(eleccion)

    # Verificar si la alternativa seleccionada es correcta
    correcto = alternativas[indice][1] == 1

    if correcto:
        print("Respuesta Correcta")
    else:
        print("Respuesta Incorrecta")

    return correcto


if __name__ == "__main__":

    from print_preguntas import print_pregunta

    # Ejemplo de pregunta
    pregunta = p.pool_preguntas["basicas"]["pregunta_2"]

    # Imprimir la pregunta y sus alternativas
    print_pregunta(pregunta["enunciado"], pregunta["alternativas"])

    # Solicitar respuesta al usuario
    respuesta = input("Escoja la alternativa correcta (a, b, c, d):\n> ").lower()

    # Verificar la respuesta
    verificar(pregunta["alternativas"], respuesta)
