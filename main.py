import calificaciones
import Estudiantes
import estadisticas
import Materias

usuario = "Admin"
contrasenia = "123"

RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"


def validar_rango(desde, hasta):

    '''
    pre: Recibe dos números enteros, desde y hasta. Solicita al usuario que ingrese un número dentro de ese rango. Valida que el número ingresado sea un número y que se encuentre dentro del rango.
    pos: Devuelve un número ingresado por el usuario que se encuentra dentro del rango desde y hasta.
    '''

    numero = input("Ingrese una opción: " )
    while numero.isnumeric() == False:
        print(f"{ROJO}Opcion inválida. Ingrese un número dentro del rango{RESET}")
        numero = input("Ingrese nuevamente una opción: " )

    numero = int(numero)
    while numero < desde or numero > hasta:
        print(f"{ROJO}Opción inválida. Ingrese una opción que se encuentre en el rango{RESET}")
        numero = input("Ingrese nuevamente una opción: ")
        while numero.isnumeric() == False:
                print(f"{ROJO}Opcion iválida. Ingrese un número dentro del rango{RESET}")
                numero = input("Ingrese nuevamente una opción: " )
        numero = int(numero)
    return numero


def login(usuario_almacenado, contrasenia_almacenada):

    '''
    pre: Recibe un usuario y una contraseña almacenados. Solicita al usuario que ingrese un usuario y una contraseña para iniciar sesión.
    pos: Devuelve True si el usuario y la contraseña ingresados coinciden con los almacenados, False en caso contrario.
    '''

    usuario_login = input("Ingrese un usuario: ")
    contrasena_login = input("Ingrese una contraseña: ")
    return usuario_login == usuario_almacenado and contrasena_login == contrasenia_almacenada


#------------------------ Submenu ---------------------
def mostrar_submenu(titulo):

    '''
    pre: Recibe un título para el menú.
    pos: Muestra un menú con el título proporcionado que contiene el CRUD y una opcion para volver al menú principal.
    '''
    print(f"""
    === MENÚ {titulo} ===
    1. ALTA
    2. BAJA
    3. MODIFICACIÓN
    4. LISTADO
    5. VOLVER AL MENÚ PRINCIPAL
    """)

def mostrar_submenu_estadistica():

    '''
    pre: No recibe parámetros.
    pos: Muestra un menú de estadísticas que contiene opciones para ver estadísticas de materias, estudiantes y una opción para volver al menú principal.
    '''
    print("""
    === MENÚ ESTADÍSTICAS ===
    1. MATERIAS
    2. ESTUDIANTES
    3. VOLVER AL MENÚ PRINCIPAL
    """)

#------------------ Menu Estudiantes ---------------------
def menu_estudiantes(estudiantes, notas):

    '''
    pre: Recibe una lista de estudiantes y una lista de notas.
    pos: Muestra un menú de estudiantes que contiene el CRUD de estudiantes y una opción para volver al menú principal. Dependiendo de la opción seleccionada, llama a la función correspondiente del módulo Estudiantes y luego vuelve a mostrar el menú de estudiantes.
    '''
    mostrar_submenu("ESTUDIANTES")
    opcion = validar_rango(1, 5)
    match opcion:
        case 1:
            Estudiantes.altas_estudiantes(estudiantes)
            menu_estudiantes(estudiantes, notas)
        case 2:
            Estudiantes.bajas_estudiantes(estudiantes, notas)
            menu_estudiantes(estudiantes, notas)
        case 3:
            Estudiantes.modificar_estudiantes(estudiantes)
            menu_estudiantes(estudiantes, notas)
        case 4:
            Estudiantes.mostrar_estudiantes(estudiantes)
            menu_estudiantes(estudiantes, notas)

#------------------ Menu Masterias ---------------------
def menu_materias(materias, notas):

    '''
    pre: Recibe una lista de materias y una lista de notas.
    pos: Muestra un menú de materias que contiene el CRUD de materias y una opción para volver al menú principal. Dependiendo de la opción seleccionada, llama a la función correspondiente del módulo Materias y luego vuelve a mostrar el menú de materias.
    '''
    mostrar_submenu("MATERIAS")
    opcion = validar_rango(1, 5)
    match opcion:
        case 1:
            Materias.altas_materias(materias)
            menu_materias(materias, notas)
        case 2:
            Materias.bajas_materias(materias, notas)
            menu_materias(materias, notas)
        case 3:
            Materias.modificar_materias(materias)
            menu_materias(materias, notas)
        case 4:
            Materias.mostrar_materias(materias)
            menu_materias(materias, notas)

