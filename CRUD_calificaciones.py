import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def boletin_nota_nueva(estudiantes, materias, legajo, materia, nota):
    '''
    pre: recibe las rutas de los archivos de estudiantes y de materias, el legajo del estudiante,
         el código de la materia y la nota (entera) recién registrada.
    pos: muestra por pantalla los datos del estudiante y el detalle de esa nota puntual
         (materia, nota y resultado).
    '''
    # ==============================
    # REPORTE / BOLETÍN DEL ALUMNO
    # ==============================

    # Buscar nombre del alumno
    nombre_alumno = utilidades.devolver_dato_json(estudiantes, "legajo", legajo, "nombre")

    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"BOLETÍN":^40}{RESET}')
    print("=" * 40)
    print(f"Alumno: {nombre_alumno}")
    print(f"Legajo: {legajo}")
    print("-" * 40)

    # Buscar la materia
    nombre_materia = utilidades.devolver_dato_plano(materias, 0, materia, 1)

    resultado = utilidades.clasificar_nota(nota)

    print(f"Materia: {nombre_materia}")
    print(f"Nota: {nota}")
    print(f"Resultado: {resultado}")
    print("-" * 40)


def pedir_datos_calificacion(arch_estudiantes, arch_materias):
    '''
    pre: recibe las rutas de los archivos de estudiantes y de materias.
    pos: solicita y valida legajo, código de materia y nota.
        Devuelve la tupla (legajo, materia, nota).
    '''
    legajos = utilidades.crear_conjunto_json(arch_estudiantes, "legajo")
    codigos = utilidades.crear_conjunto_planos(arch_materias, 0)
    legajo = utilidades.pedir_valor_existente(legajos, "Ingrese el legajo del estudiante (Formato: 100): ", "ERROR: Ese legajo no está registrado.")
    materia = utilidades.pedir_valor_existente(codigos, "Ingrese el código de la materia (Formato: 100): ", "ERROR: Ese código de materia no está registrado.")
    nota = utilidades.validar_rango(1, 10, "Ingrese la nota (1-10): ", "Nota inválida: ")
    return legajo, materia, nota


# =========================================== ALTAS ====================================
def altas_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe las rutas de los archivos de estudiantes, de notas y de materias.
    pos: solicita los datos necesarios, valida la información y agrega una nueva calificación.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS CALIFICACIONES{RESET} ====================")

    ultimo = utilidades.obtener_ultimo_codigo(notas)
    nuevo_codigo = utilidades.siguiente_codigo(ultimo)

    # Pedir legajo del estudiante 
    legajo, materia, nota = pedir_datos_calificacion(estudiantes, materias)

    condicion = utilidades.calcular_condicion(nota)

    try:
        arch = open(notas, "a", encoding="UTF-8") #Importar archivo
        nueva_calificacion = f'{nuevo_codigo};{nota};{legajo};{materia};{condicion}\n'
        arch.write(nueva_calificacion)
    except OSError as error:
        print(f"{ROJO}ERROR: no se pudo grabar {notas}: {error}{RESET}")
    else:
        print(f"{VERDE}Nota {nuevo_codigo} agregada.{RESET}")
        boletin_nota_nueva(estudiantes, materias, legajo, materia, nota)
    finally:
        try:
            arch.close()
        except NameError:
            pass


# =========================================== Bajas ====================================
def bajas_calificaciones(notas):
    '''
    pre: recibe la ruta del archivo de notas.
    pos: solicita el código de una calificación y elimina el registro correspondiente.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS CALIFICACIONES{RESET} ====================")

    # Pedir el codigo a eliminar
    while True:
        try:
            codigo_baja = utilidades.leerentero("Ingrese el código de la nota a eliminar (Formato: 100): ")
            registrado = utilidades.devolver_dato_plano(notas, 0, codigo_baja)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")

    if utilidades.actualizar_archivo_plano(notas, 0, codigo_baja):
        print(f"Nota {codigo_baja} eliminada.")


# =========================================== MODIFICACION ====================================
def modificar_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe las rutas de los archivos de estudiantes, de notas y de materias.
    pos: solicita una calificación existente y modifica sus datos, validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN CALIFICACIONES{RESET} ====================")

    
    # Pedir el codigo a modificar
    while True:
        try:
            codigo_modif = utilidades.leerentero("Ingrese el código de la nota a modificar (Formato: 100): ")
            nota_modificar = utilidades.devolver_dato_plano(notas, 0, codigo_modif)
            assert nota_modificar != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")
                
                
    # Pedir el nuevo legajo
    legajo, materia, nota = pedir_datos_calificacion(estudiantes, materias)
        

    condicion = utilidades.calcular_condicion(nota)

    nueva_linea = f'{codigo_modif};{nota};{legajo};{materia};{condicion}\n'

    if utilidades.actualizar_archivo_plano(notas, 0, codigo_modif, nueva_linea):
        print(f"Nota {codigo_modif} modificada.")


# =========================================== LISTADO ====================================
def mostrar_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe las rutas de los archivos de notas, de estudiantes y de materias.
    pos: muestra por pantalla el listado de calificaciones en forma de tabla, con el nombre del
         estudiante, el nombre de la materia y la condición de cada nota. Si el archivo de notas
         no se puede leer, informa el error.
    '''
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
        for linea in arch:
            datos = linea.strip().split(";")
            codigo = int(datos[0])
            nota = int(datos[1])
            legajo_est = int(datos[2])
            estudiante = utilidades.devolver_dato_json(estudiantes, "legajo", legajo_est, "nombre")
            if len(estudiante) > 15:
                estudiante = estudiante[:12] + "..."

            id_materia = int(datos[3])
            materia = utilidades.devolver_dato_plano(materias, 0, id_materia, 1)
            if len(materia) > 15:
                materia = materia[:12] + "..."

            condicion = utilidades.clasificar_nota(nota)
            print(f"{codigo:^7}{nota:^16}{estudiante:<21}{materia:<15}{condicion:^36}")
    finally:
        try:
            arch.close()
        except NameError as mensaje:
            print("Se ha producido un error:", mensaje)