# Funcion para encriptar un mensaje
def encryptRailFence(text, key):
 
# crear la matriz para cifrar
# clave de texto plano = filas ,
# longitud (texto) = columnas
# rellenando la matriz de carriles
# para distinguir llenos
# espacios de espacios en blanco
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]
     
    # para encontrar la direccion
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
         
        # Compruebe la dirección del flujo
        # invertir la dirección si acabamos de
        # llenó el carril superior o inferior
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # rellenar el alfabeto correspondiente
        rail[row][col] = text[i]
        col += 1
         
# encontrar la siguiente fila usando
# bandera de dirección
        if dir_down:
            row += 1
        else:
            row -= 1
# Ahora podemos construir el cifrado
    # utilizando la matriz de carriles
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
     
# Esta función recibe texto cifrado
# y tecla y devuelve el original
# texto después de descifrado
def decryptRailFence(cipher, key):
 
# crear la matriz para cifrar
    # clave de texto plano = filas ,
    # longitud (texto) = columnas
    # rellenando la matriz de carril a
    # distinguir los espacios llenos
    # De los en blanco
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]
     
    # para encontrar la direccion
    dir_down = None
    row, col = 0, 0
     
    # marcamos los lugares con '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        # lugar de la marca
        rail[row][col] = '*'
        col += 1
         
# Encontrar la siguiente fila
        # usando la bandera de dirección
        if dir_down:
            row += 1
        else:
            row -= 1
             
# Ahora podemos construir el
    # rellenar la matriz de carril
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
# ahora lee la matriz en
    # manera de construir en zig-zag
    # el texto resultante
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
   # Compruebe la dirección del flujo
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        #lugar de la marca
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
# encontrar la siguiente fila usando
        # bandera de dirección
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
 
# Codigo cifrar
if __name__ == "__main__":
    print(encryptRailFence("Ruben apruebame por favor", 2))
    print(encryptRailFence("No quiero ir a enero ", 3))
    print(encryptRailFence("Me vale con un 5", 3))
     
    # codigo descifrar
    print(decryptRailFence("Rbnareaeprfvrue pubm o ao", 3))
    print(decryptRailFence("Nuo n oqir raeeo ei r", 2))
    print(decryptRailFence("Macuevl o n5 en ", 3))
 