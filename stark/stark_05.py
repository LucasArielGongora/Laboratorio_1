from data_stark import lista_personajes
import re
# Crear la función "imprimir_menu_desafio_5" que imprima el menú de
# opciones por pantalla (las opciones son las que se van a utilizar para
# acceder a la funcionalidad de los puntos A hasta el O y Z para salir).
# Reutilizar la función 'imprimir_dato' realizada en una práctica anterior.

def imprimir_dato(string: str):
    '''
    Recibe un string y lo imprime por consola.
    '''
    print(string)
    
def imprimir_menu_desafio_5():
    """
    Esta función imprime un menú de opciones para el usuario.

    - No recibe ningún valor.
    - No retorna ningún valor, imprime el menú en la consola.
    """
    menu = '''                  
                                <<<<<<<<<<<<<<<            
                              - Desafio Stark 5 -
                                >>>>>>>>>>>>>>>
    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F) 
    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
    M. Listar todos los superhéroes agrupados por color de ojos.
    N. Listar todos los superhéroes agrupados por color de pelo.
    O. Listar todos los superhéroes agrupados por tipo de inteligencia
    Z. Salir.
        ____________________________________________________________________'''
    
    imprimir_dato(menu)

'''Crear la funcion 'stark_menu_principal_desafio_5' la cual se encargará
de imprimir el menú de opciones y le pedirá al usuario que ingrese la
letra de una de las opciones elegidas, deberá validar la letra usando
RegEx y en caso de ser correcta tendrá que retornarla, Caso contrario
retornará -1. El usuario puede ingresar tanto letras minúsculas como
mayúsculas y ambas se deben tomar como válidas
Reutilizar la función 'imprimir_menu_Desafio_5'''

def stark_menu_principal_desafio_5():
    """
     Esta función muestra el menú principal y permite al usuario ingresar una opción.
     - No recibe ningún valor.
     - Retorna: La opción ingresada por el usuario como una cadena.
    """
    imprimir_menu_desafio_5()
    opcion_ingresada = input('Ingrese una opcion: ')
    opcion_ingresada = opcion_ingresada.strip()

    patron = r'[a-oA-OZz]'
    if re.search(patron, opcion_ingresada):
        opcion_aprobada = opcion_ingresada.upper()
        return opcion_aprobada
    else:
        print('La opción ingresada no es válida.')
        return None

def stark_marvel_app_5(lista_heroes: list):
    """
      Esta función representa una aplicación que permite interactuar con los héroes y sus datos.
      - Recibe: lista_heroes (list) - Una lista de diccionarios de héroes.
      - No retorna ningún valor, interactúa con el usuario a través del menú principal.
    """
    while True:
      opcion = stark_menu_principal_desafio_5()
      if opcion == 'A':
          print(opcion)  
      elif opcion == 'B':
          print(opcion)  
      elif opcion == 'C':
          print(opcion)  
      elif opcion == 'D':
          print(opcion)  
      elif opcion == 'E':
          print(opcion)  
      elif opcion == 'F':
          print(opcion)    
      elif opcion == 'G':
          print(opcion)  
      elif opcion == 'H':
          print(opcion)  
      elif opcion == 'I':
          print(opcion)  
      elif opcion == 'J':
          print(opcion)  
      elif opcion == 'K':
          print(opcion)  
      elif opcion == 'L':
          print(opcion)  
      elif opcion == 'M':
          print(opcion)  
      elif opcion == 'N':
          print(opcion)  
      elif opcion == 'O':
          print(opcion)  
      elif opcion == 'Z':
          print('Hasta luego!')
          break

# Crear la función 'leer_archivo' la cual recibirá por parámetro un string
# que indicará el nombre y extensión del archivo a leer (Ejemplo:
# archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
# retornará la lista de héroes como una lista de diccionarios.

def leer_archivo(string:str):
    try:
        with open(string, 'r') as archivo:
            contenido = archivo.readlines()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {string} no fue encontrado.")
        return None

# Crear la función 'guardar_archivo' la cual recibirá por parámetro un
# string que indicará el nombre con el cual se guardará el archivo junto
# con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
# tendrá un string el cual será el contenido a guardar en dicho archivo.
# Debe abrirse el archivo en modo escritura+, ya que en caso de no
# existir, lo creara y en caso de existir, lo va a sobreescribir La función
# debera retornar True si no hubo errores, caso contrario False, además
# en caso de éxito, deberá imprimir un mensaje respetando el formato:
# .Se creó el archivo: nombre_archivo.csv
# En caso de retornar False, el mensaje deberá decir: ‘Error al crear el
# archivo: nombre_archivo’
# Donde nombre_archivo será el nombre que recibirá el archivo a ser
# creado, conjuntamente con su extensión.

def guardar_archivo(nombre_archivo: str, contenido:str):
    try:
        with open(nombre_archivo, 'w') as archivo:
            contenido = archivo.readlines()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {string} no fue encontrado.")
        return None
    
