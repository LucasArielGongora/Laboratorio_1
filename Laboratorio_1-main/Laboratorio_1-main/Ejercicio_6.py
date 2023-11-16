# Ejercicio 6:
# Utilizar For
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar el mayor.

numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

mayor_numero = numeros[0]
for indice in range(len(numeros)):
    if numeros[indice]> mayor_numero:
        mayor_numero= numeros[indice]
print(mayor_numero)

# mayor_numero = None

# for numero in numeros:
#     if mayor_numero == None or numero > mayor_numero:
#         mayor_numero = numero

# print(f"El numero mas alto de la lista es: {mayor_numero}") 
