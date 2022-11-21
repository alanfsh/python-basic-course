# CONDICIONALES

# edad = int(input("Escribe tu edad: "))
# if edad > 17:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")

numero = int(input("Escribe un número: "))
if numero > 0:
    print("Es positivo")
elif numero < 0: # else if --> contraccion
    print("Es negativo")
else:
    print("Es neutro")