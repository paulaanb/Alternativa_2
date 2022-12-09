def expand(expression):
 # Extraer a, b y n de la expresión
    a, b, n = extract_values_from_expression(expression)
    # Inicializar la cadena resultante como una cadena vacía
    result = " "
    # Iterar sobre las potencias de x en el resultado expandido
    for i in range(n, -1, -1):
    # Calcular el coeficiente para el término actual
    

        coefficient = n * (n - 1) * ... * (n - i + 1) / i!
        

    # Añadir el término al resultado
        result += format_term(coefficient, a, i, b)
    return result
