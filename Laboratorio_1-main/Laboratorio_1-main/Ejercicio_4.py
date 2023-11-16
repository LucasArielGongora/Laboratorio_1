# Ejercicio 4:
# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
# distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
# ser soltero.'

# while True:

#     while True:
#         try:
#             edad = int(input("Por favor, ingrese su edad: "))
#             if edad > 18:
#                 break
#             else:
#                 print("La edad debe ser mayor de 18.")
#         except ValueError:
#             print("Ingrese una edad válida (número entero).")

#     while True:
#         try:
#             estadoCivil = input("Ingrese estado civil: C/S: ")
#             estadoCivil.upper()
#             if estadoCivil == "C" or estadoCivil == "S":
#                 break
#         except ValueError:
#             print("Ingrese un estado valido C o S")
#         break

#     while estadoCivil != "C" and estadoCivil != "S":
#         print('Estado invalido')
#         estadoCivil = input("Ingrese estado civil: C/S: ")
#     break 

# if (edad<18 and estadoCivil != 'S'):
#     print ("Es muy pequeño para no ser soltero.")
# else:
#     print("Es menor y es soltero.")
