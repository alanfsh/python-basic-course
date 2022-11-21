# Un numero es primo si no es divisible entre los primeros numeros primos
def es_primo(numero):
    primeros_primos = (2, 3, 5, 7, 11)
    contador = 0
    for i in primeros_primos:
        if numero % i == 0:
            contador += 1
    if contador == 0 and numero != 1:
        return True
    else:
        return False

def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')
    
    

if __name__ == '__main__':
    run()