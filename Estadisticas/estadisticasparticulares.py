import utilidades
 
# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()
 
 
def boletin_completo(estudiantes, legajo, notas, materias):
    '''
    pre: recibe las rutas de estudiantes, notas y materias, y el legajo (entero) del estudiante.
    pos: muestra por pantalla el boletín del estudiante con sus materias, notas, resultados
         y promedio. Si no tiene notas registradas, lo informa.
    '''
    nombre_alumno = utilidades.devolver_dato_json(estudiantes, "legajo", legajo, "nombre")
 
    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"BOLETÍN":^40}{RESET}')
    print("=" * 40)
    print(f"Alumno: {nombre_alumno}")
    print(f"Legajo: {legajo}")
    print("-" * 40)
 
    # Solo las notas de este estudiante (columna 2 = legajo)
    matriz_notas = utilidades.filtrar_notas(notas, 2, legajo)
    suma = 0
 
    for registro in matriz_notas:
        nota = int(registro[1])
        codigo_materia = int(registro[3])
        suma += nota
        nombre_materia = utilidades.devolver_dato_plano(materias, 0, codigo_materia, 1)
 
        print(f"Materia: {nombre_materia}")
        print(f"Nota: {nota}")
        print(f"Resultado: {utilidades.clasificar_nota(nota)}")
        print("-" * 40)
 
    if len(matriz_notas) > 0:
        print(f"{'Promedio: ':>36}{suma / len(matriz_notas):.1f}")
    else:
        print("El estudiante no tiene notas registradas.")
 
 
def reporte_materia(materias, materia, notas, estudiantes):
    '''
    pre: recibe las rutas de materias, notas y estudiantes, y el código (entero) de la materia.
    pos: muestra por pantalla el reporte de la materia con todos los estudiantes que la
         rindieron, su nota y su resultado, y el promedio. Si no tiene notas registradas,
         lo informa.
    '''
    nombre_materia = utilidades.devolver_dato_plano(materias, 0, materia, 1)
    cuatrimestre = utilidades.devolver_dato_plano(materias, 0, materia, 2)
    anio = utilidades.devolver_dato_plano(materias, 0, materia, 3)
    codigo_temporal = utilidades.codigo_temporal(str(materia), cuatrimestre, anio)
 
    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"REPORTE":^40}{RESET}')
    print("=" * 40)
    print(f"Materia: {nombre_materia}")
    print(f"Código: {codigo_temporal}")
    print("-" * 40)
 
    # Solo las notas de esta materia (columna 3 = código de materia)
    matriz_notas = utilidades.filtrar_notas(notas, 3, materia)
    suma = 0
 
    for registro in matriz_notas:
        nota = int(registro[1])
        legajo_alumno = int(registro[2])
        suma += nota
        nombre_alumno = utilidades.devolver_dato_json(estudiantes, "legajo", legajo_alumno, "nombre")
 
        print(f"Alumno: {nombre_alumno}")
        print(f"Nota: {nota}")
        print(f"Resultado: {utilidades.clasificar_nota(nota)}")
        print("-" * 40)
 
    if len(matriz_notas) > 0:
        print(f"{'Promedio: ':>36}{suma / len(matriz_notas):.1f}")
    else:
        print("La materia no tiene notas registradas.")
 
 
def estadisticas_particulares(notas, estudiantes, materias, titulo):
    '''
    pre: recibe las rutas de notas, estudiantes y materias, y el título que indica
         si se busca un estudiante o una materia.
    pos: solicita y valida el legajo del estudiante o el código de la materia, y muestra
         por pantalla su boletín completo o su reporte de notas, según corresponda.
    '''
    if titulo == "ESTUDIANTES":
        legajos = utilidades.crear_conjunto_json(estudiantes, "legajo")
 
        while True:
            try:
                legajo = utilidades.leerentero("Ingrese el legajo del estudiante para su boletín (Formato: 100): ")
                assert legajo in legajos
                break
            except AssertionError:
                print(f"{ROJO}ERROR: Ese legajo no está registrado.{RESET}")
                print("Intente nuevamente.")
 
        boletin_completo(estudiantes, legajo, notas, materias)
 
    else:
        codigos = utilidades.crear_conjunto_planos(materias, 0)
 
        while True:
            try:
                materia = utilidades.leerentero("Ingrese el código de la materia para su reporte (Formato: 100): ")
                assert materia in codigos
                break
            except AssertionError:
                print(f"{ROJO}ERROR: Ese código no está registrado.{RESET}")
                print("Intente nuevamente.")
 
        reporte_materia(materias, materia, notas, estudiantes)