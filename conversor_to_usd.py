#Conversor de monedas MXN, COL, ARG --> USD
def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+ dolares +" dolares")

menu = """
Bienvenido al conversor de monedas 💰
1. Pesos mexicanos MXN
2. Pesos colombianos COL
3. Pesos argentinos ARG

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos", 20.25)
elif opcion == 2:
    conversor("colombianos", 3783.63)
elif opcion == 3:
    conversor("argentinos", 114.39)
else:
    print("Ingresa una opción valida")