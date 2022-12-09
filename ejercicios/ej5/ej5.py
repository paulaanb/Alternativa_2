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
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
     
# This function receives cipher-text
# and key and returns the original
# text after decryption
def decryptRailFence(cipher, key):
 
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix to
    # distinguish filled spaces
    # from blank ones
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]
     
    # to find the direction
    dir_down = None
    row, col = 0, 0
     
    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        # place the marker
        rail[row][col] = '*'
        col += 1
         
        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
             
    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
 
# Driver code
if __name__ == "__main__":
    print(encryptRailFence("Ruben apruebame por favor", 2))
    print(encryptRailFence("No quiero ir a enero ", 3))
    print(encryptRailFence("Me vale con un 5", 3))
     
    # Now decryption of the
    # same cipher-text
    print(decryptRailFence("Rbnareaeprfvrue pubm o ao", 3))
    print(decryptRailFence("Nuo n oqir raeeo ei r", 2))
    print(decryptRailFence("Macuevl o n5 en ", 3))
 