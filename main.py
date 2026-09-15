import calificaciones
import Estudiantes
import estadisticas
import Materias

usuarios = ("Admin", "Nardone")
contrasenias = ("123", "321")

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"


def validar_rango(desde, hasta):
    '''
    pre: recibe el límite inferior y superior del rango de opciones.
    pos: devuelve la opción ingresada por el usuario, validando que sea numérica
         y que se encuentre dentro del rango indicado.
    '''
    numero = input("Ingrese una opción: " )

    # Verifica que la opción ingresada sea un número.
    while numero.isnumeric() == False:
        print(f"{ROJO}Opcion inválida. Ingrese un número dentro del rango{RESET}")
        numero = input("Ingrese nuevamente una opción: " )
    numero = int(numero)

    # Verifica que el número se encuentre dentro del rango permitido.
    while numero < desde or numero > hasta:
        print(f"{ROJO}Opción inválida. Ingrese una opción que se encuentre en el rango{RESET}")
        numero = input("Ingrese nuevamente una opción: ")
        while numero.isnumeric() == False:
                print(f"{ROJO}Opcion iválida. Ingrese un número dentro del rango{RESET}")
                numero = input("Ingrese nuevamente una opción: " )
        numero = int(numero)

    return numero


def login(usuarios_almacenados, contrasenias_almacenadas):
    '''
    pre: recibe el usuario y la contraseña almacenados.
    pos: devuelve True si el usuario y la contraseña ingresados coinciden
         con los almacenados, y False en caso contrario.
    '''
    usuario_login = input("Ingrese un usuario: ")
    contrasena_login = input("Ingrese una contraseña: ")
    inicio = False
    for i in range(len(usuarios_almacenados)):
        if usuarios_almacenados[i] == usuario_login:
            for j in range(len(contrasenias_almacenadas)):
                if contrasenias_almacenadas[j] == contrasena_login and i == j:
                    inicio = True
    if inicio: 
        return usuario_login
    else:
        return -1

#------------------------ Submenu ---------------------
def mostrar_submenu(titulo, usuario):
    '''
    pre: recibe el título del menú que se desea mostrar.
    pos: muestra por pantalla el submenú correspondiente con las opciones
         de alta, baja, modificación, listado y volver.
    '''
    if usuario == "Admin":
        print(f"""
        === MENÚ {titulo} ===
        1. ALTA
        2. BAJA
        3. MODIFICACIÓN
        4. LISTADO
        5. VOLVER AL MENÚ PRINCIPAL
        """)
    else:
        if titulo == "CALIFICACIONES":
            print(f"""
        === MENÚ CALIFICACIONES ===
        1. ALTA
        2. MODIFICACIÓN
        3. LISTADO
        4. VOLVER AL MENÚ PRINCIPAL
        """)
        else:
            print(f"""
        === MENÚ {titulo} ===
        1. LISTADO
        2. VOLVER AL MENÚ PRINCIPAL
        """)
        

def mostrar_submenu_estadistica(titulo="ESTADÍSTICAS"):
    '''
    pre: no recibe parámetros.
    pos: muestra por pantalla el submenú de estadísticas.
    '''
    if titulo == "ESTADÍSTICAS":
        print("""
    === MENÚ ESTADÍSTICAS ===
    1. MATERIAS
    2. ESTUDIANTES
    3. VOLVER AL MENÚ PRINCIPAL
    """)
    else:
        print(f"""
    === MENÚ ESTADÍSTICAS {titulo} ===
    1. GENERALES
    2. PARTICULARES
    3. VOLVER AL MENÚ ESTADÍSTICAS
    """)

#------------------ Menu Estudiantes ---------------------
def menu_estudiantes(estudiantes, notas, usuario):
    '''
    pre: recibe el diccionario de estudiantes y la matriz de calificaciones.
    pos: muestra y ejecuta las opciones del menú de estudiantes, permitiendo
         realizar altas, bajas, modificaciones y listados.
    '''
    mostrar_submenu("ESTUDIANTES", usuario)
    if usuario == "Admin" :  
        opcion = validar_rango(1, 5)
        estudiantes_con_notas = set()
        estudiantes_totales = set()
        for nota in notas:
            estudiantes_con_notas.add(nota[2])
        for estudiante in estudiantes:
            estudiantes_totales.add(estudiante["legajo"])
            print(estudiantes_totales)
        match opcion:
            case 1:
                Estudiantes.altas_estudiantes(estudiantes)
                menu_estudiantes(estudiantes, notas, usuario)
            case 2:
                if len(estudiantes) > 0:
                    if len(estudiantes_totales ^ estudiantes_con_notas) != 0:
                        Estudiantes.bajas_estudiantes(estudiantes, notas, usuario)
                    else: 
                        print(f"{ROJO}ERROR: todos los estudiantes tienen una calificación registrada, no se pueden eliminar.{RESET}")
                else:
                    print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}")
                menu_estudiantes(estudiantes, notas, usuario)
            case 3:
                if len(estudiantes) > 0:
                    Estudiantes.modificar_estudiantes(estudiantes)
                else:
                    print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}")
                menu_estudiantes(estudiantes, notas, usuario)
            case 4:
                if len(estudiantes) > 0:
                    Estudiantes.mostrar_estudiantes(estudiantes)
                else:
                    print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}")
                menu_estudiantes(estudiantes, notas, usuario)
    else:
        opcion = validar_rango(1, 2)
        if opcion == 1: 
            if len(estudiantes) > 0:
                Estudiantes.mostrar_estudiantes(estudiantes)
            else:
                print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}")
            menu_estudiantes(estudiantes, notas, usuario)

