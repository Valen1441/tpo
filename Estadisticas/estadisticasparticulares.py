import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def boletin_completo(estudiantes, estudiante, notas, materias):
    '''
    pre: recibe las listas de estudiantes, notas y materias, y el legajo del estudiante.
    pos: muestra por pantalla el boletín del estudiante con sus materias, notas y resultados.
    '''
    # ==============================
    # REPORTE / BOLETÍN DEL ALUMNO
    # ==============================

    matriz_notas = utilidades.obtener_matriz(notas)

    # Buscar nombre del alumno
    nombre_alumno = utilidades.devolver_dato_json(estudiantes, "legajo", estudiante, "nombre")

    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"BOLETÍN":^40}{RESET}')
    print("=" * 40)
    print(f"Alumno: {nombre_alumno}")
    print(f"Legajo: {estudiante}")
    print("-" * 40)
    suma = 0
    total = 0

    for registro in notas:

        if int(registro[2]) == estudiante:

            nota_alumno = int(registro[1])
            codigo_materia = int(registro[3])
            suma += nota_alumno
            total += 1

            # Buscar la materia
            nombre_materia = utilidades.devolver_dato_plano(materias, 0, codigo_materia, 1)

            if nota_alumno >= 8:
                resultado = f"{AZUL}PROMOCIONADA{RESET}"
            elif nota_alumno >= 4:
                resultado = f"{VERDE}APROBADA{RESET}"
            else:
                resultado = f"{ROJO}DESAPROBADA{RESET}"

            print(f"Materia: {nombre_materia}")
            print(f"Nota: {nota_alumno}")
            print(f"Resultado: {resultado}")
            print("-" * 40)

    if total > 0:
        promedio = (lambda a, b: a / b)(suma, total)
        promedio = f"{promedio:.1f}"
        print(f"{"Promedio: ":>36}{promedio}")


def reporte_materia(materias, materia, notas, estudiantes):
    '''
    pre: recibe las matrices de materias y notas, la lista de diccionarios de estudiantes
         y el código de la materia a reportar.
    pos: muestra por pantalla el reporte de la materia con todos los estudiantes que la
         cursaron, su nota y su resultado (promocionada, aprobada o desaprobada).
    '''
    # ==============================
    # REPORTE DE LA MATERIA
    # ==============================

    matriz_notas = utilidades.obtener_matriz(notas)
    matriz_materias = utilidades.obtener_matriz(materias)

    # Buscar nombre de la materia
    nombre_materia = utilidades.devolver_dato_plano(materias, 0, materia, 1)

    # Se guardan los códigos originales para restaurarlos después.
    codigos_temp = utilidades.codigo_temporal(materias)
    codigos = [int(fila[0]) for fila in matriz_materias]
    pos_materia = codigos.index(materia)

    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"REPORTE":^40}{RESET}')
    print("=" * 40)
    print(f"Materia: {nombre_materia}")
    print(f"Código: {codigos_temp[pos_materia]}")
    print("-" * 40)
    suma = 0
    total = 0

    for registro in matriz_notas:
        if int(registro[3]) == materia:

            nota_alumno = int(registro[1])
            legajo_alumno = int(registro[2])
            suma += nota_alumno
            total += 1

            # Buscar la materia
            nombre_alumno = utilidades.devolver_dato_plano(estudiantes, "legajo", legajo_alumno, "nombre")

            if nota_alumno >= 8:
                resultado = f"{AZUL}PROMOCIONADA{RESET}"
            elif nota_alumno >= 4:
                resultado = f"{VERDE}APROBADA{RESET}"
            else:
                resultado = f"{ROJO}DESAPROBADA{RESET}"

            print(f"Alumno: {nombre_alumno}")
            print(f"Nota: {nota_alumno}")
            print(f"Resultado: {resultado}")
            print("-" * 40)

    if total > 0:
        promedio = (lambda a, b: a / b)(suma, total)
        promedio = f"{promedio:.1f}"
        print(f"{"Promedio: ":>36}{promedio}")

    if total > 0:
        promedio = (lambda a, b: a / b)(suma, total)
        promedio = f"{promedio:.1f}"
        print(f"{"Promedio: ":>36}{promedio}")


def estadisticas_particulares(notas, estudiantes, materias, titulo):
    '''
    pre: recibe la matriz de notas, la lista de diccionarios de estudiantes, la matriz de
         materias y el título que indica si se busca un estudiante o una materia.
    pos: solicita y valida el legajo del estudiante o el código de la materia, y muestra por
         pantalla su boletín completo o su reporte de notas, según corresponda.
    '''

    if titulo == "ESTUDIANTES":
        lista_legajos = utilidades.obtener_lista_legajos(estudiantes)

        while True:
            try:
                estudiante = utilidades.leerentero("Ingrese el legajo del estudiante para su boletín (Formato: 100): ")
                assert estudiante in lista_legajos
                break
            except AssertionError:
                print(f"{ROJO}ERROR: Ese legajo no está registrado.{RESET}")
                print("Intente nuevamente.")


        boletin_completo(estudiantes, estudiante, notas, materias)

    else:
        while True:
            try:
                materia = utilidades.leerentero("Ingrese el códgio de la materia para su reporte (Formato: 100): ")
                registrado = utilidades.devolver_dato_plano(materias, 0, materia)
                assert registrado != -1
                break
            except AssertionError:
                print(f"{ROJO}ERROR: Ese código no está registrado.{RESET}")
                print("Intente nuevamente.")


        reporte_materia(materias, materia, notas, estudiantes)
