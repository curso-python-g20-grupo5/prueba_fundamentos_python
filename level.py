def choose_level(n_pregunta, p_level):
    """
    Determina el nivel de dificultad de una pregunta basada en su número y un valor de referencia.

    Args:
        n_pregunta (int): Número de la pregunta actual.
        p_level (int): Valor de referencia para determinar el nivel de dificultad.

    Returns:
        str: El nivel de dificultad correspondiente a la pregunta, que pueden ser 'basicas',
        'intermedias', o 'avanzadas'.
    """
    if n_pregunta <= p_level:
        level = "basicas"
    elif n_pregunta <= 2 * p_level:
        level = "intermedias"
    else:
        level = "avanzadas"

    return level


if __name__ == "__main__":
    # Verificar resultados
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
