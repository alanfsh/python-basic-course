def run():
    diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(diccionario['llave1'])
    paises_poblacion = {
        'Mexico': 120000000,
        'Brasil': 210000000,
        'Colombia': 50000000,
    }

    # print(paises_poblacion['Basil'])
    # for pais in paises_poblacion.keys(): # .keys() devuelve las llaves
    #     print(pais)
    # for pais in paises_poblacion.values(): # .values() devuelve los valores
    #     print(pais)
    for pais, poblacion in paises_poblacion.items(): # .items() devuelve llave: valor en dos variables
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')



if __name__ == '__main__':
    run()