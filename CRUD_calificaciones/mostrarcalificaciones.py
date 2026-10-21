import utilidades

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"

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
    
def mostrar_calificaciones():

    archivo=r'tpo/CRUD_calificaciones/notas.txt'

    try:
        arch = open(archivo, "rt", encoding="UTF-8")
    except OSError as error:
        print(f'No se pudo leer el archivo {archivo}: {error}')
    else:
        print('Listado de productos:')
        print(f"{BOLD}{'ID Nota':<7}{'Nota':^16}{'Estudiante':<21}{'Materia':<15}{'Condición':^24}{RESET}")
        linea = arch.readline()
        while linea != '':
            datos = linea.strip().split(";")
            codigo = int(datos[0])
            nota = int(datos[1])
            estudiante = int(datos[2])
            materia = int(datos[3])
            condicion = clasificar_nota(nota)
            print(f"{codigo:^7}{nota:^16}{estudiante:<21}{materia:<15}{condicion:^36}")
            linea = arch.readline()
    finally:
        try:
            arch.close()
        except NameError as mensaje:
            print("Se ha producido un error:", mensaje)