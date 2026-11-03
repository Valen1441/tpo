import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

    
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
        for linea in arch:
            datos = linea.strip().split(";")
            codigo = utilidades.codigo_temporal(datos[0], datos[2], datos[3])
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