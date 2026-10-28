import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

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

    nota_alumno = int(utilidades.devolver_dato(notas, 0, nota, 1))
    codigo_materia = int(utilidades.devolver_dato(notas, 0, nota, 3))

    # Buscar la materia
    nombre_materia = utilidades.devolver_dato(materias, 0, codigo_materia, 1)

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


def obtener_ultimo_codigo(archivo):
    ultimo_codigo = "000"
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                datos = linea.strip().split(";")
                ultimo_codigo = datos[0]
    except FileNotFoundError:
        pass  # Si no existe el archivo, empezamos desde cero
    return ultimo_codigo

def siguiente_codigo(codigo_actual):
    numero = int(codigo_actual) + 1
    return numero


def altas_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita los datos necesarios, valida la información y agrega una nueva calificación.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS CALIFICACIONES{RESET} ====================")

    ultimo = obtener_ultimo_codigo(notas)
    nuevo_codigo = siguiente_codigo(ultimo)
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
            registrado = utilidades.encontrar_dato(materias, 0, materia)
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


    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3

    try:
        arch = open(notas, "a", encoding="UTF-8") #Importar archivo
        nueva_calificacion = f'{nuevo_codigo};{nota};{estudiante};{materia};{condicion}\n'
        arch.write(nueva_calificacion)

        print(f"{VERDE}Nota {nuevo_codigo} agregada.{RESET}")

    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
            boletin_nota_nueva(estudiantes, estudiante, nuevo_codigo, notas, materias)
        except NameError:
            pass