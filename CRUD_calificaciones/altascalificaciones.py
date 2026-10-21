from calificaciones import boletin_nota_nueva
import utilidades

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"

def obtener_ultimo_codigo(archivo):
    ultimo_codigo = "000"
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


def altas_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita los datos necesarios, valida la información y agrega una nueva calificación.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS CALIFICACIONES{RESET} ====================")

    archivo=r'tpo/CRUD_calificaciones/notas.txt'

    ultimo = obtener_ultimo_codigo(archivo)
    nuevo_codigo = siguiente_codigo(ultimo)
    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)

    # Pedir legajo del estudiante 
    while True:
        try:
            estudiante = utilidades.leerentero("Ingrese el legajo del estudiante a calificar (Formato: 100): ")
            assert estudiante in lista_legajos
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese legajo no está registrado.{RESET}")
            print("Intente nuevamente.")
    
    
    # Pedir id de la materia
    while True:
        try:
            materia = utilidades.leerentero("Ingrese el código de la materia (Formato: 100): ")
            registrado = utilidades.encontrar_dato(archivo, materia)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código de materia no está registrado.{RESET}")
            print("Intente nuevamente.")
        
    
    # Pedir la nota
    while True:
        try:
            nota = utilidades.leerentero("Ingrese la nota: ")
            assert nota > 0 and nota <= 10
            break
        except AssertionError:
            print(f"{ROJO}ERROR: La nota debe ser mayor a 0 y menor o igual a 10.{RESET}")
            print("Intente nuevamente.")


    # Genera el código de la nueva calificación tomando el último código y sumando 1.
    if len(notas) > 0:
        codigo = notas[len(notas) - 1][0] + 1
    else: 
        codigo = 100


    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3

    try:
        arch = open(archivo, "a", encoding="UTF-8") #Importar archivo
        nueva_calificacion = f'{nuevo_codigo};{nota};{estudiante};{materia};{condicion}\n'
        arch.write(nueva_calificacion)

        print(f"{VERDE}Nota {nuevo_codigo} agregada.{RESET}")
        boletin_nota_nueva(estudiantes, estudiante, nuevo_codigo, notas, materias)

    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass