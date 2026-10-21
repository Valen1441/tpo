import re

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"

def encontrar_dato(archivo,columna,dato):
    arch= open(archivo,"rt",encoding="UTF-8")
    encontrado=-1

    for linea in arch:
        with open(archivo,"rt",encoding="UTF-8") as arch:
            datos=linea.strip().split(";")
            if int(datos[columna])==dato:
                encontrado=dato
    return encontrado
   

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

def codigo_temporal(fila, materias):
    codigos = [fila[0] for fila in materias]
    lista_codigo = list(map(lambda fila: str(fila[3]) + "Pri" + str(fila[0]) if fila[2] == 1 else str(fila[3]) + "Seg" + str(fila[0]), materias))
    for fila in range(len(materias)):
        materias[fila][0] = lista_codigo[fila]
    return codigos
def restaurar_codigos(materias, codigos):
    for fila in range(len(materias)):
        materias[fila][0] = codigos[fila]