# Luego de analizar el set de datos correspondiente resolver el Desafío #01:

# A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
# B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
# fuerza (MÁXIMO)
# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
# (MÍNIMO)
# D. Recorrer la lista y determinar el peso promedio de los superhéroes
# masculinos (PROMEDIO)
# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
# género) los cuales su fuerza supere a la fuerza promedio de todas las
# superhéroes de género femenino

# NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
# las opciones (A-E)

from data_stark import *
from modulo_funciones import *
from stark_03 import normalizar_datos


print("\n                 Desafio Stark")
print("                ---------------\n")

datos_normalizados = False

while True:
    if datos_normalizados == False:  
        acceso_menu = input("Pulsa N para Normalizar datos y acceder al menu: ")
        acceso_menu = acceso_menu.upper()
            
        if acceso_menu == "N":
            normalizar_datos(lista_personajes)
            datos_normalizados = True

    if datos_normalizados == True:
        
        print("\n Menu:\n",
            "A- Datos de cada superhéroe.\n",
            "B- Identidad y peso del superheroe mas fuerte.\n",
            "C- Identidad del superheroe mas bajo.\n",
            "D- Peso promedio de los superheroes masculinos.\n",
            "E- Nombre y peso, de los que superen el promedio de la fuerza femenina.\n")

        opcion = input("Elija una opcion o presione ENTER para salir: ")
        opcion = opcion.upper()

        if opcion == "A":
            print("\nIngresó opcion A:\nDatos de cada superhéroe\n")
            for heroe in lista_personajes:
                print("------------------------------------")
                print("nombre:", heroe["nombre"])
                print("identidad:", heroe["identidad"])
                print("empresa:", heroe["empresa"])
                print("altura:", heroe["altura"])
                print("peso:", heroe["peso"])
                print("genero:", heroe["genero"])
                print("color_ojos:", heroe["color_ojos"])
                print("color_pelo:", heroe["color_pelo"])
                print("fuerza:", heroe["fuerza"])
                print("inteligencia:", heroe["inteligencia"])

        elif opcion == "B":
            print("\nIngresó opcion B:\nIdentidad y peso del superheroe mas fuerte\n")
                # B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
                # fuerza (MÁXIMO)
            mayor_fuerza = 0
            heroes_mayor_fuerza = []
            for personaje in lista_personajes:
                fuerza_heroe = int(personaje["fuerza"])
                if fuerza_heroe > mayor_fuerza:
                    mayor_fuerza = fuerza_heroe
                    heroes_mayor_fuerza = [{"identidad": personaje["identidad"],"peso": float(personaje["peso"])}]
                elif fuerza_heroe == mayor_fuerza:
                    heroes_mayor_fuerza.append({"identidad": personaje["identidad"],"peso": float(personaje["peso"])})
            if len(heroes_mayor_fuerza) > 0:
                # muestro el mensaje en singular o plural.
                if len(heroes_mayor_fuerza) == 1:
                
                    print(f"El Heroe con mayor fuerza es: {heroes_mayor_fuerza['identidad']}",f"Peso: {heroes_mayor_fuerza['peso']:.2f}kg")
                    print("-----------------------------------------------------------------------------\n")
                else:
                    print("Los héroes con mayor fuerza son:")
                    for heroe in heroes_mayor_fuerza:
                        print(f"{heroe['identidad']} - Peso: {heroe['peso']:.2f}kg")
                    print("-----------------------------------------------\n")
            else:
                print("No se encontró ningún héroe con fuerza mayor a 0")
                print("------------------------------------------------\n")

        elif opcion == "C":
            print("\ningresó opcion C: \nIdentidad del superheroe mas bajo.\n")
            # C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
            # (MÍNIMO)
            el_mas_bajo = None
            heroes_mas_bajos = []
            for personaje in lista_personajes:
                altura_heroe = float(personaje["altura"])
                if el_mas_bajo == None or el_mas_bajo > altura_heroe:
                    el_mas_bajo = altura_heroe
                    heroes_mas_bajos = [{"nombre": personaje["nombre"],
                                        "identidad": personaje["identidad"]}]
                elif el_mas_bajo == altura_heroe:
                    heroes_mas_bajos.append({"nombre": personaje["nombre"],
                                            "identidad": personaje["identidad"]})
            if len(heroes_mas_bajos) > 0:
                # muestro el mensaje en singular o plural.
                if len(heroes_mas_bajos) == 1:
                    print(f"El Heroe mas bajo es: {heroes_mas_bajos[0]['nombre']}",
                        "- identidad: {heroes_mas_bajos[0]['identidad']}.")
                else:  # terminar de corregir
                    print("Los héroes mas bajos son:")
                    for heroe in heroes_mas_bajos:
                        print(f"{heroe['identidad']} - Peso: {heroe['peso']}kg")

        elif opcion == "D":
            print("\ningresó opcion D:\nPeso promedio de los superheroes masculinos.\n")
            acumulador_peso_masculinos = 0
            heroes_masculinos = []
            for personaje in lista_personajes:
                if personaje["genero"] == "M":
                    peso_float = float(personaje["peso"])
                    heroes_masculinos.append(personaje["nombre"])
                    acumulador_peso_masculinos += peso_float
            promedio_peso_masculinos = acumulador_peso_masculinos /len(heroes_masculinos)
            print(f"El promedio de peso masculino es: {promedio_peso_masculinos:.2f}")

        elif opcion == "E":
            
            print("\ningresó opcion E:\nNombre y peso, de los que superen el promedio de la fuerza femenina.\n")
            acumulador_fuerza_f = 0
            lista_personajes_f = []
            lista_fuerza_superior_a_promedio = []
            # Casteo la fuerza a float y si es femenino lo agrego a la lista.
            for personaje in lista_personajes:
                fuerza_float = float(personaje["fuerza"])
                if personaje["genero"] == "F":
                    acumulador_fuerza_f += fuerza_float
                    lista_personajes_f.append(personaje["nombre"])
            # calculo el promedio con la cantidad de elementos de la lista.
            if len(lista_personajes_f) > 0:
                promedio_fuerza_f = acumulador_fuerza_f / len(lista_personajes_f)
            # recorro la lista y si la fuerza es mayor al promedio femenino lo agrego a lista superior fuerza al promedio.
            for personaje in lista_personajes:
                fuerza_float = float(personaje["fuerza"])
                if fuerza_float > promedio_fuerza_f:
                    lista_fuerza_superior_a_promedio.append(
                        {"Nombre": personaje["nombre"], "Peso": personaje["peso"]})
            # recorro la lista superior fuerza al promedio y muestro el nombre y peso.
            for superheroe in lista_fuerza_superior_a_promedio:
                nombre = superheroe['Nombre']
                peso_float = float(superheroe["Peso"])
                print(f"Nombre: {nombre} \nPeso: {peso_float}")
                print("-------------------------------")

        else: 
            opcion = ""
            print("Hasta luego!")
            break
    else:
        print("Necesitas normalizar los datos para acceder al menu. ")        



