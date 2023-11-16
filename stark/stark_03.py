from data_stark import *

import re

def normalizar_datos(lista: list):
    '''Obtiene una lista de diccionarios y castea elcontenido de las claves en int o float.

    parametros:
        lista (list): lista de diccionarios.

    Returna:
        retorna la lista normalizada.'''
    
    if lista == []:
        print("la lista esta vacia")
        return False
    else:
        lista_normalizada = False 
        datos_modificados = False

    if not lista_normalizada:
        for heroe in lista:
            if type(heroe["altura"]) != float:
                heroe["altura"] = float(heroe["altura"])
                datos_modificados = True
            if type(heroe["peso"]) != float:
                heroe["peso"] = float(heroe["peso"])
                datos_modificados = True
            if type(heroe['fuerza']) != int:
                heroe['fuerza'] = int(heroe["fuerza"])
                datos_modificados = True
        
        lista_normalizada = True
        
        if datos_modificados:
            print ("\nDatos normalizados.\n")
        else:
            print("“Hubo un error al normalizar los datos. Verifique que la lista no este",
                " vacía o que los datos no se hayan normalizado anteriormente”")

        return lista_normalizada

def obtener_dato(diccionario: dict, key: str)->bool:
    """
    Obtiene un dato específico representado de un diccionario.

    parametros:
        diccionario (dict): El diccionario que representa.
        key (str): La clave que se desea obtener del diccionario.

    Returna:
        any: El dato asociado a la clave en el diccionario o False si no se encuentra.
    """
    if diccionario and 'nombre' in diccionario and key in diccionario:
        return diccionario[key]
    else:
        return False

def obtener_nombre(diccionario: dict)->bool:
    """
    Obtiene un dato específico de un diccionario.

    parametros:
        diccionario (dict): El diccionario que representa.
        key (str): La clave que se desea obtener del diccionario.

    Returna:
        any: El valor asociado a la clave en el diccionario o False si no se encuentra.
    """

    nombre = obtener_dato(diccionario, 'nombre')
    if nombre:
        return "Nombre: " + nombre
    else:
        return False

def obtener_nombre_y_dato(diccionario: dict, key: str)->bool:
    """
    Obtiene un dato específico representado como un diccionario.

    parametros:
        diccionario (dict): El diccionario que representa.
        key (str): La clave que se desea obtener del diccionario.

    Returna:
        any: El valor asociado a la clave en el diccionario o False si no se encuentra.
    """
    
    nombre = obtener_dato(diccionario, 'nombre')
    dato = obtener_dato(diccionario, key)


    if nombre and dato is not False:
        return f"Nombre: {nombre} | {key}: {dato}"
    else:
        return False

def obtener_maximo(lista: list, key: str)-> any:
    ''' Recibe una lista de diccionarios y una clave(str).
    
    Parametros:
        lista (list): la lista de diccionarios.
        key (str): la clave de la cual se espera el valor maximo.

    Devuelve:
        el valor maximo de la clave que se pasa como parametro.
        '''
    valor_maximo = None

    if lista == []:
        print("La lista esta vacia.")
        return False
    
    for personaje in lista:
        if key in personaje:
            if type(personaje[key]) == int or type(personaje[key]) == float:
                if valor_maximo == None or personaje[key] > valor_maximo:
                    valor_maximo = personaje[key]

    if valor_maximo != None:
        return valor_maximo
    else:
        print(f"No se encontraron valores válidos de {key} en la lista.\n")
        return False

def obtener_minimo(lista: list, key: str)-> any:
    ''' Recibe una lista de diccionarios y una clave(str).
    
    Parametros:
        lista (list): la lista de diccionarios.
        key (str): la clave de la cual se espera el valor minimo.

    Devuelve:
        el valor minimo de la clave que se pasa como parametro.
        '''
    valor = 0
    
    if lista == []:
        print("La lista esta vacia.")
        return False

    for personaje in lista:
        if key in personaje:
            if type(personaje[key]) == int or type(personaje[key]) == float:
                if valor == 0 or personaje[key] < valor:
                    valor = personaje[key]

    if valor > 0:
        return valor 
    else:
        print(f"No se encontraron valores válidos de {key} en la lista.")
        return False