#------------------ Menu Masterias ---------------------
def menu_materias(materias, notas, usuario):
    '''
    pre: recibe las matrices de materias y calificaciones.
    pos: muestra y ejecuta las opciones del menú de materias, permitiendo
         realizar altas, bajas, modificaciones y listados.
    '''
    mostrar_submenu("MATERIAS", usuario)
    if usuario == "Admin": 
        opcion = validar_rango(1, 5)
        materias_con_notas = set()
        materias_totales = set()
        for nota in notas:
            materias_con_notas.add(nota[2])
        for materia in materias:
            materias_totales.add(materia[0])
        match opcion:
            case 1:
                Materias.altas_materias(materias)
                menu_materias(materias, notas, usuario)
            case 2:
                if len(materias) > 0:
                    if len(materias_totales ^ materias_con_notas) != 0:     
                        Materias.bajas_materias(materias, notas, usuario)
                    else:
                        print(f"{ROJO}ERROR: todas las materias tienen una calificación registrada, no se pueden eliminar.{RESET}") 
                else:
                    print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
                menu_materias(materias, notas, usuarios)
            case 3:
                if len(materias) > 0:
                    Materias.modificar_materias(materias)
                else:
                    print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
                menu_materias(materias, notas, usuario)
            case 4:
                if len(materias) > 0:
                    Materias.mostrar_materias(materias)
                else:
                    print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
                menu_materias(materias, notas, usuario)
    else: 
        opcion = validar_rango(1, 2)
        if opcion == 1:
            if len(materias) > 0:
                Materias.mostrar_materias(materias)
            else:
                print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
            menu_materias(materias, notas, usuario)


#------------------ Menu Calificaciones ---------------------
def menu_calificaciones(notas, estudiantes, materias, usuario):
    '''
    pre: recibe las matrices de calificaciones, estudiantes y materias.
    pos: muestra y ejecuta las opciones del menú de calificaciones, permitiendo
         realizar altas, bajas, modificaciones y listados.
    '''
    mostrar_submenu("CALIFICACIONES", usuario)
    if usuario == "Admin": 
        opcion = validar_rango(1, 5)
        match opcion:
            case 1:
                calificaciones.altas_calificaciones(notas, estudiantes, materias)
                menu_calificaciones(notas, estudiantes, materias, usuario)
            case 2:
                if len(notas) > 0:
                    calificaciones.bajas_calificaciones(notas)
                else:
                    print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
                menu_calificaciones(notas, estudiantes, materias, usuario)
            case 3:
                if len(notas) > 0:
                    calificaciones.modificar_calificaciones(notas, estudiantes, materias)
                else:
                    print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
                menu_calificaciones(notas, estudiantes, materias, usuario)
            case 4:
                if len(notas) > 0:
                    calificaciones.mostrar_calificaciones(notas, estudiantes, materias)
                else:
                    print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
                menu_calificaciones(notas, estudiantes, materias, usuario)
    else:
        opcion = validar_rango(1, 4)
        match opcion: 
            case 1:
                calificaciones.altas_calificaciones(notas, estudiantes, materias)
                menu_calificaciones(notas, estudiantes, materias, usuario)
            case 2:
                if len(notas) > 0:
                    calificaciones.modificar_calificaciones(notas, estudiantes, materias)
                else:
                    print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
                menu_calificaciones(notas, estudiantes, materias, usuario)
            case 3:
                if len(notas) > 0:
                    calificaciones.mostrar_calificaciones(notas, estudiantes, materias)
                else:
                    print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
                menu_calificaciones(notas, estudiantes, materias, usuario)


#------------------ Menu Estadisticas ---------------------
def menu_estadisticas(notas, estudiantes, materias):
    '''
    pre: recibe las matrices de calificaciones, estudiantes y materias.
    pos: muestra y ejecuta las opciones disponibles del menú de estadísticas.
    '''
    mostrar_submenu_estadistica()
    opcion = validar_rango(1, 3)
    match opcion:
        case 1:
            if len(notas) > 0 and len(materias) > 0:
                estadisticas_estudiantes_materias(notas, estudiantes, materias, "MATERIAS")
            else:
                if len(notas) == 0:
                    print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
                else:
                    print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
            menu_estadisticas(notas, estudiantes, materias)
        case 2:
            if len(notas) > 0 and len(estudiantes) > 0:
                estadisticas_estudiantes_materias(notas, estudiantes, materias, "ESTUDIANTES")
            else:
                if len(notas) == 0:
                    print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
                else:
                    print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}") 
            menu_estadisticas(notas, estudiantes, materias)


