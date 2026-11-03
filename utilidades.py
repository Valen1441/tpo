import re
import json
import os

# Códigos ANSI
def codigos_ansi():
    RESET = "\033[0m"
    BOLD  = "\033[1m"
    ROJO  = "\033[31;1m"
    VERDE = "\033[32;1m"
    AZUL  = "\033[34;1m"
    MAGENTA  = "\033[35;1m"
    NARANJA = "\033[33;1m"
    CELESTE = "\033[36;1m"
    return RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE

RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = codigos_ansi()


def devolver_dato_plano(archivo,columna_buscar,dato,columna_devolver=0):
    encontrado=-1
    try:
        with open(archivo,"r",encoding="UTF-8") as arch:
            for linea in arch:
                datos=linea.strip().split(";")
                if int(datos[columna_buscar]) == dato:
                    encontrado = datos[columna_devolver]
    except OSError:
        pass
    return encontrado

def devolver_dato_json(archivo,columna_buscar,dato,columna_devolver):
    encontrado=-1
    try:
        with open(archivo,"r",encoding="UTF-8") as arch:
            datos = json.load(arch)
            for linea in datos:
                if linea[columna_buscar] == dato:
                    encontrado = linea[columna_devolver]
    except (OSError, json.JSONDecodeError):
        pass
    return encontrado


def leerentero(msj="Ingrese un número: "):
    ''' Función para ingresar un número entero '''
    while True:
        try:
            n = int(input(msj))
            break
        except ValueError:
            print(f"{ROJO}ERROR: Solo se admiten números enteros.{RESET}")
            print("Intente nuevamente.")
    return n

def generar_usuarios(nombre, estudiantes):
    usuario = nombre.split()
    nombre_usuario = usuario[0]
    apellido_usuario = usuario[1]
    cont = 1
    numero = 0
    primera_letra = nombre_usuario[0]
    for est in estudiantes:
        alumno = est["nombre"].split()
        if re.search(f"^{re.escape(nombre)}$", est["nombre"], re.IGNORECASE):
            # Si re repite el nombre entre los estudiantes se suma una letra del nombre al usuario
            if cont < len(nombre_usuario):
                cont += 1
            # Si se completó el nombre se le suma un número al usuario 
            else: 
                numero += 1
        elif re.search(f"^{re.escape(primera_letra)}", alumno[0], re.IGNORECASE) and re.search(f"^{re.escape(apellido_usuario)}$", alumno[1], re.IGNORECASE):
            # Si se repite el apellido y la primera letra entre los estudiantes se suma un número al usuario
                numero += 1
    if numero == 0:
        usuario = (nombre_usuario[:cont] + apellido_usuario).lower()
    else:
        usuario = (nombre_usuario[:cont] + apellido_usuario + str(numero)).lower()
    return usuario

def codigo_temporal(codigo, cuatrimestre, anio):
    '''
    pre: recibe como strings el código, el cuatrimestre y el año de una materia.
    pos: devuelve el código temporal con el formato año + período + código.
    '''
    periodo = "Pri" if int(cuatrimestre) == 1 else "Seg"
    return anio + periodo + codigo

def crear_conjunto_planos(archivo, columna):
    conjunto = set()
    try: 
        with open(archivo,"rt",encoding="UTF-8") as arch1:
            for linea in arch1:
                datos = linea.strip().split(";")
                conjunto.add(int(datos[columna]))
    except OSError:
        pass
    return conjunto


def crear_conjunto_json(archivo, llave):
    conjunto = set()
    try: 
        with open(archivo,"r",encoding="UTF-8") as arch2:
            datos = json.load(arch2)
            for dic in datos:
                conjunto.add(dic[llave])
    except (OSError, json.JSONDecodeError):
        pass
    return conjunto


def validar_rango(desde, hasta, msj="Ingrese una opción: ", error="Opción inválida: "):
    '''
    pre: recibe el límite inferior y superior del rango de opciones.
    pos: devuelve la opción ingresada por el usuario, validando que sea numérica
         y que se encuentre dentro del rango indicado.
    '''

    while True:
        try:
            numero = leerentero(msj)
            assert numero >= desde and numero <= hasta
            break
        except AssertionError:
            print(f"{ROJO}{error}rango permitido de {desde} a {hasta}.{RESET}")
            print("Intente nuevamente.")
    return numero


def pedir_datos_estudiante():
    '''
    pre: no recibe parámetros.
    pos: solicita y valida nombre y apellido, edad y año de cursada.
         Devuelve la tupla (nombre, edad, anio).
    '''
    patron = r"^[A-Za-zÁÉÍÓÚÑáéíóúñ]+ +[A-Za-zÁÉÍÓÚÑáéíóúñ]+$"
    nombre = input("Ingrese el nombre y apellido del estudiante: ").strip().title()
    while not re.search(patron, nombre):
        print(f"{ROJO}ERROR: ingrese solo un nombre y un apellido, con letras.{RESET}")
        nombre = input("Ingrese otra vez el nombre y apellido: ").strip().title()
    nombre = " ".join(nombre.split())
    edad = validar_rango(17, 100, "Ingrese la edad (17-100): ", "Edad inválida: ")
    anio = validar_rango(1, 9, "Ingrese el año de cursada (1-9): ", "Año de cursada inválido: ")
    return nombre, edad, anio


