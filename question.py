import preguntas as p
import random
from shuffle import shuffle_alt

"""
Este módulo permite seleccionar preguntas de una trivia basada en la dificultad y 
mezclar sus alternativas para evitar la repetición de preguntas dentro de una sesión de juego.

Módulos Importados:
    - preguntas (import as p): Contiene el banco de preguntas organizadas por niveles de dificultad.
    - random: Módulo estándar de Python para operaciones aleatorias.
    - shuffle_alt (from shuffle): Función personalizada para mezclar las alternativas de las preguntas.

Variables Globales:
    - opciones (dict): Un diccionario que contiene listas de índices para cada nivel de dificultad 
    ('basicas', 'intermedias', 'avanzadas'), utilizados para seleccionar preguntas sin repetición.

"""
# Opciones dadas para escoger.
###############################################
opciones = {"basicas": [1, 2, 3], "intermedias": [1, 2, 3], "avanzadas": [1, 2, 3]}
###############################################


def choose_q(dificultad):
    """
    - choose_q(dificultad):
        Selecciona una pregunta de la dificultad especificada, mezcla sus alternativas y devuelve
        el enunciado junto con las alternativas mezcladas.
        Args:
            dificultad (str): El nivel de dificultad de la pregunta a seleccionar ('basicas',
                            'intermedias', 'avanzadas').

        Returns:
            tuple: Una tupla que contiene:
                - enunciado (str): El enunciado de la pregunta seleccionada.
                - alternativas (list): Una lista de alternativas mezcladas.

        La función elimina la pregunta seleccionada de la lista global `opciones` para evitar
        que se repita durante la misma sesión.
    """
    # escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]

    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)

    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f"pregunta_{n_elegido}"]
    alternativas = shuffle_alt(pregunta)

    return pregunta["enunciado"], alternativas


if __name__ == "__main__":

    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q("basicas")
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")

    pregunta, alternativas = choose_q("basicas")
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")

    pregunta, alternativas = choose_q("basicas")
    print(f"El enunciado es: {pregunta}")
    print(f"Las alternativas son: {alternativas}")
