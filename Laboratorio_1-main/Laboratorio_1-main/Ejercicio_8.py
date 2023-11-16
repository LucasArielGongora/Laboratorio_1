# Ejercicio 8:
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
# mostrar el número repetido

numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 3, 12, 48, 78, 29, 58]
# repetido = False

# for numero in numeros:
#     contador = 0
#     for numero_dos in numeros:
#         if numero == numero_dos:
#             contador += 1

#             if contador == 2:
#                 numero_repetido = numero
#                 repetido = True
#                 break
#     if repetido == True:
#         break

# print(f"el numero repetido es: {numero_repetido}")

repetidos = []

for indice in range(len(numeros)):
    for indice_dos in range(indice + 1, len(numeros)):
        if numeros[indice] == numeros[indice_dos] and numeros[indice] not in repetidos:
            repetidos.append(numeros[indice])

print(repetidos)

# 0 1 2 3 4 
# 0 hasta 4




