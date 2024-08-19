import preguntas as p
import random

"""
Este módulo proporciona una función para mezclar las alternativas de respuesta de una pregunta
de una trivia, asegurando que las alternativas aparezcan en un orden aleatorio cada vez que
se presenta la pregunta.

Módulos Importados:
    - preguntas (import as p): Contiene el banco de preguntas organizadas por niveles de dificultad.
    - random: Módulo estándar de Python para realizar operaciones aleatorias, como mezclar listas.
"""


def shuffle_alt(pregunta):
    """
    - shuffle_alt(pregunta):
        Mezcla las alternativas de una pregunta, alterando el orden en el que se presentan.

        Args:
            pregunta (dict): Un diccionario que representa una pregunta, donde la clave 'alternativas'
                            es una lista de alternativas de respuesta.

        Returns:
            list: Una lista de alternativas mezcladas en un orden aleatorio.
    """
    # Mezclar las alternativas de la pregunta
    #######################################################################
    random.shuffle(pregunta["alternativas"])
    #######################################################################
    return pregunta["alternativas"]


if __name__ == "__main__":
    """
    if __name__ == '__main__':
        print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']))
        # Ejemplo de salida:
        # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
    """
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas["basicas"]["pregunta_1"]))
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
