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
    '''
    pre: recibe la ruta de un archivo de texto, la columna donde buscar, 
         el valor buscado y la columna cuyo dato se quiere devolver (por defecto, la 0).
    pos: devuelve, como cadena, el dato de columna_devolver del registro encontrado, o -1 si
         no hay ninguno o si el archivo no se puede abrir.
    '''
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
    '''
    pre: recibe la ruta de un archivo JSON con una lista de diccionarios, la clave por la que
         buscar, el valor buscado y la clave cuyo dato se quiere devolver.
    pos: devuelve el dato del registro encontrado, o -1 si no hay ninguno o si el archivo no
         se puede leer.
    '''
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
    '''
    pre: recibe opcionalmente el mensaje que se muestra al pedir el número.
    pos: pide un número por teclado hasta que se ingresa un entero válido y lo devuelve.
    '''
    while True:
        try:
            n = int(input(msj))
            break
        except ValueError:
            print(f"{ROJO}ERROR: Solo se admiten números enteros.{RESET}")
            print("Intente nuevamente.")
    return n


def codigo_temporal(codigo, cuatrimestre, anio):
    '''
    pre: recibe como strings el código, el cuatrimestre y el año de una materia.
    pos: devuelve el código temporal con el formato año + período + código.
    '''
    periodo = "Pri" if int(cuatrimestre) == 1 else "Seg"
    return anio + periodo + codigo


def crear_conjunto_planos(archivo, columna):
    '''
    pre: recibe la ruta de un archivo de texto y la columna que se quiere leer.
    pos: devuelve un conjunto con los valores enteros de esa columna. Si el archivo no se
         puede leer, devuelve un conjunto vacío.
    '''
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
    '''
    pre: recibe la ruta de un archivo JSON con una lista de diccionarios y la clave que se
         quiere leer.
    pos: devuelve un conjunto con los valores de esa clave. Si el archivo no se puede leer,
         devuelve un conjunto vacío.
    '''
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
    pre: recibe el límite inferior y superior del rango de opciones, 
         el mensaje que se muestra por pantalla y el mensaje de error.
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
    '''
    pre: recibe la ruta de un archivo de texto.
    pos: devuelve, como cadena, el código del último registro del archivo, o "99" si el
         archivo no existe o está vacío (así el primer código generado es el 100).
    '''
    ultimo_codigo = "99"
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                datos = linea.strip().split(";")
                ultimo_codigo = datos[0]
    except FileNotFoundError:
        pass  # Si no existe el archivo, empezamos desde 99 + 1
    return ultimo_codigo

def siguiente_codigo(codigo_actual):
    '''
    pre: recibe un código numérico (como cadena o como entero).
    pos: devuelve, como cadena, el código siguiente.
    '''
    numero = int(codigo_actual) + 1
    return str(numero)


def actualizar_archivo_plano(archivo, columna, valor, nueva_linea=0):
    '''
    pre: recibe la ruta de un archivo de texto, la columna donde buscar, el valor entero a buscar
         y, opcionalmente, la línea que reemplaza al registro.
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
    pre: recibe la ruta del archivo de notas, la columna por la que filtrar
         (2 = legajo del estudiante, 3 = código de la materia) y el valor entero buscado.
    pos: lee el archivo línea por línea y devuelve una matriz solo con las filas que coinciden. 
         Si el archivo no se puede leer, informa el error y devuelve una lista vacía.
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


# ============================== RECURSIVIDAD ==============================
def suma_recursiva(lista, i=0):
    '''
    pre: recibe una lista de números y el índice desde el cual sumar (por defecto, 0).
    pos: devuelve la suma de los elementos de la lista desde el índice i hasta el final.
    Caso base: i == len(lista), ya no quedan elementos, la suma es 0.
    Caso recursivo: lista[i] + la suma de los elementos que quedan desde i + 1.
    Reducción del dominio: el índice avanza de a uno hasta llegar a len(lista).
    '''
    if i == len(lista):
        return 0
    return lista[i] + suma_recursiva(lista, i + 1)


def contar_en_columna(matriz, columna, valor, i=0):
    '''
    pre: recibe una matriz de registros (listas de cadenas con números enteros), la columna a
         revisar, el valor entero buscado y la fila desde la cual contar (por defecto, 0).
    pos: devuelve cuántas filas, desde la fila i hasta el final, tienen ese valor en la columna.
    Caso base: i == len(matriz), ya no quedan filas, la cantidad es 0.
    Caso recursivo: 1 si la fila i coincide (0 si no) más la cantidad en las filas desde i + 1.
    Reducción del dominio: el índice de fila avanza de a uno hasta llegar a len(matriz).
    '''
    if i == len(matriz):
        return 0
    if int(matriz[i][columna]) == valor:
        return 1 + contar_en_columna(matriz, columna, valor, i + 1)
    return contar_en_columna(matriz, columna, valor, i + 1)


def minimo_recursivo(lista, i=0):
    '''
    pre: recibe una lista de números no vacía y el índice desde el cual buscar (por defecto, 0).
    pos: devuelve el menor elemento de la lista desde el índice i hasta el final.
         Si la lista está vacía lanza ValueError.
    Caso base: i es el último índice, el único elemento que queda es el mínimo.
    Caso recursivo: el menor entre lista[i] y el mínimo de los elementos desde i + 1.
    Reducción del dominio: el índice avanza de a uno hasta llegar al último elemento.
    '''
    if len(lista) == 0:
        raise ValueError("La lista no debe estar vacía")
    if i == len(lista) - 1:
        return lista[i]
    minimo_resto = minimo_recursivo(lista, i + 1)
    if lista[i] < minimo_resto:
        return lista[i]
    return minimo_resto


def maximo_recursivo(lista, i=0):
    '''
    pre: recibe una lista de números no vacía y el índice desde el cual buscar (por defecto, 0).
    pos: devuelve el mayor elemento de la lista desde el índice i hasta el final.
         Si la lista está vacía lanza ValueError.
    Caso base: i es el último índice, el único elemento que queda es el máximo.
    Caso recursivo: el mayor entre lista[i] y el máximo de los elementos desde i + 1.
    Reducción del dominio: el índice avanza de a uno hasta llegar al último elemento.
    '''
    if len(lista) == 0:
        raise ValueError("La lista no debe estar vacía")
    if i == len(lista) - 1:
        return lista[i]
    maximo_resto = maximo_recursivo(lista, i + 1)
    if lista[i] > maximo_resto:
        return lista[i]
    return maximo_resto