#------------------ Menu Calificaciones ---------------------
def menu_calificaciones(notas, estudiantes, materias):

    '''
    pre: Recibe una lista de notas, una lista de estudiantes y una lista de materias.
    pos: Muestra un menú de calificaciones que contiene el CRUD de calificaciones y una opción para volver al menú principal. Dependiendo de la opción seleccionada, llama a la función correspondiente del módulo calificaciones y luego vuelve a mostrar el menú de calificaciones.
    '''
    mostrar_submenu("CALIFICACIONES")
    opcion = validar_rango(1, 5)
    match opcion:
        case 1:
            calificaciones.altas_calificaciones(notas, estudiantes, materias)
            menu_calificaciones(notas, estudiantes, materias)
        case 2:
            calificaciones.bajas_calificaciones(notas)
            menu_calificaciones(notas, estudiantes, materias)
        case 3:
            calificaciones.modificar_calificaciones(notas, estudiantes, materias)
            menu_calificaciones(notas, estudiantes, materias)
        case 4:
            calificaciones.mostrar_calificaciones(notas, estudiantes, materias)
            menu_calificaciones(notas, estudiantes, materias)

#------------------ Menu Estadisticas ---------------------
def menu_estadisticas(notas, estudiantes, materias):

    '''
    pre: Recibe una lista de notas, una lista de estudiantes y una lista de materias.
    pos: Muestra un menú de estadísticas que contiene opciones para ver estadísticas de materias, estudiantes y una opción para volver al menú principal. Dependiendo de la opción seleccionada, llama a la función correspondiente del módulo estadisticas y luego vuelve a mostrar el menú de estadísticas.
    '''
    mostrar_submenu_estadistica()
    opcion = validar_rango(1, 3)
    match opcion:
        case 1:
            estadisticas.estadisticas_materias(notas, materias)
            menu_estadisticas(notas, estudiantes, materias)
        case 2:
            estadisticas.estadisticas_estudiantes(notas, estudiantes, materias)
            menu_estadisticas(notas, estudiantes, materias)


def mostrar_menu_principal():

    '''
    pre: No recibe parámetros.
    pos: Muestra el menú principal del programa.
    '''

    print("""
    ==== MENÚ PRINCIPAL ====

    1. ESTUDIANTES
    2. MATERIAS
    3. CALIFICACIONES
    4. ESTADISTICAS
    5. SALIR DEL PROGRAMA
    """)
 
 
def ejecutar_menu_principal(eleccion, estudiantes, materias, notas):

    '''
    pre: Recibe una opción elegida por el usuario, una lista de estudiantes, una lista de materias y una lista de notas.
    pos: Dependiendo de la opción elegida, llama a la función correspondiente para mostrar el menú de estudiantes, materias, calificaciones o estadísticas. Si la opción elegida es salir del programa, muestra un mensaje de despedida.
    '''
    match eleccion:
        case 1:
            menu_estudiantes(estudiantes, notas)
            menu_principal(estudiantes, materias, notas)
        case 2:
            menu_materias(materias, notas)
            menu_principal(estudiantes, materias, notas)
        case 3:
            menu_calificaciones(notas, estudiantes, materias)
            menu_principal(estudiantes, materias, notas)
        case 4:
            menu_estadisticas(notas, estudiantes, materias)
            menu_principal(estudiantes, materias, notas)
        case 5:
            print("Saliste del programa.")
 
 
def menu_principal(estudiantes, materias, notas):

    '''
    pre: Recibe una lista de estudiantes, una lista de materias y una lista de notas.
    pos: Muestra el menú principal del programa, llama a la función para validar la opción elegida por el usuario y luego entrega la opción correspondiente para la otra función.
    '''
    mostrar_menu_principal()
    opcion = validar_rango(1, 5)
    ejecutar_menu_principal(opcion, estudiantes, materias, notas)


def principal():

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
    lgin = login(usuario, contrasenia)

    while cont > 0 and lgin == False:
        print(f"{ROJO}Usuario o contraseña inválidos. Intentos restantes: {cont}{RESET}")
        lgin = login(usuario, contrasenia)
        cont -= 1

    if lgin == True:
        menu_principal(estudiantes, materias, notas)
    else:
        print("Intentos superados, vuelva a intentar más tarde")


principal()