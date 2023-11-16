# Ejercicio 5:
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final:
# -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
# descuento del 10% Mar del Plata tiene un descuento del 20%
# -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
# un aumento del 10% Mar del Plata tiene un aumento del 20%
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
# aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
# precio sin descuento.
# Validar el ingreso de datos

precioBase = 15000

precioFinal = 0
precioFinalconAumento=None
precioFinalConDescuento=None

while True:
    estacion = str(input("Ingrese estacion del año, INVIERNO, VERANO, OTOÑO O PRIMAVERA: "))
    estacion = estacion.upper()
    while estacion != "INVIERNO" and estacion != "VERANO" and estacion != "OTOÑO" and estacion != "PRIMAVERA":
        print("ERROR, no es una estacion del año.")
        estacion = str(input("Ingrese estacion del año, INVIERNO, VERANO, OTOÑO O PRIMAVERA: "))
        estacion = estacion.upper()

    localidad = str(input("Ingrese destino: Bariloche, Cataratas, Mar del Plata, Córdoba "))
    localidad= localidad.upper()
    while localidad != "BARILOCHE" and estacion != "CATARATAS" and estacion != "MAR DEL PLATA" and estacion != "CORDOBA":
        print("ERROR, no es un destino disponible.")
        localidad = str(input("Ingrese destino: Bariloche, Cataratas, Mar del Plata, Córdoba "))
        localidad= localidad.upper()
    break

match estacion:
    case 'INVIERNO':
        if localidad == 'BARILOCHE':
            precioFinal = precioBase * 1.20
        elif localidad == "MAR DEL PLATA":
            precioFinal = precioBase * 0.80
        else:
            precioFinal = precioBase * 0.90

    case 'VERANO':
        if localidad == 'BARILOCHE':
            precioFinal = precioBase * 0.80
        elif localidad == "MAR DEL PLATA":
            precioFinal = precioBase * 1.20
        else:
            precioFinal = precioBase * 1.10

    case _:#otoño-primavera
        if localidad == 'BARILOCHE':
            precioFinal = precioBase * 1.10
        elif localidad == 'CATARATAS':
            precioFinal = precioBase * 1.10
        elif localidad == 'MAR DEL PLATA':
            precioFinal = precioBase * 1.10

print(f"el precio final de la estadia es:{precioFinal}")
