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

Se solicita crear un programa llamado ```validador.py``` el cual permite validar si un valor se encuentra incluido en un conjunto de opciones.
● Se pide crear la función ```validate()```, la cual debe aceptar como argumentos una lista de opciones y una elección.
● En caso de que no se ingrese una opción dentro del conjunto, la aplicación debe mostrar: 'Opción no válida, ingrese una de las opciones válidas: ' y solicitar el valor hasta que se ingrese uno válido.
● La función debe retornar la opción ingresada.

## 2. level.py

Crear un programa llamado level.py que incluya la función choose_level() que permite escoger el nivel de dificultad de la pregunta a realizar. Esa función debe aceptar como argumentos el número de la pregunta, y la cantidad de preguntas por nivel que puede ser 1, 2 o 3.
El funcionamiento debe ser el siguiente:
● Si se eligen 2 preguntas por nivel: Las preguntas n°1 y n°2 deben ser de nivel de dificultad básicas, las preguntas n°3 y n°4 de nivel intermedio y las preguntas n°5 y n°6 avanzadas.
● En cambio, si se escogen 3 preguntas por nivel, la 1,2 y 3 deben ser básicas,  4,5,6 intermedias y 7, 8 y 9 avanzadas.
● La función debe retornar el nivel escogido.

## 3. shuffle.py
Crear un programa llamado ```shuffle.py``` que contenga la función ```shuffle_alt()```. Esta función debe tomar como argumento una pregunta desde el archivo
```preguntas.py``` (con un nivel y una pregunta definida) y mezclar las alternativas. La función debe retornar las alternativas mezcladas. 

## 4. question.py
Crear un programa llamado question.py que permita escoger una pregunta que no se haya hecho durante la ejecución del programa dependiendo del nivel de dificultad.
Para ello:
● Cree una función llamada ```choose_q()``` que tome como único argumento la dificultad de la pregunta.
● La función debe tomar las preguntas del archivo ```preguntas.py``` de acuerdo a la dificultad escogida.
● La función debe escoger una pregunta de las opciones disponibles y eliminar dicha opción para no volverla a escoger.
● La función debe retornar dos elementos separados, el primero debe ser el enunciado escogido y el segundo las alternativas mezcladas de acuerdo a la tarea anterior.

## 5. print_preguntas.py
Crear un programa llamado ```print_preguntas.py```, el cual permitirá mostrar en la app las preguntas de acuerdo a un formato:
● El programa debe contener la función ```print_pregunta()``` que tome como argumentos un enunciado y sus alternativas, y que les aplique formato. Esta función no debe retornar ningún objeto, sólo imprimir en pantalla.
● El formato a utilizar es imprimir el enunciado, seguido de un salto de línea. Luego cada alternativa irá acompañada una letra asociada, una por cada línea de la siguiente manera:
○ A. Alternativa 1
○ B. Alternativa 2
○ C. Alternativa 3
○ D. Alternativa 4

## 6. verify.py
Crear un programa llamado ```verify.py```, cuya función es verificar si la respuesta entregada por el usuario es correcta. El programa debe contener la función ```verificar()``` que toma como argumentos las alternativas y la elección.
En el caso que la respuesta sea correcta debe imprimir en pantalla 'Respuesta Correcta' y retornar sólo el valor True, en caso contrario debe imprimir en pantalla 'Respuesta Incorrecta' y retornar sólo el valor False.

## 7. main.py
Este esqueleto ya incluye mensajes en el caso de acertar a una pregunta, de responder correctamente todas las preguntas o en caso de equivocarse, además de la lógica de pasar preguntas una a una. El objetivo de esta tarea es poder incluir todas las funcionalidades desarrolladas anteriormente y completar las siguientes tareas:
● Agregar un validador de opcion (el cual determina el inicio del programa o no). En caso de escoger la opción 0 entonces, agregar el mensaje 'Nos vemos pronto!' y finalizar el programa.
● Agregar un validador al número de preguntas por nivel.
● Escoger el nivel de la pregunta dependiendo del contador n_pregunta y el número de preguntas por nivel.
● Escoger el enunciado y las alternativas dependiendo del nivel según corresponda.
● Imprimir enunciado y sus alternativas en pantalla.
● Validar la respuesta entregada
● Verificar si la respuesta es correcta o no.
● Validar los valores si desea continuar o no.

**Uso**

Para ejecutar el archivo, utiliza el siguiente comando en la terminal:
```
python main.py
```
