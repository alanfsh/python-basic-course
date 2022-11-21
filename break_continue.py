def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue            # continue continua el ciclo haste este punto
    #     print(contador)
    # for i in range(0, 10000):
    #     print(i)
    #     if i == 5678:
    #         break                 # break rompe el ciclo y se sale
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra.lower() == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()