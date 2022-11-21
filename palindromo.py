# Programa para verificar si una frase o palabra es un palindromo
def palindromo(palabra):
    palabra = palabra.replace(' ', '') # Reemplazar espacios por nada
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]  # Slices, invierte la palabra cadena[inicio:fin:paso], -1 indica que la recorre al reves
    if palabra == palabra_invertida:
        return True
    else:
        return False
# DEJAR DOS LINEAS ENTRE FUNCIONES ES BUENA PRACTICA

def run():
    palabra = input('Escribe una palabra o frase: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

if __name__ == '__main__': # Entry point, BUENA PRACTICA PARA QUE SE EJECUTE EL PROGRAMA
    run()
