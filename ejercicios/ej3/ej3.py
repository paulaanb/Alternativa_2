# Función que cuenta el número de patrones posibles a partir del punto inicial especificado
# y con la longitud especificada entre 4 y 9 puntos/puntos
def count_patterns(start, length, pattern):
 # Estructura de datos para almacenar los puntos visitados en el patrón actual
    visited = []

 # Lista de patrones encontrados
    patterns = []

 # Función recursiva que busca patrones posibles en la matriz de patrones
    def search_patterns(point, visited):
   # Agrega el punto al patrón actual
        visited.append(point)

    # Si el patrón actual es válido (es decir, tiene la longitud especificada)
    if len(visited) == length:
        # Agrega el patrón a la lista de patrones encontrados
        patterns.append(visited)

        # Vuelve al último punto agregado al patrón y continúa buscando más patrones
        return visited.pop()

    # Si el patrón actual no es válido (es decir, no tiene la longitud especificada),
    # entonces busca puntos válidos para continuar el patrón
    else:
        # Obtiene la fila y columna del punto en la matriz de patrones
        row, col = divmod(point - 1, 3)

        # Lista de puntos válidos para continuar el patrón
        valid_points = []

        # Revisa los puntos adyacentes al punto actual en la matriz de patrones
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]:
        # Si el punto adyacente está en la matriz de patrones y no ha sido visitado
            if 0 <= r < 3 and 0 <= c < 3 and pattern[r][c] not in visited:
            # Agrega el punto a la lista de puntos válidos
                valid_points.append(pattern[r][c])

        # Si hay puntos válidos para continuar el patrón, entonces busca patrones en cada punto válido
        if valid_points:
            for point in valid_points:
            # Busca patrones en el punto válido
                search_patterns(point, visited)

        # Si no hay puntos válidos para continuar el patrón, entonces vuelve al último punto agregado
        # al patrón y continúa buscando más patrones
        else:
            visited.pop()

    # Inicia la búsqueda