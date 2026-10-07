import utilidades

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"


#------------------------ CALIFICACIONES ---------------------

def boletin_nota_nueva(estudiantes, estudiante, nota, notas, materias):
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
    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)
    posicion_estudiante = lista_legajos.index(estudiante)
    nombre_alumno = estudiantes[posicion_estudiante]["nombre"]

    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"BOLETÍN":^40}{RESET}')
    print("=" * 40)
    print(f"Alumno: {nombre_alumno}")
    print(f"Legajo: {estudiante}")
    print("-" * 40)

    posicion_nota = utilidades.busqueda_secuencial(notas, 0, nota)

    nota_alumno = notas[posicion_nota][1]
    codigo_materia = notas[posicion_nota][3]

    # Buscar la materia
    posicion_materia = utilidades.busqueda_secuencial(materias, 0, codigo_materia)
    nombre_materia = materias[posicion_materia][1]

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

#------------------ ALTAS CALIFICACIONES ---------------------
def altas_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita los datos necesarios, valida la información y agrega una nueva calificación.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS CALIFICACIONES{RESET} ====================")

    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)

    # Pedir legajo del estudiante 
    while True:
        try:
            estudiante = utilidades.leerentero("Ingrese el legajo del estudiante a calificar (Formato: 100): ")
            assert estudiante in lista_legajos
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese legajo no está registrado.{RESET}")
            print("Intente nuevamente.")
    
    
    # Pedir id de la materia
    while True:
        try:
            materia = utilidades.leerentero("Ingrese el código de la materia (Formato: 100): ")
            registrado = utilidades.busqueda_secuencial(materias, 0, materia)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código de materia no está registrado.{RESET}")
            print("Intente nuevamente.")
        
    
    # Pedir la nota
    while True:
        try:
            nota = utilidades.leerentero("Ingrese la nota: ")
            assert nota > 0 and nota <= 10
            break
        except AssertionError:
            print(f"{ROJO}ERROR: La nota debe ser mayor a 0 y menor o igual a 10.{RESET}")
            print("Intente nuevamente.")


    # Genera el código de la nueva calificación tomando el último código y sumando 1.
    if len(notas) > 0:
        codigo = notas[len(notas) - 1][0] + 1
    else: 
        codigo = 100


    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3


    # Agrega la nueva calificación a la matriz.
    notas.append([codigo, nota, estudiante, materia, condicion])

    print(f"{VERDE}Nota {codigo} agreagada.{RESET}")

    boletin_nota_nueva(estudiantes, estudiante, codigo, notas, materias)
    

