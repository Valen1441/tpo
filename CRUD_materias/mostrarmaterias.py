import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

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
    
def mostrar_materias(materias):

    try:
        arch = open(materias, "rt", encoding="UTF-8")
    except OSError as error:
        print(f'No se pudo leer el archivo {materias}: {error}')
    else:
        print("="*82)
        print(f'{BOLD}{MAGENTA}{"MATERIAS":^82}{RESET}')
        print("="*82)
        print(f"{BOLD}{'Id Materia':<16}{'Nombre':<21}{'Cuatrimestre':^12}{'Año':^17}{'Carga Horaria':^13}{RESET}")
        print("-" * 82)
        linea = arch.readline()
        while linea != '':
            datos = linea.strip().split(";")
            codigo = int(datos[0])
            nombre = datos[1]
            if len(nombre) > 15:
                nombre = nombre[:12] + "..."
            cuatrimestre = int(datos[2])
            anio = int(datos[3])
            horaria = int(datos[4])

            print(f"{codigo:<16}{nombre:<21}{cuatrimestre:^12}{anio:^17}{horaria:^13}")
            linea = arch.readline()
    finally:
        try:
            arch.close()
        except NameError as mensaje:
            print("Se ha producido un error:", mensaje)