from data_stark import*
import re

def extraer_iniciales(nombre_heroe):
    """
    Esta función toma un nombre de héroe como entrada y retorna sus iniciales.
    
    - Recibe: nombre_heroe (str) - El nombre del héroe.
    - Retorna: iniciales (str) - Las iniciales del héroe, sin "N/A".
    """
    if nombre_heroe.strip() == "":
        return "N/A"

    nombre = nombre_heroe.replace("the ", "").replace("-", " ")
    palabras = nombre.split()

    iniciales = []

    for palabra in palabras:
        inicial = ''.join (palabra[0].upper() + '.')
        iniciales.append(inicial)

    iniciales_unidas = ''.join(iniciales)
    resultado = re.sub('N.','',iniciales_unidas)

    return resultado

def definir_iniciales_nombre(heroe: dict):
    """
    Esta función recibe un diccionario de héroe y define sus iniciales en el diccionario.

    - Recibe: heroe (dict) - El diccionario del héroe con al menos una clave 'nombre'.
    - Retorna: True si las iniciales se definen con éxito, False en caso contrario.
    """
    if not type(heroe) == dict:
        return False

    if 'nombre' not in heroe:
        return False

    iniciales = f"({extraer_iniciales(heroe['nombre'])})"

    heroe['iniciales'] = iniciales

    return True

def agregar_iniciales_nombre(lista:list)->bool:
    """
    Esta función toma una lista de diccionarios de héroes y agrega las iniciales de nombre a cada héroe.

    - Recibe: lista (list) - Una lista de diccionarios de héroes, cada uno con al menos una clave 'nombre'.
    - Retorna: True si todas las iniciales se agregan con éxito, False en caso contrario.
    """
    if type(lista) == list and len(lista) > 0:
        for heroe in lista:
            if not definir_iniciales_nombre(heroe):
                print("Error: El origen de datos no contiene el formato correcto")
                return False

        return True

def stark_imprimir_nombres_con_iniciales(lista:list):
    """
    Esta función toma una lista de diccionarios de héroes, agrega iniciales a cada héroe y los imprime en un formato específico.

    - Recibe: lista (list) - Una lista de diccionarios de héroes, cada uno con al menos una clave 'nombre'.
    - No retorna ningún valor.
    """

    if type(lista) == list and len(lista) > 0:
        agregar_iniciales_nombre(lista)
        for personaje in lista:
            personaje = print(f"* {personaje['nombre']} {personaje['iniciales']}")

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    """
    Esta función genera un código de héroe basado en su género y ID.

    - Recibe: id_heroe (int) - El ID del héroe y genero_heroe (str) - El género del héroe (F, M, o NB).
    - Retorna: Un código de héroe (str) o "N/A" si los parámetros son inválidos.
    """
    genero_heroe = genero_heroe.upper()

    if genero_heroe not in ["F","M","NB"] or genero_heroe == "" or type(id_heroe) != int:
        return "N/A"
    else:
        if genero_heroe == "F" or "M":
            codigo_heroe = f"{genero_heroe}-{str(id_heroe).zfill(8)}"
        else:
            codigo_heroe = f"{genero_heroe}-{str(id_heroe).zfill(7)}"

        return codigo_heroe

def agregar_codigo_heroe(heroe:dict,id_heroe:int):
    """
    agrega el código de héroe al diccionario del héroe y verifica su longitud.

    - Recibe: heroe (dict) - El diccionario del héroe con la clave 'genero' y id_heroe (int) - El ID del héroe.
    - Retorna: True si se agrega el código de héroe con éxito y tiene una longitud de 10 caracteres, False en caso contrario.
    """
    if heroe != {} and 'genero' in heroe:
        genero_heroe = heroe["genero"]
        heroe['codigo_heroe'] = generar_codigo_heroe(id_heroe,genero_heroe)
        if len(heroe["codigo_heroe"]) == 10:
            return True
        else: return False
    else: return False

def stark_generar_codigos_heroes(lista: list):
    """
    genera códigos de héroes para una lista de diccionarios de héroes y muestra información relacionada.

    - Recibe: lista (list) - Una lista de diccionarios de héroes.
    - No retorna ningún valor.
    """
    acumulador_id = 0
    for id_heroe,personaje in enumerate(lista,1):
        agregar_codigo_heroe(personaje,id_heroe)
        acumulador_id += 1

    print('''{}
    Se asignaron {} códigos
    * El código del primer héroe es: {}
    * El ultimo codigo agregado es: {}
    '''.format(generar_separador('*',50,False),acumulador_id, lista[0]['codigo_heroe'],lista[-1]['codigo_heroe']))