def obtener_dato_cantidad(lista: list, valor: float, key: str)->list:
    '''
    Obtiene una lista con los diccionarios que tienen un valor específico para la clave.

    Parámetros:
        lista (list): Una lista de diccionarios.
        valor (float): El valor específico que se está buscando en la clave proporcionada.
        key (str): La clave del diccionario por la cual se desea filtrar los valores.

    Retorna:
        list: Una lista de diccionarios que tienen el valor específico para la clave proporcionada.
            Si no se encuentra ningún diccionario con el valor dado, retorna la lista vacía.
    '''
    
    if lista == []:
        print("La lista está vacía.")
        return []
    
    if key in ["altura", "fuerza", "peso", "edad","color_ojos"]:
        if valor == obtener_maximo(lista, key) or valor == obtener_minimo(lista, key):
            lista_resultado = []
            for heroe in lista:
                if key in heroe and heroe[key] == valor:
                    lista_resultado.append(heroe)

            return lista_resultado  
        
    else:
        print(f"No se puede buscar por la clave '{key}'.")
        return []

def stark_imprimir_heroes(lista: list):
    '''
        Imprime en consola los datos de la lista de diccionarios.¿

    parametros: 
        lista(list): la lista de heroes

    no retorna nada.
    '''   
    if lista != []:
        for heroe in lista:
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
            print("-------------------------------------")
    else:
        return False

def sumar_dato_heroe(lista:list, key:str)->float:
    '''
    Suma el dato de la lista de diccionarios asosiado a la clave que se pase por parametro
    
    Paramnetros:
        lista(list): lista de diccionarios que contiene la key.
        key(str): clave del diccionario que se desea sumar.
    
    Retorna:
        La suma total de los valores asociados a la clave.
        si no encuentra la clave retorna 0.
        '''
    suma_dato = 0
    
    for heroe in lista:
        if type(heroe)==dict and heroe != {}:
            if key in heroe:
                suma_dato += heroe[key]
        else:
            print("El diccionario esta vacio ")
    
    suma_dato = float(f"{suma_dato:.2f}")
    
    return suma_dato

def dividir(num_uno: int, num_dos: int)->float:
    '''    
    Esta función toma dos números enteros como entrada y devuelve el resultado de
    la división formateado con dos decimales, si el segundo número es mayor que 0.

    Parámetros:
        num_uno (int): El dividendo, un número entero.
        num_dos (int): El divisor, un número entero.

    Retorna:
        str: El resultado de la división formateado con dos decimales.
        False: Si el segundo número es menor o igual a 0, por ser una división inválida.
    '''
    if num_dos > 0:
        resultado = num_uno / num_dos
        resultado = float(f"{resultado:.2f}")
        return resultado
    else:
        return False

def calcular_promedio(lista: list, dato:str):
    '''
    Calcula el promedio del dato especificado en la lista.

    Esta función toma una lista de diccionarios y una clave (dato) como entrada,
    utiliza la función sumar_dato_heroe() para sumar los valores asociados a la clave
    en la lista y luego calcula el promedio dividiendo la suma por la cantidad de elementos
    en la lista. El resultado se redondea a dos decimales.

    Parámetros:
    lista (list): Lista de diccionarios que contiene el dato a sumar.
    dato (str): Clave del diccionario cuyos valores se desean promediar.

    Retorna:
    str: El promedio del dato en la lista, formateado con dos decimales.
    '''
    acumulador = (sumar_dato_heroe(lista,dato))
    promedio = (dividir(acumulador,len(lista)))
    resultado = f"{promedio:.2f}"
    return resultado

def mostrar_promedio_dato(lista: list, key: str):
    '''
    Verifica si la lista no está vacía y si la clave especificada existe
    en el primer diccionario de la lista. Si el dato asociado a la clave es de tipo float
    o int, utiliza la función calcular_promedio() para calcular el promedio de ese dato
    en toda la lista.

    Parámetros:
    lista (list): Lista de diccionarios que contiene el dato a promediar.
    key (str): Clave del diccionario cuyos valores se desean promediar.

    Retorna:
    str: El promedio del dato en la lista, formateado con dos decimales.
    False: Si la lista está vacía, la clave no está presente en el primer diccionario
    o el tipo de dato del valor asociado a la clave no es int o float.
    '''
    if lista == []:
        return False
    
    elif key in lista[0]:
        if type(lista[0][key]) == float or type(lista[0][key]) == int:
            resultado = calcular_promedio(lista, key)
            return resultado
    
    else:
        return False

