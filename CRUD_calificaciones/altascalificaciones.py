import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def boletin_nota_nueva(estudiantes, materias, legajo, materia, nota):
    '''
    pre: recibe la lista de diccionarios de estudiantes, el legajo del estudiante, el código
         de la nota recién registrada o modificada, y las matrices de notas y materias.
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


def altas_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita los datos necesarios, valida la información y agrega una nueva calificación.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS CALIFICACIONES{RESET} ====================")

    ultimo = utilidades.obtener_ultimo_codigo(notas)
    nuevo_codigo = utilidades.siguiente_codigo(ultimo)

    # Pedir legajo del estudiante 
    legajo, materia, nota = utilidades.pedir_datos_calificacion(estudiantes, materias)

    condicion = utilidades.calcular_condicion

    try:
        arch = open(notas, "a", encoding="UTF-8") #Importar archivo
        nueva_calificacion = f'{nuevo_codigo};{nota};{legajo};{materia};{condicion}\n'
        arch.write(nueva_calificacion)

        print(f"{VERDE}Nota {nuevo_codigo} agregada.{RESET}")

    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
            boletin_nota_nueva(estudiantes, legajo, nuevo_codigo, notas, materias)
        except NameError:
            pass