def sanitizar_entero(numero_str:str):
    """
    toma un string que representa un número entero, realiza un proceso de saneamiento y validación, y retorna
    el número entero si es válido. Si el número no es un entero positivo válido, la función retorna un valor específico
    para indicar si el número es negativo o si no es un entero válido.

    Parámetros:
        numero_str (str): Un string que representa el número entero.

    Retorna:
        int: El número entero si es válido.
        -1: Si el número no es un entero positivo válido.
        -2: Si el número representa un valor negativo.
    """
    # Quitar espacios en blanco al principio y al final del string
    numero_str = numero_str.strip()

    # Verificar si el primer carácter es un signo negativo
    if numero_str and numero_str[0] == '-':
        return -2

    # Patrón regex para verificar números enteros positivos
    patron = r'^\d+$'

    # Verificar si el string coincide con el patrón regex
    if re.search(patron, numero_str):
        # Convertir el string a entero y retornarlo
        return int(numero_str)
    else:
        # Si no coincide con el patrón, retornar -1
        return -1

def sanitizar_flotante(numero_str:str):
    """
    sanitiza una cadena para convertirla en un número flotante redondeado a 2 decimales.

    - Recibe: numero_str (str) - La cadena que se desea sanitizar.
    - Retorna: El número flotante redondeado a 2 decimales, -2 si es negativo, o -1 si no es válido.
    """
    numero_str = numero_str.strip()
    if numero_str and numero_str[0] == '-':
        return -2

    # Patrón regex para verificar números enteros positivos
    patron_flotante = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'

    # Verificar si el string coincide con el patrón regex
    if re.search(patron_flotante, numero_str):
         # Convertir el string a flotante y redondearlo a 2 decimales
        numero_flotante = float(numero_str)
        numero_redondeado = round(numero_flotante, 2)
        return numero_redondeado
    else:
        # Si no coincide con el patrón, retornar -1
        return -1

def sanitizar_string(valor_str: str, valor_por_defecto: str, parámetro_opcional='-'):
    """
    sanitiza una cadena de texto, realizando ciertas transformaciones y validaciones.

    - Recibe: valor_str (str) - La cadena que se desea sanitizar, valor_por_defecto (str) - El valor por defecto,
              y parámetro_opcional (str, opcional) - Un carácter opcional.
    - Retorna: La cadena sanitizada en minúsculas, el valor por defecto en minúsculas si valor_str está vacío y se proporciona un valor por defecto, o 'N/A' si no es válido.
    """
    valor_str = valor_str.strip()

    valor_str = valor_str.replace('/', ' ')

    # Verificar si valor_str es solo texto (sin números)
    if re.match('^[a-zA-Z ]*$', valor_str):
        # Si es solo texto, convertir a minúsculas
        valor_str = valor_str.lower()
    else:

        return 'N/A'

    # Si el valor_str está vacío y se proporciona un valor por defecto, retornar el valor por defecto en minúsculas
    if not valor_str and valor_por_defecto:
        return valor_por_defecto.lower()

    return valor_str

def sanitizar_dato(heroe: dict, clave: str, tipo_dato):
    """
    sanitiza un valor en el diccionario de un héroe de acuerdo al tipo de dato especificado.

    - Recibe: heroe (dict) - El diccionario del héroe, clave (str) - La clave del valor a sanitizar, tipo_dato (str) - El tipo de dato ('string', 'entero' o 'flotante').
    - Retorna: True si el valor se sanitiza con éxito, False si el tipo de dato no es reconocido.
    """
    tipo_dato = tipo_dato.lower()

    # Verificar si tipo_dato es válido
    if tipo_dato not in ['string','entero','flotante']:
        print('Tipo de dato no reconocido')
        return False
    else:
        if tipo_dato == 'string':
            heroe[clave] = sanitizar_string(heroe[clave], heroe[clave])
        elif tipo_dato == 'entero':
            heroe[clave] = sanitizar_entero(heroe[clave])
        elif tipo_dato == 'flotante':
            heroe[clave] = sanitizar_flotante(heroe[clave])

        return True

