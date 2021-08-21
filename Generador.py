import random

"""
    La función choice(secuencia) elige un valor al azar en un conjunto de elementos. 
    Cualquier tipo de datos enumerable (tupla, lista, cadena, range) 
    puede utilizarse como conjunto de elementos.

    La función join convierte una lista en una cadena formada 
    por los elementos de la lista separados por comas.

"""

def generarContra():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS
    contrasena = []

    for i in range(16):
        random_caracter = random.choice(caracteres)
        contrasena.append(random_caracter)

    contrasena = "".join(contrasena)
    return contrasena 

def main():
    contrasena = generarContra()

    print("Tu nueva contraseña es: " + contrasena)


if __name__ == '__main__':
    main()
    