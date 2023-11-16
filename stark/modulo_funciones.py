from data_stark import *

def mostrar_menu():
    '''
    muestra un menu con opciones de la 'A' a la 'J'

    parametros:
        no recibe.
    Returns:
        No retorna nada. muestra el manu en consola.
    '''
    while True:
        print("\n                 Desafio Stark 02")
        print("                ------------------\n")
        print("A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
        print("B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
        print("C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
        print("D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M")
        print("E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
        print("F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
        print("G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
        print("H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
        print("I. Listar todos los superhéroes agrupados por color de ojos.")
        print("J. Listar todos los superhéroes agrupados por tipo de inteligencia")

        opcion = input("Elija una opcion o presione ENTER para salir: ")
        opcion = opcion.upper()

        if opcion == "":
                print("Hasta luego!")
                break
        else: 
            seleccionar_opcion(opcion)

def seleccionar_opcion(opcion: str):
    '''
    Muestra la opcion seleccionada por consola
    '''
    if opcion == "A":
        print("\nSeleccionó opcion A:")
        print("Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB.\n")

        imprimir_lista_por_nombre(lista_personajes)

    elif opcion == "B":
        print("\nSeleccionó opcion B:")
        print("Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n")

        hallar_la_mas_alta_f(lista_personajes)

    elif opcion == "C":
        print("\nSeleccionó opcion C:")
        print("Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n")

        hallar_el_mas_alto_m(lista_personajes)

    elif opcion == "D":
        print("\nSeleccionó opcion D:")
        print("Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n")

        mas_debil_genero_m(lista_personajes)

    elif opcion == "E":
        print("\nSeleccionó opcion E:")
        print("Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n")

        mas_debil_genero_nb(lista_personajes)

    elif opcion == "F":
        print("\nSeleccionó opcion F:")
        print("Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n")

        calcular_fuerza_promedio_nb(lista_personajes)

    elif opcion == "G":
        print("\nSeleccionó opcion G:\n")
        print("Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n")

        obtener_superheroes_por_color_de_ojos(lista_personajes)

    elif opcion == "H":
        print("\nSeleccionó opcion H:\n")
        print("Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n")
        
        obtener_superheroes_por_color_de_pelo(lista_personajes)

    elif opcion == "I":
        print("\nSeleccionó opcion I:\n")
        print("Listar todos los superhéroes agrupados por color de ojos\n.")

        listar_superheroes_por_color_de_ojos(lista_personajes)

    elif opcion == "J":
        print("\nSeleccionó opcion J:\n")
        print("Listar todos los superhéroes agrupados por tipo de inteligencia\n")

        listar_superheroes_por_inteligencia(lista_personajes)

def imprimir_lista_por_nombre(lista:list):
    '''Recorre la lista imprimiendo por consola el nombre de cada personaje de género NB

    parametros:
        lista: Una lista de diccionarios, donde cada diccionario representa un personaje y debe contener
        las claves "nombre" y "genero".

    Returns:
        Esta funcion no retorna nada. Imprime por consola los nombres de los personajes cuyo genero sea "NB"
    '''
    lista_nb = []
    for personaje in lista:
        if personaje["genero"]== "NB":    
            lista_nb.append(personaje["nombre"])
        
    if len(lista_nb) > 0:    
        for nombre in lista_nb:
            print(nombre)
    else:
        print("No se encontraron personajes con ese genero")

def hallar_la_mas_alta_f(lista:list):
    """
    Esta función toma una lista de personajes y busca a la mujer más alta dentro de la lista
    que tengan el género 'F'. Imprime el nombre y la altura de la mujer más alta.

    parametros:
        lista (list): Una lista de diccionarios, donde cada diccionario representa un personaje y debe contener
        las claves "nombre", "genero" y "altura".

    Returns:
        Esta función no devuelve ningún valor. Imprime los resultados en la consola.

    Example:
        >>> personajes = [
        ...     {"nombre": "Superheroína1", "genero": "F", "altura": "170.0"},
        ...     {"nombre": "Superheroína2", "genero": "M", "altura": "180.0"},
        ...     {"nombre": "Superheroína3", "genero": "F", "altura": "175.5"},
        ... ]
        >>> hallar_la_mas_alta_f(personajes)
        La mujer más alta es Superheroína1 con una altura de 170.0 cm.
    """
    mujer_mas_alta = None

    for personaje in lista:  
        if personaje["genero"] == "F":
            altura = float(personaje["altura"])
            if mujer_mas_alta == None or altura> mujer_mas_alta["altura"]:
                mujer_mas_alta = {'Nombre': personaje["nombre"], 'altura': altura}

    if mujer_mas_alta:
        print(f"La mujer más alta es {mujer_mas_alta['Nombre']} con una altura de {mujer_mas_alta['altura']} cm.")
    else:
        print("No se encontraron mujeres en la lista.")

def hallar_el_mas_alto_m(lista:list):
    """
    Esta función toma una lista de personajes y busca al hombre más alto dentro de la lista
    que tengan el género 'M'. Imprime el nombre y la altura del hombre más alto.

    parametros:
        lista (list): Una lista de diccionarios, donde cada diccionario representa un personaje y debe contener
        las claves "nombre", "genero" y "altura".

    Returns:
        Esta función no devuelve ningún valor. Imprime los resultados en la consola.
    """
    hombre_mas_alto = None

    for personaje in lista:  
        if personaje["genero"] == "M":
            altura = float(personaje["altura"])
            if hombre_mas_alto == None or altura> hombre_mas_alto["altura"]:
                hombre_mas_alto = {'Nombre': personaje["nombre"], 'altura': altura}

    if hombre_mas_alto:
        print(f"El hombre más alto es {hombre_mas_alto['Nombre']} con una altura de {hombre_mas_alto['altura']} cm.")
    else:
        print("No se encontraron hombres en la lista.")

def mas_debil_genero_m(lista: list):
    '''
    Esta funcion encuentra y muestra al hombre mas debil.
    
    parametros:
    - lista: list una lista de diccionarios de personajes que contenga
    nombre, genero, y fuerza
    
    imprime por consola al hombre mas debil o un mensaje si no hay ninguno  '''

    hombre_mas_debil = None
    #recorre la lista en busca del genero M
    for personaje in lista:  
        if personaje["genero"] == "M":
            #casteo la fuerza a int para compararla con la fuerza actual
            fuerza = int(personaje["fuerza"])
            if hombre_mas_debil == None or fuerza < hombre_mas_debil["fuerza"]:
                hombre_mas_debil = {'Nombre': personaje["nombre"], 'fuerza': fuerza}
    #imprimo el resultado en consola
    if hombre_mas_debil:
        print(f"El hombre mas debil es {hombre_mas_debil['Nombre']} con una fuerza de {hombre_mas_debil['fuerza']} .")
    else:
        print("No se encontraron hombres en la lista.")

def mas_debil_genero_nb(lista: list):
    """
    Encuentra y muestra al superhéroe no binario 
    con la fuerza más baja en una lista de personajes.

    Parámetros:
    - lista (list): Una lista de diccionarios que representan personajes, 
    donde cada diccionario debe tener "nombre", "genero" y "fuerza".

    Resultado:
    - None: Esta función no devuelve un valor, pero muestra 
    en la consola el superhéroe no binario más débil encontrado.
    """    
    nb_mas_debil = None

    for personaje in lista:  
        if personaje["genero"] == "NB":
            print(personaje['nombre'], personaje['fuerza'])
            fuerza = int(personaje["fuerza"])
            if nb_mas_debil == None or fuerza < nb_mas_debil["fuerza"]:
                nb_mas_debil = {'Nombre': personaje["nombre"], 'fuerza': fuerza}
    
    if nb_mas_debil:
        print(f"El hombre mas debil es {nb_mas_debil['Nombre']} con una fuerza de {nb_mas_debil['fuerza']} .")
    else:
        print("No se encontraron no binarios en la lista.")

def calcular_fuerza_promedio_nb(lista: list):
    """
    Calcula y muestra el promedio de fuerza de superhéroes no binarios en una lista de personajes.

    Parámetros:
    lista (list): Una lista de diccionarios que representan personajes,
    donde cada diccionario debe tener al menos las claves "nombre", "genero" y "fuerza".

    Resultado:
    Esta función muestra en la consola el promedio de
    fuerza de superhéroes no binarios encontrado en la lista, 
    si hay alguno.
    """
    acumulador_fuerza_nb = 0
    heroes_nb = []

    for personaje in lista:
        if personaje["genero"] == "NB":
            fuerza_float = float(personaje["fuerza"])
            heroes_nb.append(personaje["nombre"])
            acumulador_fuerza_nb += fuerza_float

    if acumulador_fuerza_nb > 0:
        promedio_fuerza_nb = acumulador_fuerza_nb /len(heroes_nb)
        print(f"El promedio de fuerza no binario es: {promedio_fuerza_nb:.2f}")
    else:
        print("No se encontraron no binarios en la lista.")

def obtener_superheroes_por_color_de_ojos(lista: list):
    '''
    Toma una lista de superhéroes y cuenta cuántos tienen cada color de ojos. 

    parametros:
    lista (list): Una lista de diccionarios, donde cada diccionario representa un personaje
    de superhéroe y debe contener la clave "color_ojos" que indica el color de ojos
    del personaje.

    Returns:
    None: Esta función no devuelve ningún valor. Imprime los resultados en la consola.
    '''
    diccionario_color_ojos = {}
    for personaje in lista:
        
        color_ojos = personaje["color_ojos"]
        color_ojos = color_ojos.capitalize()
        # Si el color de ojos no está en el diccionario, inicialízalo con 1
        if color_ojos not in diccionario_color_ojos:
            diccionario_color_ojos[color_ojos] = 1
        # Incrementar el recuento para el color de ojos existente
        else:
            diccionario_color_ojos[color_ojos] += 1
    # Imprimo la cantidad de cada color de ojos
    for color in diccionario_color_ojos:
        cantidad = diccionario_color_ojos[color]
        if cantidad > 1:
            print(f"Hay {cantidad} superhéroes con color de ojos {color}")
        else:
            print(f"Hay {cantidad} superhéroe con color de ojos {color}")

def obtener_superheroes_por_color_de_pelo(lista: list):
    '''
    Toma una lista de superhéroes y cuenta cuántos tienen cada color de pelo. 

    parametros:
    lista (list): Una lista de diccionarios, donde cada diccionario representa un personaje
    de superhéroe y debe contener la clave "color_pelo" que indica el color de pelo
    del personaje.

    Returns:
    None: Esta función no devuelve ningún valor. Imprime los resultados en la consola.
    '''
    diccionario_color_pelo = {}
    contador_no_hair = 0

    for personaje in lista:
        color_pelo = personaje["color_pelo"]

        if color_pelo == '':
            print(f"{personaje['nombre']}, no hay datos del color de pelo")
        
        elif color_pelo == 'No Hair':
            contador_no_hair += 1

        # Si el color de pelo no está en el diccionario, inicialíza con 1
        elif color_pelo not in diccionario_color_pelo:    
            diccionario_color_pelo[color_pelo] = 1

        # Incremento el recuento para el color de pelo existente
        else:
            diccionario_color_pelo[color_pelo] += 1

    # Imprimo la cantidad de cada color de pelo
    for color in diccionario_color_pelo:
        cantidad = diccionario_color_pelo[color]
        if cantidad > 1:
            print(f"Hay {cantidad} superhéroes con color de pelo {color}")
        else:
            print(f"Hay {cantidad} superhéroe con color de pelo {color}")
    # Imprimo el contador de "No Hair"
    if contador_no_hair > 1:
        print(f"Hay {contador_no_hair} superhéroes sin pelo.")
    else:
        print(f"Hay {contador_no_hair} superhéroes sin pelo.")

def listar_superheroes_por_color_de_ojos(lista:list):
    '''
    Toma una lista de superhéroes,
    los agrupa por color de ojos 
    en un diccionario y los imprime. 

    parametros:
    lista (list): Una lista de diccionarios, donde cada diccionario representa un personaje
    de superhéroe y debe contener la clave "color_pelo" que indica el color de pelo
    del personaje.

    Returns:
    None: Esta función no devuelve ningún valor. Imprime los resultados en la consola.
    '''
    grupo_color_ojos = {}

    for personaje in lista:
        
        color_ojos = personaje["color_ojos"]
        color_ojos = color_ojos.capitalize()
        
        if color_ojos not in grupo_color_ojos:
            grupo_color_ojos[color_ojos] = []
        
        grupo_color_ojos[color_ojos].append(personaje['nombre'])
    
    for color in grupo_color_ojos:
        print(f"Superheroes color de ojos {color}")
        for personaje in grupo_color_ojos[color]:
            print(personaje)
        print("------------------------------")

def listar_superheroes_por_inteligencia(lista:list):
    '''
    Toma una lista de superhéroes,
    los agrupa por inteligencia 
    en un diccionario y los imprime. 

    parametros:
    lista (list): Una lista de diccionarios, donde cada diccionario representa un personaje
    de superhéroe y debe contener la clave "inteligencia" que indica el tipo
    de inteligencia del personaje.

    Returns:
    None: Esta función no devuelve ningún valor. Imprime los resultados en la consola.
    '''
    grupo_de_inteligencia = {}

    for personaje in lista:
        
        inteligencia = personaje["inteligencia"]
        inteligencia = inteligencia.capitalize()

        if inteligencia == '':
            print(f"{personaje['nombre']}: no tiene datos de inteligencia")
            print("------------------------------")
        else:
            if inteligencia not in grupo_de_inteligencia:
                grupo_de_inteligencia[inteligencia] = []
            
            grupo_de_inteligencia[inteligencia].append(personaje['nombre'])

    for inteligencia in grupo_de_inteligencia:
        print(f"Superheroes inteligencia: {inteligencia}")
        for personaje in grupo_de_inteligencia[inteligencia]:
            print(personaje)
        print("------------------------------")

