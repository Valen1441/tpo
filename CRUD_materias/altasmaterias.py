import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()


def altas_materias(materias):
    '''
    pre: recibe la matriz de materias.
    pos: agrega una nueva materia a la matriz con un código,
         nombre, cuatrimestre, año y carga horaria válidos.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS MATERIAS{RESET} ====================")

    ultimo = utilidades.obtener_ultimo_codigo(materias)
    nuevo_codigo = utilidades.siguiente_codigo(ultimo)

    # Pedir nombre
    nombre, cuatrimestre, anio, horaria = utilidades.pedir_datos_materia()

    try:
        arch = open(materias, "a", encoding="UTF-8") #Importar archivo
        nueva_materia = f'{nuevo_codigo};{nombre};{cuatrimestre};{anio};{horaria}\n'
        arch.write(nueva_materia)
    except OSError as error:
        print(f"{ROJO}ERROR: no se pudo grabar {materias}: {error}{RESET}")
    else: 
        print(f"{VERDE}Materia {nuevo_codigo} agregada.{RESET}")
    finally:
        try:
            arch.close()
        except NameError:
            pass