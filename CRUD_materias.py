import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()


def pedir_datos_materia():
    '''
    pre: no recibe parámetros.
    pos: solicita y valida nombre, cuatrimestre, año y carga horaria.
         Devuelve la tupla (nombre, cuatrimestre, anio, horaria).
    '''
    nombre = input("Ingrese el nombre de la materia: ")
    sin_espacios = "".join(nombre.split())
    while not sin_espacios.isalnum() or sin_espacios.isdigit():
        print(f"{ROJO}ERROR: use solo letras, números y espacios, con al menos una letra.{RESET}")
        nombre = input("Ingrese el nombre de la materia: ")
        sin_espacios = "".join(nombre.split())
    nombre = " ".join(nombre.split()).title()
    cuatrimestre = utilidades.validar_rango(1, 2, "Ingrese el cuatrimestre (1-2): ", "Cuatrimestre inválido: ")
    anio = utilidades.validar_rango(1, 5, "Ingrese el año de la materia (1-5): ", "Año inválido: ")
    horaria = utilidades.validar_rango(1, 12, "Ingrese la carga horaria (1-12): ", "Carga horaria inválida: ")
    return nombre, cuatrimestre, anio, horaria


# =========================================== ALTAS ====================================
def altas_materias(materias):
    '''
    pre: recibe la ruta del archivo de materias.
    pos: agrega una nueva materia al archivo con un código,
         nombre, cuatrimestre, año y carga horaria válidos.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS MATERIAS{RESET} ====================")

    ultimo = utilidades.obtener_ultimo_codigo(materias)
    nuevo_codigo = utilidades.siguiente_codigo(ultimo)

    # Pedir nombre
    nombre, cuatrimestre, anio, horaria = pedir_datos_materia()

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


# =========================================== Bajas ====================================
def bajas_materias(materias, notas):
    '''
    pre: recibe la ruta de los archivos de materias y de notas.
    pos: solicita el código de una materia y elimina el registro correspondiente, 
         siempre que exista y no tenga una calificación registrada.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS MATERIAS{RESET} ====================")

    # Pedir el código a eliminar
    while True:
        try:
            codigo_baja = utilidades.leerentero("Ingrese el código de la materia a eliminar (Formato: 100) (0 para cancelar): ")
            if codigo_baja == 0:
                print("Operación cancelada.")
                return
            esta_en_calificaciones = utilidades.devolver_dato_plano(notas, 3, codigo_baja)
            registrado = utilidades.devolver_dato_plano(materias, 0, codigo_baja)
            assert esta_en_calificaciones == -1
            assert registrado != -1
            break
        except AssertionError:
            if registrado == -1:
                print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            else:
                print(f"{ROJO}ERROR: Esa materia tiene una calificación registrada, no se puede eliminar{RESET}")
            print("Intente nuevamente.")

    if utilidades.actualizar_archivo_plano(materias, 0, codigo_baja):
        print(f"Materia {codigo_baja} eliminada correctamente.")


# =========================================== MODIFICACION ====================================
def modificar_materias(materias):
    '''
    pre: recibe la ruta del archivo de materias.
    pos: solicita una materia existente y modifica sus datos, validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN MATERIAS{RESET} ====================")
    
    # Pedir el codigo a modificar
    while True:
        try:
            codigo_modif = utilidades.leerentero("Ingrese el código de la materia a modificar (Formato: 100) (0 para cancelar): ")
            if codigo_modif == 0:
                print("Operación cancelada.")
                return
            modificar = utilidades.devolver_dato_plano(materias, 0, codigo_modif)
            assert modificar != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")

                
    # Pedir nombre de la materia
    nombre, cuatrimestre, anio, horaria = pedir_datos_materia()


    nueva_linea = f'{codigo_modif};{nombre};{cuatrimestre};{anio};{horaria}\n'

    if utilidades.actualizar_archivo_plano(materias, 0, codigo_modif, nueva_linea):
        print(f"Materia {codigo_modif} modificada.")


# =========================================== LISTADO ====================================
def mostrar_materias(materias):
    '''
    pre: recibe la ruta del archivo de materias.
    pos: muestra por pantalla el listado de materias en forma de tabla, con su código temporal
         y recortando los nombres largos. Si el archivo no se puede leer, informa el error.
    '''
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
    finally:
        try:
            arch.close()
        except NameError as mensaje:
            print("Se ha producido un error:", mensaje)