def stark_normalizar_datos(lista_heroes:list):
    """
    normaliza los datos de una lista de héroes, sanitizando ciertas claves de acuerdo a su tipo de dato.

    - Recibe: lista_heroes (list) - Una lista de diccionarios de héroes.
    - No retorna ningún valor.
    """
    if lista_heroes == []:
        print('La lista se encuentra vacia.')

    #las claves a sanitizar
    claves_a_sanitizar = ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']

    tipos_dato = {
        'altura': 'flotante',
        'peso': 'flotante',
        'color_ojos': 'string',
        'color_pelo': 'string',
        'fuerza': 'entero',
        'inteligencia': 'entero'
    }

    for heroe in lista_heroes:
        for clave in claves_a_sanitizar:
            # Verificar si la clave existe en el héroe
            if clave in heroe:
                # Obtener el tipo de dato apropiado para la clave
                tipo_dato = tipos_dato.get(clave, 'string')  # Por defecto, considerar 'string'

                # Sanitizar el dato utilizando la función sanitizar_dato
                sanitizar_dato(heroe, clave, tipo_dato)
                print(f"Sanitizado: {clave} de {heroe['nombre']}")

    print("\nDatos normalizados")

def generar_indice_nombres(lista_heroes):
    """
    Esta función genera un índice de nombres a partir de una lista de héroes.

    - Recibe: lista_heroes (list) - Una lista de diccionarios de héroes.
    - Retorna: Una lista de palabras individuales que conforman los nombres de los héroes, o None si la lista está vacía o no contiene el formato correcto.
    """
    lista_nombres = []

    if len(lista_heroes) == 0:
        print('El origen de datos no contiene el formato correcto')
        return  # Termina la función si la lista está vacía

    for personaje in lista_heroes:
        if isinstance(personaje, dict) and 'nombre' in personaje:
            nombre = personaje['nombre']
            # Dividir el nombre en palabras
            palabras = nombre.split()
            # Extiender la lista con los nombres
            lista_nombres.extend(palabras)

    if len(lista_nombres) == 0:
        print('El origen de datos no contiene el formato correcto')
    else:
        return lista_nombres

def stark_imprimir_indice_nombre(lista_heroes: list):
    """
    Esta función genera un índice de nombres a partir de una lista de héroes y lo imprime en un formato específico.

    - Recibe: lista_heroes (list) - Una lista de diccionarios de héroes.
    - No retorna ningún valor.
    """
    lista_nombres = generar_indice_nombres(lista_heroes)
    lista_formateada = '-'.join(lista_nombres)
    print(lista_formateada)

def convertir_cm_a_mtrs(valor_cm:float):
    """
    Esta función convierte centímetros a metros y retorna el valor resultante.

    - Recibe: valor_cm (float) - El valor en centímetros a ser convertido.
    - Retorna: El valor en metros (float) redondeado a 2 decimales, o -1 si el valor no es válido.
    """
    if type(valor_cm) == float and valor_cm > 0:
        valor_mts = valor_cm / 100
        valor_mts_formateado = round(valor_mts,2)
        return valor_mts_formateado
    else:
        return -1

def generar_separador(patron: str, largo: int, imprimir=True):
    """
    Esta función genera un separador utilizando un patrón y un largo especificados, y opcionalmente lo imprime.

    - Recibe: patron (str) - El patrón a repetir, largo (int) - La cantidad de veces a repetir el patrón,
              e imprimir (bool, opcional) - Un indicador para imprimir el separador.
    - Retorna: El separador (str) generado, o "N/A" si los valores no son válidos.
    """
    # Validación del patrón
    if not (1 <= len(patron) <= 2):
        return "N/A"

    # Validación del largo
    if not (1 <= largo <= 235):
        return "N/A"

    separador = patron * largo

    if imprimir:
        print(separador)

    return separador

def generar_encabezado(titulo:str):
    """
    Esta función genera un encabezado con un título en mayúsculas y un separador.

    - Recibe: titulo (str) - El título a ser incluido en el encabezado.
    - No retorna ningún valor, imprime el encabezado.
    """
    titulo_mayus = titulo.upper()
    separador = generar_separador('*',100,False)

    print(separador + "\n" + titulo_mayus + "\n" + separador)