def estadisticas_estudiantes_materias(notas, estudiantes, materias, titulo):
    mostrar_submenu_estadistica(titulo)
    opcion = validar_rango(1, 3)
    match opcion:
        case 1:
            if titulo == "ESTUDIANTES":
                estadisticas.estadisticas_estudiantes_generales(notas, estudiantes)
            else:
                estadisticas.estadisticas_materias(notas, materias)
            estadisticas_estudiantes_materias(notas, estudiantes, materias, titulo)
        case 2:
            if titulo == "ESTUDIANTES":
                if len(materias) > 0:
                    estadisticas.estadisticas_estudiantes_particulares(notas, estudiantes, materias)
                else:
                    print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
            else:
                if len(estudiantes) > 0:
                    ...
                else:
                    print(f"{ROJO}ERROR: no hay estudiantes cargadas.{RESET}")
            estadisticas_estudiantes_materias(notas, estudiantes, materias, titulo)


def mostrar_menu_principal():
    '''
    pre: no recibe parámetros.
    pos: muestra por pantalla el menú principal del programa.
    '''
    print("""
    ==== MENÚ PRINCIPAL ====

    1. ESTUDIANTES
    2. MATERIAS
    3. CALIFICACIONES
    4. ESTADISTICAS
    5. SALIR DEL PROGRAMA
    """)
 
 
def menu_principal(estudiantes, materias, notas, usuario):
    '''
    pre: recibe el diccionario de estudiantes y las matrices de 
         materias y calificaciones.
    pos: muestra el menú principal, solicita una opción válida y ejecuta
         la función correspondiente a la opción seleccionada.
    '''
    mostrar_menu_principal()
    opcion = validar_rango(1, 5)
    match opcion:
            case 1:
                menu_estudiantes(estudiantes, notas, usuario)
                menu_principal(estudiantes, materias, notas, usuario)
            case 2:
                menu_materias(materias, notas, usuario)
                menu_principal(estudiantes, materias, notas, usuario)
            case 3:
                menu_calificaciones(notas, estudiantes, materias, usuario)
                menu_principal(estudiantes, materias, notas, usuario)
            case 4:
                menu_estadisticas(notas, estudiantes, materias)
                menu_principal(estudiantes, materias, notas, usuario)
            case 5:
                print("Saliste del programa.")


def principal():
    '''
    pre: no recibe parámetros.
    pos: inicializa los datos del sistema, realiza el inicio de sesión
         y, si las credenciales son válidas, inicia el menú principal.
    '''

    '''
    pre: No recibe parámetros.
    pos: Inicializa las matrices de estudiantes, materias y notas, llama a la función de login, valida los intentos de inicio de sesión y, si se loguea correctamente dentro de los intentos, llama a la función para mostrar el menú principal del programa.
    '''
    # Matriz estudiantes: legajo, nombre, edad, año de cursada, nombre de usuario
    matriz_estudiantes = [
    [100, "Ares Alfini", 18, 2, "aalfini"],
    [101, "Lucas Jaldin", 19, 3, "ljaldin"],
    [102, "Marcos Ratt", 18, 1, "mratt"],
    [103, "Diomid Petrenko", 22, 2, "dpetrenko"],
    [104, "Valentino Lazzari", 18, 1, "vlazzari"]
    ]

    encabezados = ("legajo", "nombre", "edad", "año cursada", "usuario")

    # Convierte la matriz de estudiantes en una lista de diccionarios utilizando los encabezados como claves
    estudiantes = [dict(zip(encabezados, fila)) for fila in matriz_estudiantes]

    # Matriz materias: id, nombre, cuatrimestre, año, carga horaria
    materias = [
    [100, "Programación", 2, 2, 6],
    [101, "Álgebra", 2, 2, 4],
    [102, "Sistemas de Información", 1, 1, 6],
    [103, "Química", 2, 2, 4],
    [104, "Inglés", 1, 3, 3]
    ]     

    # Matriz notas: id nota, nota, legajo estudiante, id materia, condicion: 1(aprobado), 2(promocionada), 3(desaprobado)
    notas = [
    [100, 8, 100, 101, 2],
    [101, 6, 101, 101, 1],
    [102, 7, 102, 104, 1],
    [103, 3, 103, 103, 3],
    [104, 9, 104, 102, 2]
    ]

    cont = 4 #Cantidad de intentos de login
    lgin = login(usuarios, contrasenias)

    while cont > 0 and lgin == -1:
        print(f"{ROJO}Usuario o contraseña inválidos. Intentos restantes: {cont}{RESET}")
        lgin = login(usuarios, contrasenias)
        cont -= 1

    if lgin != -1:
        menu_principal(estudiantes, materias, notas, lgin)
    else:
        print("Intentos superados, vuelva a intentar más tarde")


principal()