"""
Este módulo define un conjunto de preguntas categorizadas en diferentes niveles de dificultad
para ser utilizadas en una trivia de Python. Cada pregunta incluye un enunciado y varias 
alternativas de respuesta, donde una o más son correctas.

Diccionarios de Preguntas:
    - preguntas_basicas: Contiene preguntas de nivel básico sobre conceptos fundamentales 
    de Python.
    - preguntas_intermedias: Contiene preguntas de nivel intermedio que abordan temas como 
    métodos y estructuras de datos en Python.
    - preguntas_avanzadas: Contiene preguntas de nivel avanzado que cubren conceptos más 
    complejos como comprensiones de listas y el uso de `self` en clases.

Estructura de Cada Pregunta:
    Cada pregunta está representada por un diccionario con las siguientes claves:
        - "enunciado": Una lista que contiene el enunciado de la pregunta.
        - "alternativas": Una lista de listas, donde cada sublista contiene una alternativa
        de respuesta y un valor (0 o 1) que indica si la alternativa es incorrecta (0)
        o correcta (1).

Diccionario Global:
    - pool_preguntas: Un diccionario que organiza todas las preguntas por nivel de dificultad:
        - "basicas": Contiene preguntas básicas.
        - "intermedias": Contiene preguntas intermedias.
        - "avanzadas": Contiene preguntas avanzadas.

Ejemplo de Uso:
    Las preguntas pueden ser seleccionadas y utilizadas en una trivia para evaluar el 
    conocimiento del usuario en distintos niveles de dificultad.
"""

preguntas_basicas = {
    "pregunta_1": {
        "enunciado": ["¿Cómo se declara una variable en Python?"],
        "alternativas": [
            ["var nombre = valor", 0],
            ["nombre := valor", 0],
            ["nombre = valor", 1],
            ["let nombre = valor", 0],
        ],
    },
    "pregunta_2": {
        "enunciado": ['¿Qué tipo de datos es "123" en Python?'],
        "alternativas": [["Integer", 0], ["Float", 0], ["String", 1], ["List", 0]],
    },
    "pregunta_3": {
        "enunciado": ["¿Cómo se define una función en Python?"],
        "alternativas": [
            ["def funcion():", 1],
            ["function funcion[]:", 0],
            ["func funcion[]:", 0],
            ["define funcion():", 0],
        ],
    },
}

preguntas_intermedias = {
    "pregunta_1": {
        "enunciado": ["¿Qué hace el método `.append()` en una lista en Python?"],
        "alternativas": [
            ["Elimina un elemento de la lista", 0],
            ["Añade un elemento al final de la lista", 1],
            ["Ordena la lista", 0],
            ["Crea una nueva lista", 0],
        ],
    },
    "pregunta_2": {
        "enunciado": ["¿Qué es un diccionario en Python?"],
        "alternativas": [
            ["Una estructura de datos que almacena pares clave-valor", 1],
            ["Una lista ordenada de elementos", 0],
            ["Un tipo de variable de texto", 0],
            ["Una función especial de Python", 0],
        ],
    },
    "pregunta_3": {
        "enunciado": [
            "¿Cómo se accede al valor asociado a una clave en un diccionario?"
        ],
        "alternativas": [
            ["diccionario[clave]", 1],
            ["diccionario(clave)", 0],
            ["diccionario.get(clave)", 1],
            ["diccionario.key(clave)", 0],
        ],
    },
}

preguntas_avanzadas = {
    "pregunta_1": {
        "enunciado": ["¿Qué es una comprensión de listas en Python?"],
        "alternativas": [
            ["Un método para crear listas usando un bucle for", 1],
            ["Una forma de convertir listas en diccionarios", 0],
            ["Un tipo de función especial", 0],
            ["Una forma de ordenar listas", 0],
        ],
    },
    "pregunta_2": {
        "enunciado": ["¿Qué hace el operador `**` en Python?"],
        "alternativas": [
            ["Realiza una operación de potencia", 1],
            ["Multiplica dos números", 0],
            ["Divide dos números", 0],
            ["Calcula el módulo de una división", 0],
        ],
    },
    "pregunta_3": {
        "enunciado": ['¿Qué es el "self" en un método de una clase en Python?'],
        "alternativas": [
            ["Un parámetro que se refiere al objeto actual", 1],
            ["Una variable global en la clase", 0],
            ["Un tipo de método especial", 0],
            ["Una forma de inicializar una clase", 0],
        ],
    },
}

pool_preguntas = {
    "basicas": preguntas_basicas,
    "intermedias": preguntas_intermedias,
    "avanzadas": preguntas_avanzadas,
}