def imprimir_menu():
    print("\n                 Desafío Stark 03")
    print("                ------------------")
    print("\n Menu:\n")
    print("1. Normalizar datos.")
    print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
    print("3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M")
    print("6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
    print("7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
    print("8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("10. Listar todos los superhéroes agrupados por color de ojos.")
    print("11. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("0. Salir\n")
    
def validar_entero(numero_str: str):
    numero_str = numero_str.strip()

    # Patrón regex para verificar números enteros positivos
    patron = r'^\d+$'

    # Verificar si el string coincide con el patrón regex
    if re.search(patron, numero_str):
        # Convertir el string a entero y retornarlo
        return int(numero_str)
    else:
        # Si no coincide con el patrón, retornar -1
        return False

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Elija una opción o presione '0' para salir: ").upper()
    opcion = validar_entero(opcion)
    return opcion

def stark_marvel_app(lista_personajes:list):
    datos_normalizados = False
    
    while True:
        opcion = stark_menu_principal()
        
        if opcion == 1:
            if datos_normalizados:
                print("Los datos ya fueron normalizados anteriormente.")
            else:
                normalizar_datos(lista_personajes)
                datos_normalizados = True
            
        elif datos_normalizados:
            
            if opcion == 2:
                #Recorrer la lista e imprimir el nombre de superhéroes de género NB
                nombres_nb = []

                for heroe in lista_personajes:
                    if heroe['genero'] == 'NB':
                        nombre = obtener_dato(heroe, 'nombre')
                        if nombre:
                            nombres_nb.append(nombre)

                if len(nombres_nb) == 1:
                    print(nombres_nb[0])
                elif len(nombres_nb) > 1:
                    nombres_formato = '\n' .join(nombres_nb)
                    print(f"NOMBRES NB: \n{nombres_formato}\n")
                else:
                    print('\nNo se encontraron heroes NB.')
                    
            elif opcion == 3:
                # Filtro la lista de héroes para obtener solo personajes de género femenino
                mujeres = [heroe for heroe in lista_personajes if heroe['genero'] == 'F']
            
                # Utiliza la función obtener_maximo para obtener la altura máxima de las mujeres
                altura_maxima = obtener_maximo(mujeres, 'altura')
                
                if mujeres:
                    altura_maxima = obtener_maximo(mujeres, 'altura')
                    if altura_maxima is not False:
                        for heroe in mujeres:
                            if 'altura' in heroe and heroe['altura'] == altura_maxima:
                                nombre_y_altura = obtener_nombre_y_dato(heroe, 'altura')
                                print(f"La altura máxima del género femenino es {nombre_y_altura}")
                else:
                    print("No se encontraron héroes de género femenino en la lista.")
                    
            elif opcion == 4:
                masculinos = [heroe for heroe in lista_personajes if heroe['genero'] == 'M']
            
                # Utiliza la función obtener_maximo para obtener la altura máxima de las mujeres
                altura_maxima = obtener_maximo(masculinos, 'altura')
                
                if masculinos:
                    altura_maxima = obtener_maximo(masculinos, 'altura')
                    if altura_maxima is not False:
                        for heroe in masculinos:
                            if 'altura' in heroe and heroe['altura'] == altura_maxima:
                                nombre_y_altura = obtener_nombre_y_dato(heroe, 'altura')
                                print(f"La altura máxima del género masculino es {nombre_y_altura}")
                else:
                    print("No se encontraron héroes de género masculino en la lista.")
            
            elif opcion == 5:
                masculinos = [heroe for heroe in lista_personajes if heroe['genero'] == 'M']
            
                # Utiliza la función obtener_maximo para obtener la altura máxima de las mujeres
                fuerza_minima = obtener_minimo(masculinos, 'fuerza')
            
                if masculinos:
                    fuerza_minima = obtener_minimo(masculinos, 'fuerza')
                    if fuerza_minima is not False:
                        for heroe in masculinos:
                            if 'fuerza' in heroe and heroe['fuerza'] == fuerza_minima:
                                nombre_y_fuerza = obtener_nombre_y_dato(heroe, 'fuerza')
                                print(f"El mas debil del género masculino es {nombre_y_fuerza}")
                else:
                    print("No se encontraron héroes de género masculino en la lista.")
            
            elif opcion == 6:
                no_binarios = [heroe for heroe in lista_personajes if heroe['genero'] == 'NB']
            
                # Utiliza la función obtener_maximo para obtener la altura máxima de las mujeres
                fuerza_minima = obtener_minimo(no_binarios, 'fuerza')
            
                if no_binarios:
                    fuerza_minima = obtener_minimo(no_binarios, 'fuerza')
                    if fuerza_minima is not False:
                        for heroe in no_binarios:
                            if 'fuerza' in heroe and heroe['fuerza'] == fuerza_minima:
                                nombre_y_fuerza = obtener_nombre_y_dato(heroe, 'fuerza')
                                print(f"El mas debil del género no binario es {nombre_y_fuerza}")
                else:
                    print("No se encontraron héroes de género no binario en la lista.")
            
            elif opcion == 7:
                #Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
                no_binarios = [heroe for heroe in lista_personajes if heroe['genero'] == 'NB']
                
                fuerza_promedio_nb = mostrar_promedio_dato(no_binarios,'fuerza')
                if len(no_binarios) > 0:
                    print(f'La fuerza promedio del genero No Binario es: {fuerza_promedio_nb}')
                else:
                    print('No se encontraron no binarios.')
                    
            elif opcion == 8:
                #Determinar cuántos superhéroes tienen cada tipo de color de ojos.
                diccionario_color_ojos = {}
                for personaje in lista_personajes:
                    color_ojos = obtener_dato(personaje, 'color_ojos')  # Obtener el color de ojos utilizando obtener_dato
                    if color_ojos:
                        color_ojos = color_ojos.capitalize()
                        # Si el color de ojos no está en el diccionario, inicialízalo con 1
                        if color_ojos not in diccionario_color_ojos:
                            diccionario_color_ojos[color_ojos] = 1
                        # Incrementar el recuento para el color de ojos existente
                        else:
                            diccionario_color_ojos[color_ojos] += 1

                # Imprimo la cantidad de cada color de ojos
                print("{:<25} {:<10}".format("Color ojos", "Cantidad"))
                for color, cantidad in diccionario_color_ojos.items():
                    print("{:<25} {:<10}".format(color, cantidad))
                
            elif opcion == 9:
                diccionario_color_pelo = {}
                for personaje in lista_personajes:
                    if personaje['color_pelo'] != 'No Hair':
                        color_pelo = obtener_dato(personaje, 'color_pelo')  # Obtener el color de ojos utilizando obtener_dato
                        if color_pelo:
                            color_pelo = color_pelo.capitalize()
                            # Si el color de ojos no está en el diccionario, inicialízalo con 1
                            if color_pelo not in diccionario_color_pelo:
                                diccionario_color_pelo[color_pelo] = 1
                            # Incrementar el recuento para el color de ojos existente
                            else:
                                diccionario_color_pelo[color_pelo] += 1

                # Imprimo la cantidad de cada color de ojos
                print("{:<25} {:<10}".format("Color pelo", "Cantidad"))
                for color, cantidad in diccionario_color_pelo.items():
                    print("{:<25} {:<10}".format(color, cantidad))
            
            elif opcion == 10:
                grupo_color_ojos = {}

                for personaje in lista_personajes:
                    
                    color_ojos = obtener_dato(personaje, 'color_ojos')
                    
                    if color_ojos:
                        color_ojos = color_ojos.capitalize()
                    
                        if color_ojos not in grupo_color_ojos:
                            grupo_color_ojos[color_ojos] = []
                    
                        grupo_color_ojos[color_ojos].append(personaje['nombre'])
                
                for color in grupo_color_ojos:
                    print(f"\nSuperheroes color de ojos {color}:\n")
                    for personaje in grupo_color_ojos[color]:
                        print(personaje)
                    print("------------------------------")
                    
            elif opcion == 11:
                grupo_inteligencia = {}

                for personaje in lista_personajes:
                    
                    inteligencia = obtener_dato(personaje, 'inteligencia')
                    
                    if inteligencia:
                        inteligencia = inteligencia.capitalize()
                    
                        if inteligencia not in grupo_inteligencia:
                            grupo_inteligencia[inteligencia] = []
                    
                        grupo_inteligencia[inteligencia].append(personaje['nombre'])
                
                for inteligencia in grupo_inteligencia:
                    print(f"\nSuperheroes por inteligencia {inteligencia}: \n")
                    
                    for personaje in grupo_inteligencia[inteligencia]:
                        print(personaje)
                    print("------------------------------")

        elif datos_normalizados == False:
            print("ERROR! Entrada invalida, Normalizar datos para acceder al resto de opciones.")
        
        elif opcion == 0:
            print("Hasta luego!")
            break

stark_marvel_app(lista_personajes)