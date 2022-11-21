dolares = input("¿Cuántos dolares tienes?: ")
dolares = float(dolares)
valor_peso_mxn = 0.0494
pesos_mxn = dolares / valor_peso_mxn
pesos_mxn = round(pesos_mxn, 2)
pesos_mxn = str(pesos_mxn)
print("Tienes $"+ pesos_mxn + " pesos mexicanos") 