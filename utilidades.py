# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"

def busqueda_secuencial(matriz, columna, dato):
    '''
    pre: recibe una matriz, el número de columna donde buscar y el dato a buscar.
    pos: devuelve la posición de la fila donde se encuentra el dato o -1 si no lo encuentra.
    '''
    i = 0
    while i < len(matriz) and matriz[i][columna] != dato:
        i += 1
    if i < len(matriz):
        return i
    else:
        return -1

def obtener_lista_legajos(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: devuelve una lista que contiene los legajos de todos los estudiantes.
    '''
    lista_legajos = []
    for i in estudiantes:
        lista_legajos.append(i["legajo"])
    return lista_legajos

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