#------------------ BAJAS CALIFICACIONES ---------------------
def bajas_calificaciones(notas):
    '''
    pre: recibe la matriz de calificaciones.
    pos: solicita el código de una calificación y elimina el registro correspondiente.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS CALIFICACIONES{RESET} ====================")

    # Pedir el codigo a eliminar
    while True:
        try:
            codigo = utilidades.leerentero("Ingrese el código de la nota a eliminar (Formato: 100): ")
            registrado = utilidades.busqueda_secuencial(notas, 0, codigo)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")

                    
    # Elimina de la matriz la fila encontrada.
    notas.pop(registrado)
    
    print(f"{NARANJA}Nota {codigo} eliminada.{RESET}")
    

#------------------ MODIFICACION CALIFICACIONES ---------------------
def modificar_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita una calificación existente y modifica sus datos, validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN CALIFICACIONES{RESET} ====================")

    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)
    
    # Pedir el codigo a modificar
    while True:
        try:
            codigo = utilidades.leerentero("Ingrese el código de la nota a modificar (Formato: 100): ")
            nota_modificar = utilidades.busqueda_secuencial(notas, 0, codigo)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")
                
                
    # Pedir el nuevo legajo
    while True:
        try:
            legajo = utilidades.leerentero("Ingrese el legajo del estudiante a calificar (Formato: 100): ")
            assert legajo in lista_legajos
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese legajo no está registrado.{RESET}")
            print("Intente nuevamente.")

        
    # Pedir el nuevo codigo de materia
    while True:
        try:
            materia = utilidades.leerentero("Ingrese el código de la materia (Formato: 100): ")
            registrado = utilidades.busqueda_secuencial(materias, 0, materia)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código de materia no está registrado.{RESET}")
            print("Intente nuevamente.")

    
    # Pedir la nueva nota
    while True:
        try:
            nota = utilidades.leerentero("Ingrese la nota: ")
            assert nota > 0 and nota <= 10
            break
        except AssertionError:
            print(f"{ROJO}ERROR: La nota debe ser mayor a 0 y menor o igual a 10.{RESET}")
            print("Intente nuevamente.")
        

    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3

    # Reemplaza los datos de la calificación seleccionada.
    notas[nota_modificar][0] = codigo
    notas[nota_modificar][1] = nota
    notas[nota_modificar][2] = legajo
    notas[nota_modificar][3] = materia
    notas[nota_modificar][4] = condicion
    
    print(f"{AZUL}Nota {codigo} modificada.{RESET}")
    
    boletin_nota_nueva(estudiantes, legajo, codigo, notas, materias)
        

#------------------ MOSTRAR CALIFICACIONES ---------------------
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
    
def imprimir_calificacion(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: muestra por pantalla todas las calificaciones en formato de tabla.
    '''
    # Encabezado
    print("="*80)
    print(f'{BOLD}{MAGENTA}{"CALIFICACIONES":^80}{RESET}')
    print("="*80)
    print(f"{BOLD}{'ID Nota':<7}{'Nota':^16}{'Estudiante':<21}{'Materia':<15}{'Condición':^24}{RESET}")
    print("-" * 80)

    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)

    # Datos
    for i in range(len(notas)):
        id_nota = notas[i][0]
        nota = notas[i][1]

        estudiante = notas[i][2]
        pos = lista_legajos.index(estudiante)
        estudiante = estudiantes[pos]["nombre"]
        if len(estudiante) > 15:
            estudiante = estudiante[:12] + "..."

        materia = notas[i][3]
        pos = utilidades.busqueda_secuencial(materias, 0, materia)
        materia = materias[pos][1]
        if len(materia) > 15:
            materia = materia[:12] + "..."
        
        condicion = clasificar_nota(nota)
        print(f"{id_nota:^7}{nota:^16}{estudiante:<21}{materia:<15}{condicion:^36}")

def ordenar_notas(notas, columna, reversa):
    '''
    pre: recibe una matriz, el número de columna por la cual ordenar y un indicador de orden.
    pos: ordena la matriz por la columna indicada, de forma ascendente o descendente.
    '''
    if reversa == 0: 
        notas_ordenadas = sorted(notas, key=lambda fila: fila[columna])
    else:
        notas_ordenadas = sorted(notas, key=lambda fila: fila[columna], reverse=True)
    return notas_ordenadas

def mostrar_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita la columna y el tipo de orden, ordena las calificaciones y las muestra por pantalla.
    '''

    while True:
        try:
            columna = utilidades.leerentero("""Ingrese el número de la columna para ordenar 
(1 = id, 2 = nota, 3 = legajo estudiante, 4 = id materia, 5 = condicion): """) - 1
            assert columna >= 0 and columna <= 4
            break
        except AssertionError:
            print(f"{ROJO}Número inválido, la matriz posee 5 columnas{RESET}")
            print("Intente nuevamente.")

    
    while True:
        try:
            reversa = utilidades.leerentero("Ingrese 0 = ascendente, 1 = descendente: ")
            assert reversa >= 0 and reversa <= 1
            break
        except AssertionError:
            print(f"{ROJO}Número inválido, rango valido de 0 a 1{RESET}")
            print("Intente nuevamente.")

    notas_ordenadas = ordenar_notas(notas, columna, reversa)
    imprimir_calificacion(notas_ordenadas, estudiantes, materias)