def imprimir_ficha_heroe(heroe: dict)->str:
    """
    Esta función imprime la ficha de un héroe con información detallada.

    - Recibe: heroe (dict) - Un diccionario con información del héroe.
    - No retorna ningún valor, imprime la ficha del héroe.
    """
    nombre = heroe['nombre']
    iniciales = heroe['iniciales']
    identidad = heroe['identidad']
    consultora = heroe['empresa']
    codigo = heroe['codigo_heroe']
    altura = convertir_cm_a_mtrs(heroe['altura'])
    peso = heroe['peso']
    fuerza = heroe['fuerza']
    color_ojos = heroe['color_ojos']
    color_pelo = heroe['color_pelo']

    generar_encabezado("PRINCIPAL")
    print(f"NOMBRE DEL HÉROE: {nombre} {iniciales}")
    print(f"IDENTIDAD SECRETA: {identidad}")
    print(f"CONSULTORA: {consultora}")
    print(f"CODIGO DE HEROE: {codigo}")

    generar_encabezado("FISICO")
    print(f"ALTURA: {altura}Mts")
    print(f"PESO: {peso}Kg")
    print(f"FUERZA: {fuerza}")

    generar_encabezado("SEÑAS PARTICULARES")
    print(f"COLOR OJOS: {color_ojos}")
    print(f"COLOR PELO: {color_pelo}")

def stark_navegar_fichas(lista_heroes:list):
    """
    Esta función permite navegar a través de las fichas de héroes en una lista y visualizar la información de cada héroe.

    - Recibe: lista_heroes (list) - Una lista de diccionarios de héroes.
    - No retorna ningún valor, interactúa con el usuario para navegar las fichas de héroes.
    """
    navegar = True
    posicion_actual = 0 
    
    while(navegar):
        imprimir_ficha_heroe(lista_heroes[posicion_actual])

        opcion = input('ingrese la opcion deseada: [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir ')
        
        if opcion == '1':
            if posicion_actual > 0:
                posicion_actual -= 1
            else:
                posicion_actual = len(lista_heroes) -1
        elif opcion == '2':
            if posicion_actual < len(lista_heroes) - 1:
                posicion_actual += 1 
            else:
                posicion_actual = 0
                
        elif opcion.lower() == 's':
            navegar = False
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

def imprimir_menu():
    """
    Esta función imprime un menú de opciones para el usuario.

    - No recibe ningún valor.
    - No retorna ningún valor, imprime el menú en la consola.
    """
    print('\n1 - Imprimir la lista de nombres junto con sus iniciales')
    print('2 - Generar códigos de héroes')
    print('3 - Normalizar datos')
    print('4 - Imprimir índice de nombres')
    print('5 - Navegar fichas')
    print('S - Salir')
    print('____________________________________________________________\n')

def stark_menu_principal():
    """
    Esta función muestra el menú principal y permite al usuario ingresar una opción.

    - No recibe ningún valor.
    - Retorna: La opción ingresada por el usuario como una cadena.
    """
    imprimir_menu()
    opcion_ingresada = input('Ingrese una opcion: ')
    return opcion_ingresada

def stark_marvel_app_4(lista_heroes: list):
    """
    Esta función representa una aplicación que permite interactuar con los héroes y sus datos.

    - Recibe: lista_heroes (list) - Una lista de diccionarios de héroes.
    - No retorna ningún valor, interactúa con el usuario a través del menú principal.
    """
    opcion_uno_ejecutada = False
    opcion_dos_ejecutada = False
    while True:
        opcion = stark_menu_principal()

        if opcion == '1':
            stark_imprimir_nombres_con_iniciales(lista_heroes)
            opcion_uno_ejecutada = True
        elif opcion == '2':
            stark_generar_codigos_heroes(lista_personajes)
            opcion_dos_ejecutada = True
        elif opcion == '3':
            stark_normalizar_datos(lista_heroes)
        elif opcion == '4':
            stark_imprimir_indice_nombre(lista_personajes)
        elif opcion == '5':
            if opcion_uno_ejecutada and opcion_dos_ejecutada:
                stark_navegar_fichas(lista_personajes)
            else:
                print('Para ejecutar esta opcion es necesario ejecutar la opcion 1 y 2 primero. ')
        elif opcion == 's':
            break
        else:
            print('ERROR, Ingresa una opcion valida')

stark_marvel_app_4(lista_personajes)
