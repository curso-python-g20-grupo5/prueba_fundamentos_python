import preguntas as p


def print_pregunta(enunciado, alternativas):
    """
    Este módulo proporciona una función para imprimir preguntas y sus alternativas de respuesta
    en un formato claro y estructurado.

    Funciones:
        - print_pregunta(enunciado, alternativas):
            Imprime el enunciado de una pregunta y sus alternativas, asignando automáticamente
            una letra (A, B, C, D) a cada alternativa.

        Args:
            enunciado (str): El enunciado de la pregunta.
            alternativas (list): Una lista de listas, donde cada sublista contiene:
                                - El texto de la alternativa (str).
                                - Un indicador (int) que señala si la alternativa es correcta (1) o incorrecta (0).

        Ejemplo de Uso:
            La función `print_pregunta` se puede utilizar para mostrar preguntas formateadas en un
            juego de trivia. Al ejecutarse, se imprime el enunciado de la pregunta seguido de las
            alternativas con su respectiva letra asociada.

    """

    # Imprimir el enunciado de la pregunta
    print(enunciado)
    print()  # Salto de línea


    # Creamos una lista que contiene letras. Estas se serán asociadas a cada alternativa.
    letras = ["A", "B", "C", "D"]

    # Iterar la lista que creamos a cada alternativa.
    for i, (texto, _) in enumerate(alternativas):
        if i < len(letras):  # Asegurarse de que no se exceda el número de letras
            print(f"{letras[i]}. {texto}")


if __name__ == "__main__":
    """
    if __name__ == '__main__':
        pregunta = p.pool_preguntas['basicas']['pregunta_1']
        print_pregunta(pregunta['enunciado'], pregunta['alternativas'])

        # Ejemplo de salida:
        # ¿Cómo se declara una variable en Python?
        # A. var nombre = valor
        # B. nombre := valor
        # C. nombre = valor
        # D. let nombre = valor
    """
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas["basicas"]["pregunta_1"]
    print_pregunta(pregunta["enunciado"], pregunta["alternativas"])

    # Enunciado básico 1
    # A. 1
    # B. 3
    # C. 5
    # D. 2
