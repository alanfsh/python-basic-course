import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['#', '$', '%', '&', '!', '?', '¿', 'ñ']

    caracteres = mayusculas + minusculas + numeros + simbolos # Sumando las listas en una sola

    contrasena = []

    for i in range(15): # Para generar la contraseña de 15 caracteres
        caracter_random = random.choice(caracteres) # Selecciona un item random de la lista caracteres
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena) # Convierte una lista a un String
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)
    

if __name__ == '__main__':
    run()