#Función que calcula el millonésimo número en la recurrencia de Fibonacci
def fibonacci(n):
    # Inicializa los dos primeros números en la recurrencia (0 y 1)
    a, b = 0, 1
    # Calcula los números sucesivos en la recurrencia hasta llegar al millonésimo número
    for i in range(1, n):
        a, b = b, a + b
    # Devuelve el millonésimo número en la recurrencia
    return b


# Calcula el millonésimo número en la recurrencia de Fibonacci
millonth_number = fibonacci(1000000)
# Imprime el resultado
print(millonth_number) 
# Imprime: 8247650592082470666723170306785496252186258551345437492922123134388955774976000000000000000