def pedir_datos_materia():
    '''
    pre: no recibe parámetros.
    pos: solicita y valida nombre, cuatrimestre, año y carga horaria.
         Devuelve la tupla (nombre, cuatrimestre, anio, horaria).
    '''
    nombre = input("Ingrese el nombre de la materia: ")
    sin_espacios = "".join(nombre.split())
    while not sin_espacios.isalnum() or sin_espacios.isdigit():
        print(f"{ROJO}ERROR: use solo letras, números y espacios, con al menos una letra.{RESET}")
        nombre = input("Ingrese el nombre de la materia: ")
        sin_espacios = "".join(nombre.split())
    nombre = " ".join(nombre.split()).title()
    cuatrimestre = validar_rango(1, 2, "Ingrese el cuatrimestre (1-2): ", "Cuatrimestre inválido: ")
    anio = validar_rango(1, 5, "Ingrese el año de la materia (1-5): ", "Año inválido: ")
    horaria = validar_rango(1, 12, "Ingrese la carga horaria (1-12): ", "Carga horaria inválida: ")
    return nombre, cuatrimestre, anio, horaria



def pedir_valor_existente(conjunto, msj, error):
    '''
    pre: recibe un conjunto de valores válidos, el mensaje a mostrar y el de error.
    pos: pide un entero hasta que pertenezca al conjunto y lo devuelve.
    '''
    while True:
        try:
            valor = leerentero(msj)
            assert valor in conjunto
            break
        except AssertionError:
            print(f"{ROJO}{error}{RESET}")
            print("Intente nuevamente.")
    return valor


def pedir_datos_calificacion(arch_estudiantes, arch_materias):
    '''
    pre: recibe las rutas de los archivos de estudiantes y de materias.
    pos: solicita y valida legajo, código de materia y nota.
        Devuelve la tupla (legajo, materia, nota).
    '''
    legajos = crear_conjunto_json(arch_estudiantes, "legajo")
    codigos = crear_conjunto_planos(arch_materias, 0)
    legajo = pedir_valor_existente(legajos, "Ingrese el legajo del estudiante (Formato: 100): ", "ERROR: Ese legajo no está registrado.")
    materia = pedir_valor_existente(codigos, "Ingrese el código de la materia (Formato: 100): ", "ERROR: Ese código de materia no está registrado.")
    nota = validar_rango(1, 10, "Ingrese la nota (1-10): ", "Nota inválida: ")
    return legajo, materia, nota


def clasificar_nota(nota):
    '''
    pre: recibe una nota numérica.
    pos: devuelve una cadena que indica si la nota es promocionada, aprobada o desaprobada.
    '''
    if nota >= 8:
        cadena = f"{AZUL}Promocionada{RESET}"
    elif nota >= 4:
        cadena = f"{VERDE}Aprobada{RESET}"
    else:
        cadena = f"{ROJO}Desaprobada{RESET}"
    return cadena


def calcular_condicion(nota):
    '''
    pre: recibe una nota entera.
    pos: devuelve 2 si está promocionada (>= 8), 1 si está aprobada (>= 4) y 3 si está desaprobada.
    '''
    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3
    return condicion


def obtener_ultimo_codigo(archivo):
    ultimo_codigo = "99"
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                datos = linea.strip().split(";")
                ultimo_codigo = datos[0]
    except FileNotFoundError:
        pass  # Si no existe el archivo, empezamos desde cero
    return ultimo_codigo

def siguiente_codigo(codigo_actual):
    numero = int(codigo_actual) + 1
    return str(numero)




def actualizar_archivo_plano(archivo, columna, valor, nueva_linea=0):
    '''
    pre: recibe la ruta de un archivo de texto con campos separados por ";", la columna
        donde buscar, el valor entero a buscar y, opcionalmente, la línea que reemplaza al registro.
    pos: copia el archivo a uno temporal salteando el registro (o reemplazándolo si hay nueva_linea)
        y luego reemplaza el original. Devuelve True si completó la operación y False si hubo error.
    '''
    temp = "temp.txt"
    actualizo = False
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            with open(temp, "wt", encoding="UTF-8") as aux:
                for linea in arch:
                    datos = linea.strip().split(";")
                    if int(datos[columna]) != valor:
                        aux.write(linea)
                    elif nueva_linea != 0:
                        aux.write(nueva_linea)
    except (OSError, ValueError) as error:
        print(f"{ROJO}ERROR: no se pudo procesar {archivo}: {error}{RESET}")
    else:
        try:
            os.remove(archivo)
            os.rename(temp, archivo)
            actualizo = True
        except OSError as error:
            print(f"{ROJO}ERROR al reemplazar el archivo: {error}{RESET}")
    return actualizo


def nombres_con_valor(lista, posicion, valor):
    '''
    pre: recibe una lista de filas, la posición de la columna a comparar y un valor.
    pos: devuelve, ordenados alfabéticamente y separados por coma, los nombres
         (columna 0) de las filas que tienen ese valor en la columna indicada.
    '''
    empates = filter(lambda fila: fila[posicion] == valor, lista)
    nombres = map(lambda fila: fila[0], empates)
    return ", ".join(sorted(nombres))



def filtrar_notas(arch_notas, columna, valor):
    '''
    pre: recibe la ruta de notas.txt, la columna (entera) por la que filtrar
         (2 = legajo del estudiante, 3 = código de la materia) y el valor entero buscado.
    pos: lee el archivo línea por línea y devuelve una matriz solo con las filas
         que coinciden (cada fila es una lista de strings). Si el archivo no se
         puede leer, informa el error y devuelve una lista vacía.
    '''
    matriz = []
    try:
        with open(arch_notas, "rt", encoding="UTF-8") as notas:
            for linea in notas:
                datos = linea.strip().split(";")
                if int(datos[columna]) == valor:
                    matriz.append(datos)
    except (OSError, ValueError) as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_notas}: {error}{RESET}")
    return matriz