from verify import verificar
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

"""
    Este módulo implementa una trivia interactiva en la que los jugadores responden preguntas
    de distintos niveles de dificultad. El juego permite al usuario seleccionar el número
    de preguntas por nivel y continuar respondiendo mientras acierte las respuestas.

Módulos Importados:
    - verificar (from verify): Verifica si la respuesta del jugador es correcta.
    - choose_q (from question): Selecciona una pregunta y sus alternativas según el nivel.
    - print_pregunta (from print_preguntas): Muestra la pregunta y sus alternativas.
    - choose_level (from level): Determina el nivel de la pregunta según su número.
    - validate (from validador): Valida la entrada del usuario.
    - time, os, sys: Módulos estándar de Python para la gestión del tiempo, sistema operativo y
    funciones del sistema.
"""
# Valores iniciales
op_sys = "cls" if sys.platform == "win32" else "clear"


def limpiar_pantalla():
    """
    - limpiar_pantalla(): Limpia la pantalla de la consola según el sistema operativo.
    """
    os.system(op_sys)


def mostrar_bienvenida():
    """
    - mostrar_bienvenida(): Muestra un mensaje de bienvenida al iniciar el juego.
    """
    print("Bienvenido a la Trivia")


def mostrar_menu():
    """
    - mostrar_menu(): Muestra el menú principal y valida la opción elegida por el usuario.
    """
    opcion = input(
        """Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
    > """
    )
    return validate(["0", "1"], opcion)


def manejar_salida():
    """
    - manejar_salida(): Muestra un mensaje de despedida y cierra el juego.
    """
    print("Nos vemos pronto!")
    time.sleep(2)
    limpiar_pantalla()
    sys.exit()


def seleccionar_nivel_preguntas():
    """_summary_
    - seleccionar_nivel_preguntas(): Permite al usuario seleccionar cuántas preguntas por nivel
    responderá.
    """
    p_level_input = input("¿Cuántas preguntas por nivel? (Máximo 3): ")
    return int(validate(["1", "2", "3"], p_level_input))


def procesar_pregunta(n_pregunta, p_level):
    """
    - procesar_pregunta(n_pregunta, p_level): Procesa una pregunta, muestra las alternativas,
    y verifica las respuestas.
    """
    nivel = choose_level(n_pregunta, p_level)
    print(f"Pregunta {n_pregunta}:")

    enunciado, alternativas = choose_q(nivel)
    print_pregunta(enunciado, alternativas)

    respuesta = input("Escoja la alternativa correcta (a, b, c, d):\n> ").lower()
    respuesta = validate(["a", "b", "c", "d"], respuesta)

    return verificar(alternativas, respuesta)


def manejar_respuesta_correcta(n_pregunta, p_level):
    """
    - manejar_respuesta_correcta(n_pregunta, p_level): Maneja la secuencia de juego cuando la
    respuesta es correcta y pregunta si el jugador desea continuar.
    """
    if n_pregunta < 3 * p_level:
        print("Muy bien, sigue así!")
        continuar = input("Desea continuar? [y/n]: ").lower()
        return validate(["y", "n"], continuar)
    else:
        print(
            f"Felicitaciones, has respondido {3 * p_level} preguntas correctas.\nHas ganado la Trivia.\nGracias por jugar, hasta luego!!!"
        )
        time.sleep(3)
        limpiar_pantalla()
        sys.exit()


def manejar_respuesta_incorrecta(n_pregunta):
    """_
    - manejar_respuesta_incorrecta(n_pregunta): Maneja la secuencia de juego cuando la respuesta
    es incorrecta.
    """
    print(
        f"Lo siento, conseguiste {n_pregunta - 1} respuestas correctas.\nSigue participando!!"
    )
    time.sleep(3)
    sys.exit()


def main():
    """
    - main(): Función principal que controla el flujo del juego, desde la bienvenida hasta la
    finalización.
    """
    limpiar_pantalla()
    mostrar_bienvenida()

    opcion = mostrar_menu()

    if opcion == "0":
        manejar_salida()

    # Configuración inicial del juego
    n_pregunta = 0
    continuar = "y"
    correcto = True
    p_level = 10

    while correcto and n_pregunta < 3 * p_level:

        if n_pregunta == 0:
            p_level = seleccionar_nivel_preguntas()

        if continuar == "y":
            n_pregunta += 1
            correcto = procesar_pregunta(n_pregunta, p_level)

            if correcto:
                continuar = manejar_respuesta_correcta(n_pregunta, p_level)
                limpiar_pantalla()
            else:
                manejar_respuesta_incorrecta(n_pregunta)
        else:
            print("Nos vemos la próxima vez, sigue practicando")
            time.sleep(3)
            sys.exit()


if __name__ == "__main__":
    main()
