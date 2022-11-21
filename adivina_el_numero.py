# Juego para adivinar un numero entre 1 y 100
import random  # aleatoriedad

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    vidas = 10
    sin_vidas = False
    while numero_elegido != numero_aleatorio:
        vidas -= 1
        if vidas == 0:
            sin_vidas = True
            break
        print('Vidas: '+ str(vidas))
        if numero_elegido < numero_aleatorio:
            print('Elige un número más grande')
        elif numero_elegido > numero_aleatorio:
            print('Elige un número más pequeño')
        numero_elegido = int(input('Intenta otra vez: '))
    if sin_vidas:
        print('No te quedan vidas!!')
        print('--------------------- GAME OVER --------------------------')
    else:
        print('------------------- ¡¡¡GANASTE!!! -------------------------')


if __name__ == '__main__':
    run()