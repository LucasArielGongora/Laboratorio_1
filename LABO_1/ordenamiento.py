import time

lista_numeros = [3, 4, 5, 6, 7, 8, 9, 2, 1]

# for i in range(len(lista_numeros) - 1):
#     for j in range(i + 1, len(lista_numeros)):
#         if lista_numeros[i] > lista_numeros[j]:
#             aux = lista_numeros[i]
#             lista_numeros[i] = lista_numeros[j]
#             lista_numeros[j] = aux

# print(lista_numeros)

for i in range(1, len(lista_numeros)):
    key = lista_numeros[i]
    j = i - 1
    while j >= 0 and key < lista_numeros[j]:
        lista_numeros[j + 1] = lista_numeros[j]
        j -= 1
    lista_numeros[j + 1] = key

print(lista_numeros)

# lista = []

# for i in range(0,20000):
#     if i%2 == 0:
#         lista.append(i+5)
#     else:
#         lista.append(i*3)

# unaLista= lista
# comienzo_tiempo = time.time()
# def ordenamientoBurbujaCorto(unaLista):
#     intercambios = True
#     numPasada = len(unaLista)-1

#     while numPasada > 0 and intercambios:
#        intercambios = False

#        for i in range(numPasada):
#            if unaLista[i]>unaLista[i+1]:
#                intercambios = True
#                temp = unaLista[i]
#                unaLista[i] = unaLista[i+1]
#                unaLista[i+1] = temp
#        numPasada = numPasada-1

# ordenamientoBurbujaCorto(unaLista)
# fin_tiempo = time.time()
# total = fin_tiempo - comienzo_tiempo
# print(unaLista)
# print(total)

#ORDENAMIENTO2
# import time 
# lista = []

# for i in range(0,20000):
#     if i%2 == 0:
#         lista.append(i+5)
#     else:
#         lista.append(i*3)
        
# lista_numeros = lista

# comienzo_tiempo = time.time()
# for i in range(len(lista_numeros)-1):
    
#     #j = i + 1
#     for j in range(i+1, len(lista_numeros)):
#         if lista_numeros[i] > lista_numeros[j]:
#             #-          8
#             aux = lista_numeros[i]
#             #8          8
#             lista_numeros[i] = lista_numeros[j]
#             #5                      5
#             lista_numeros[j] = aux
#             #8                  8

# fin_tiempo = time.time()
    
# total = fin_tiempo - comienzo_tiempo

# print(lista_numeros)
# print(total)
