# Prueba Fundamentos de programación en Python
Aquí se expone el desarrollo de la prueba correspondiente al módulo Fundamentos de programación en Python

## Descripción
La aplicación de trivia permite a los jugadores responder preguntas de distintos niveles de dificultad: Básico, Intermedio y Avanzado. El jugador puede elegir el número de preguntas a responder por cada nivel, y las preguntas y sus alternativas se presentan en orden aleatorio para evitar patrones repetitivos.

## Estructura del Proyecto
El proyecto está dividido en varios módulos, cada uno cumpliendo una funcionalidad específica:

- **validador.py**: Valida si una opción ingresada es válida dentro de un conjunto de opciones.
- **level.py**: Permite al usuario elegir el nivel de dificultad de las preguntas.
- **shuffle.py**: Mezcla las alternativas de una pregunta de forma aleatoria.
- **question.py**: Selecciona una pregunta aleatoria de un nivel específico, asegurando que no se repita durante la ejecución.
- **print_preguntas.py**: Imprime las preguntas y sus alternativas en un formato adecuado.
- **verify.py**: Verifica si la respuesta seleccionada por el usuario es correcta.
- **main.py**: Esqueleto del programa que integra todas las funcionalidades y gestiona la lógica de la trivia.

## 1. validador.py
Se solicita crear un programa llamado ```validador.py``` el cual permite validar si un valor se encuentra incluido en un conjunto de opciones. Además, debe tener los siguientes requerimientos:
● La función ```validate()```, la cual debe aceptar como argumentos una lista de opciones y una elección.
● En caso de que no se ingrese una opción dentro del conjunto, la aplicación debe mostrar: 'Opción no válida, ingrese una de las opciones válidas: ' y solicitar el valor hasta que se ingrese uno válido.
● La función debe retornar la opción ingresada.

```
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
```
Importante mencionar que la utilización del operador ```not in``` nos permite determinar si un elemento no es parte de una lista.

## 2. level.py
Se crea el programa ```level.py```, el cual incluye la función ```choose_level()``` que permite escoger el nivel de dificultad de la pregunta a realizar. Esa función debe aceptar como argumentos el número de la pregunta, y la cantidad de preguntas por nivel que puede ser 1, 2 o 3.
El funcionamiento debe ser el siguiente:
● Si se eligen 2 preguntas por nivel: Las preguntas n°1 y n°2 deben ser de nivel de dificultad básicas, las preguntas n°3 y n°4 de nivel intermedio y las preguntas n°5 y n°6 avanzadas.
● En cambio, si se escogen 3 preguntas por nivel, la 1,2 y 3 deben ser básicas,  4,5,6 intermedias y 7, 8 y 9 avanzadas.
● La función debe retornar el nivel escogido. Es decir, el nivel de dificultad correspondiente a la pregunta, que pueden ser 'basicas',
        'intermedias', o 'avanzadas'.

```
def choose_level(n_pregunta, p_level):
    if n_pregunta <= p_level:
        level = "basicas"
    elif n_pregunta <= 2 * p_level:
        level = "intermedias"
    else:
        level = "avanzadas"

    return level
```

## 3. shuffle.py
Crear un programa llamado ```shuffle.py``` que contenga la función ```shuffle_alt()```. Esta función debe tomar como argumento una pregunta desde el archivo ```preguntas.py``` (con un nivel y una pregunta definida) y mezclar las alternativas. La función debe retornar las alternativas mezcladas. En palabras más sencillas, este módulo proporciona una función para mezclar las alternativas de respuesta de una pregunta de una trivia, asegurando que las alternativas aparezcan en un orden aleatorio cada vez que se presenta la pregunta.

```
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
    random.shuffle(pregunta["alternativas"])
    return pregunta["alternativas"]
```

## 4. question.py
El módulo ```question.py``` permite seleccionar preguntas de una trivia basada en la dificultad y mezclar sus alternativas para evitar la repetición de preguntas dentro de una sesión de juego. Para ello:
● Se crea la función ```choose_q()``` que toma como único argumento la dificultad de la pregunta, tomando las preguntas del archivo ```preguntas.py``` de acuerdo a la dificultad escogida. Asimismo, esta función escoge una pregunta de las opciones disponibles y después elimina dicha opción para no volverla a seleccionar. Finalmente, retorna dos elementos separados, el primero es el enunciado escogido y el segundo las alternativas mezcladas.

```
# Opciones dadas para escoger.
opciones = {"basicas": [1, 2, 3], "intermedias": [1, 2, 3], "avanzadas": [1, 2, 3]}

def choose_q(dificultad):
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
```

## 5. print_preguntas.py
Se crea el módulo ```print_preguntas.py```, el cual muyestra las preguntas de acuerdo a un formato:
● La función ```print_pregunta()``` toma como argumentos un enunciado y sus alternativas a través de un formato. Esta función no debe retornar ningún objeto, sólo imprimir en pantalla.
Cada pregunta está representada por un diccionario con las siguientes claves:
    - "enunciado": Una lista que contiene el enunciado de la pregunta.
    - "alternativas": Una lista de listas, donde cada sublista contiene una alternativa de respuesta y un valor (0 o 1) que indica si la alternativa es incorrecta (0) o correcta (1).

## 6. verify.py
La función del módulo ```verify.py``` es verificar si la respuesta entregada por el usuario es correcta. El programa debe contener la función ```verificar()``` que toma como argumentos las alternativas y la elección.
En el caso que la respuesta sea correcta debe imprimir en pantalla 'Respuesta Correcta' y retornar sólo el valor True, en caso contrario debe imprimir en pantalla 'Respuesta Incorrecta' y retornar sólo el valor False.

```
def verificar(alternativas, eleccion):
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
```

## 7. main.py
Este módulo implementa una trivia interactiva en la que los jugadores responden preguntas de distintos niveles de dificultad. El juego permite al usuario seleccionar el número de preguntas por nivel y continuar respondiendo mientras acierte las respuestas.
● Agregar un validador de opcion (el cual determina el inicio del programa o no). En caso de escoger la opción 0 entonces, agregar el mensaje 'Nos vemos pronto!' y finalizar el programa.

```
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
```
● Agregar un validador al número de preguntas por nivel.
● Escoger el nivel de la pregunta dependiendo del contador n_pregunta y el número de preguntas por nivel.
● Escoger el enunciado y las alternativas dependiendo del nivel según corresponda.
● Imprimir enunciado y sus alternativas en pantalla.
● Validar la respuesta entregada

```
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
```

● Verificar si la respuesta es correcta o no.
● Validar los valores si desea continuar o no.

```
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
```
#Uso del programa
Para ejecutar el archivo, utiliza el siguiente comando en la terminal:

```
python main.py
```

## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)

⌨️ con ❤️ por el Grupo 5 - G20 😊
