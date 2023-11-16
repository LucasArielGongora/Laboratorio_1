# Ejercicio 3:
# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

# contador = 0
# listaNumeros = []
# while contador < 5:
#     contador += 1
#     numero = (input("ingrese un numero: "))
#     numero = int(numero)
#     while numero == 0:
#         print ('no puede ser 0')
#         numero = (input("ingrese un numero: "))
#         numero = int(numero)

#     listaNumeros.append(numero)

# print(listaNumeros)

# numerosPares = 0
# numerosImpares = 0
# menorNumero = None
# mayorPar = None
# sumaPositivos = 0
# productoNegativos = 1
# flagPar = false

# for numero in listaNumeros:
#     if numero % 2 == 0 :
#        if mayorPar == None or numero > mayorPar:
#             mayorPar = numero
#             flagPar = True
#         numerosPares += 1
#     else:
#         numerosImpares += 1

#     if menorNumero == None or numero < menorNumero:
#         menorNumero = numero

#     if numero > 0:
#         sumaPositivos+= numero

#     if numero<0:
#         productoNegativos *= numero

# print(-------------------------------------------------------------------------)
# print(f"A- Hay {numerosPares} numeros pares y {numerosImpares} numeros impares.")
# print(f"B- El menor numero ingresado es: {menorNumero}")
#if flagPar == True
#    print(f"C- El mayor numero par es: {mayorPar}")
#else:
#   print('No hay números pares.')
# print(f"D- La suma de los positivos es: {sumaPositivos}")
# print(f"E- El producto de los negativos es: {productoNegativos}")
