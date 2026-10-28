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
    
def mostrar_calificaciones(notas, materias):

    try:
        arch = open(notas, "rt", encoding="UTF-8")
    except OSError as error:
        print(f'No se pudo leer el archivo {notas}: {error}')
    else:
        print("="*80)
        print(f'{BOLD}{MAGENTA}{"CALIFICACIONES":^80}{RESET}')
        print("="*80)
        print(f"{BOLD}{'ID Nota':<7}{'Nota':^16}{'Estudiante':<21}{'Materia':<15}{'Condición':^24}{RESET}")
        print("-" * 80)
        linea = arch.readline()
        while linea != '':
            datos = linea.strip().split(";")
            codigo = int(datos[0])
            nota = int(datos[1])
            estudiante = int(datos[2])
            id_materia = int(datos[3])
            materia = utilidades.devolver_dato(materias, 0, id_materia, 1)
            if len(materia) > 15:
                materia = materia[:12] + "..."

            condicion = clasificar_nota(nota)
            print(f"{codigo:^7}{nota:^16}{estudiante:<21}{materia:<15}{condicion:^36}")
            linea = arch.readline()
    finally:
        try:
            arch.close()
        except NameError as mensaje:
            print("Se ha producido un error:", mensaje)