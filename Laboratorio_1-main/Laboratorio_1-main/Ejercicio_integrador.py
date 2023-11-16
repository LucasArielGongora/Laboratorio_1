# Ejercicio Integrador 01
# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.
# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.

lista_productos = []
lista_precio = []
lista_marca = []
lista_fabricante = []
lista_cantidad = []

contador = 0
mas_caro_barbijo = 0
maximo_cantidad = None
unidades_jabon = 0


while contador < 5:
    while True:
        try:
            print("Ingrese el tipo de producto.")
            tipo = input("Barbijo, Jabon o Alcohol: ")
            tipo = tipo.upper()
            if tipo == 'BARBIJO' or tipo == 'JABON' or tipo == 'ALCOHOL':
                break
            else:
                print('Tipo de producto no válido. Intente nuevamente.')
        except ValueError:
            print('Error, intente nuevamente. ')

    while True:
        try:
            precio =float(input("Ingrese el precio:"))
            if precio >= 100 and precio <= 300:
                break
            else:
                    print("Ingresaste un numero no valido. debe ser entre 100 y 300. ")
        except ValueError:
            print('Error, intente nuevamente')
            

    while True:
        try:
            cantidad = int(input("ingrese la cantidad: "))
            if cantidad >= 1 and cantidad <= 1000:
                    break
            else:
                    print("Ingresaste una cantidad no valida. debe ser entre 1 y 1000. ")
        except ValueError:
            print('Error, intente nuevamente')

    marca = input("ingrese la marca: ")
    fabricante = input("ingrese el fabricante: ")
    
    lista_productos.append(tipo)
    lista_precio.append(precio)
    lista_fabricante.append(fabricante)
    lista_marca.append(marca)
    lista_cantidad.append(cantidad)

    print("----------------------------------")

    if contador == 0:
        print("El primer producto ingresó a la lista.")
    elif contador == 1:
        print("El segundo producto ingresó a la lista.")
    elif contador == 2:
        print("El tercer producto ingresó a la lista.")
    elif contador == 3:
        print("El cuarto producto ingresó a la lista.")
    else:
        print("El quinto producto ingresó a la lista.")
        print("Lista completa")

    contador += 1

print("----------------------------------")

# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
for indice in range(len(lista_productos)):
    #A
    if mas_caro_barbijo == 0 or lista_precio[indice] > mas_caro_barbijo:
        mas_caro_barbijo = lista_precio[indice]
        cant_barbijo_mas_caro = lista_cantidad[indice]
        fabr_barbijo_mas_caro = lista_fabricante[indice]
    
    # B. Del ítem con más unidades, el fabricante.
    if maximo_cantidad == None or lista_cantidad[indice] > maximo_cantidad:
        maximo_cantidad = lista_cantidad[indice]
        fabricante_max_cantidad = lista_fabricante[indice]
        producto_max_cantidad = lista_productos[indice]

    # C. Cuántas unidades de jabones hay en total.
    if lista_productos[indice] == "JABON":
        unidades_jabon += lista_cantidad[indice]

print(f"El barbijo mas caro vale {mas_caro_barbijo}, cantidad de unidades: {cant_barbijo_mas_caro}, y son marca {fabr_barbijo_mas_caro}.")
print(f"El producto con mas unidades vendidas es {producto_max_cantidad} con {maximo_cantidad}, del fabricante {fabricante_max_cantidad}.")
if unidades_jabon == 0:
    print("no se ingresaron jabones.")
else:
    print(f"Total de jabones {unidades_jabon}.")
