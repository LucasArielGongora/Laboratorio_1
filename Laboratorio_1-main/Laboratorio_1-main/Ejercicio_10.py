# Ejercicio 10:
# Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
# respectivas listas. Validar el ingreso de datos según su criterio.
# Datos:
# nombre, sexo (f/m), nota (validar).
# Una vez cargados los datos:
# Mostrar el nombre del hombre con nota más baja
# Mostrar el promedio de notas de las mujeres


nombres = []
generos = []
notas = []
notas_mujeres = []

menorNota = False
menor_nota_hombre = None

for i in range(5):

    while True:
        nombre = input("Ingrese nombre alumno:")
        if nombre.isalpha():
            nombres.append(nombre)
            break
        else:
            print ("El dato no es valido, debe contener solo letras.")

    while True:
        genero = input("Ingrese genero: F/M: ")
        genero = genero.upper()
        if genero == "F" or genero == "M":
            generos.append(genero)
            break
        else:
            print ("el dato no es valido. Intente nuevamente.")
            

    while True:
        try:
            nota=int(input("ingrese la nota: "))
            if  nota >= 0 and nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe ser entre 0 y 10. ")
        except ValueError:
            print("Ingreso invalido. intente nuevamente. ")

    print("--------------------------------")

for i in range(len(nombres)):
    if generos[i] == "M":
        if menor_nota_hombre is None or notas[i] < menor_nota_hombre:
            menor_nota_hombre = notas[i]
            hombre_nota_baja = nombres[i]

for i in range(len(nombres)):
    if generos[i] == "F":
        notas_mujeres.append(notas[i])

print("--------------------------------------")

if notas_mujeres:
    promedio_mujeres = sum(notas_mujeres) / len(notas_mujeres) 
else:
    promedio_mujeres = ("No se ingresaron mujeres. ")

if menor_nota_hombre is not None:
    print(f"El hombre con la nota más baja es: {hombre_nota_baja} con nota: {menor_nota_hombre}")
else:
    print("No se ingresaron hombres.")

print(f"El promedio de notas de las mujeres es: {promedio_mujeres:.2f}")

print("--------------------------------------")
