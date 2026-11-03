import re
import json

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
    try:
        with open(archivo,"r",encoding="UTF-8") as arch:
            encontrado=-1
            for linea in arch:
                datos=linea.strip().split(";")
                if int(datos[columna_buscar]) == dato:
                    encontrado = datos[columna_devolver]
            return encontrado
    except (FileNotFoundError, OSError):
        pass

def devolver_dato_json(archivo,columna_buscar,dato,columna_devolver):
    try:
        with open(archivo,"r",encoding="UTF-8") as arch:
            encontrado=-1
            datos = json.load(arch)
            for linea in datos:
                if linea[columna_buscar] == dato:
                    encontrado = linea[columna_devolver]
            return encontrado
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass

    
def obtener_matriz(archivo):
    try:
        with open(archivo,"rt",encoding="UTF-8") as arch:
            matriz = []
            for linea in arch:
                datos = linea.strip().split(";")
                matriz.append(datos)
            return matriz
    except (FileNotFoundError, OSError) as error:
            print(f'No se pudo leer el archivo {arch}: {error}')
   

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


def obtener_lista_legajos(arch_estudiantes):
    try:
        with open(arch_estudiantes, 'r', encoding="UTF-8") as datos:
            estudiantes = json.load(datos)  # Cargar el contenido existente del archivo JSON

        lista_legajos = [est["legajo"] for est in estudiantes]

    except (FileNotFoundError, OSError, json.JSONDecodeError) as error:
            pass

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

def generar_usuarios(nombre, estudiantes):
    usuario = nombre.split()
    nombre_usuario = usuario[0]
    apellido_usuario = usuario[1]
    cont = 1
    numero = 0
    primera_letra = nombre_usuario[0]
    for i in range(len(estudiantes)):
        alumno = estudiantes[i]["nombre"].split()
        if re.search(f"^{re.escape(nombre)}$", estudiantes[i]["nombre"], re.IGNORECASE):
            # Si re repite el nombre entre los estudiantes se suma una letra del nombre al usuario
            if cont < len(usuario[0]):
                cont += 1
            # Si se completó el nombre se le suma un número al usuario 
            else: 
                numero += 1
        elif re.search(f"^{primera_letra}", alumno[0], re.IGNORECASE) and re.search(f"^{apellido_usuario}$", alumno[1], re.IGNORECASE):
            # Si re repite el apellido y la primera letra entre los estudiantes se suma un número al usuario
                numero += 1
    if numero == 0:
        usuario = (nombre_usuario[:cont] + apellido_usuario).lower()
    else:
        usuario = (nombre_usuario[:cont] + apellido_usuario + str(numero)).lower()
    return usuario

def codigo_temporal(arch_materias):
    with open(arch_materias,"rt",encoding="UTF-8") as materias: 
        matriz_mat = []
        for linea in materias:
            datos = linea.strip().split(";")
            matriz_mat.append(datos)
        lista_codigo = list(map(lambda fila: fila[3] + "Pri" + fila[0] if int(fila[2]) == 1 else fila[3] + "Seg" + fila[0], matriz_mat))
    return lista_codigo


def crear_conjunto_planos(archivo, columna):
    try: 
        conjunto = set()

        with open(archivo,"rt",encoding="UTF-8") as arch1:
            for linea in arch1:
                datos = linea.strip().split(";")
                conjunto.add(int(datos[columna]))

        return conjunto
    except (FileNotFoundError, OSError) as error:
            pass


def crear_conjunto_json(archivo, columna):
    try: 
        conjunto = set()

        with open(archivo,"r",encoding="UTF-8") as arch2:
            datos = json.load(arch2)
            for dic in datos:
                conjunto.add(dic[columna])
        return conjunto
    except (FileNotFoundError, OSError, json.JSONDecodeError) as error:
            pass