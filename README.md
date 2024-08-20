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

**Uso**

Para ejecutar el archivo, utiliza el siguiente comando en la terminal:
```
python main.py
```
