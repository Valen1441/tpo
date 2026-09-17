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
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"
CELESTE = "\033[36;1m"


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
    pre: recibe las tuplas de usuarios y contraseñas almacenados.
    pos: solicita usuario y contraseña y devuelve el nombre de usuario ingresado 
         si coincide con un par usuario-contraseña almacenado, o -1 si no coincide.
    '''
    usuario_login = input("Ingrese un usuario: ")
    contrasena_login = input("Ingrese una contraseña: ")
    inicio = False
    for i in range(len(usuarios_almacenados)):
        if usuarios_almacenados[i] == usuario_login and contrasenias_almacenadas[i] == contrasena_login:
            inicio = True
    if inicio: 
        return usuario_login
    else:
        return -1

#------------------------ Submenu ---------------------
def mostrar_submenu(titulo, usuario):
    '''
    pre: recibe el título del menú que se desea mostrar y el usuario que
         está utilizando el sistema.
    pos: muestra por pantalla el submenú correspondiente. Las opciones disponibles 
         dependen del tipo de usuario y del menú seleccionado.
    '''
    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"MENÚ " + titulo:^40}{RESET}')
    print("=" * 40)

    if usuario == "Admin":
        print(f"  {VERDE}1. ALTA{RESET}")
        print(f"  {NARANJA}2. BAJA{RESET}")
        print(f"  {AZUL}3. MODIFICACIÓN{RESET}")
        print(f"  {MAGENTA}4. LISTADO{RESET}")
        print(f"  {BOLD}5. VOLVER AL MENÚ PRINCIPAL{RESET}")
    else:
        if titulo == "CALIFICACIONES":
            print(f"  {VERDE}1. ALTA{RESET}")
            print(f"  {AZUL}2. MODIFICACIÓN{RESET}")
            print(f"  {MAGENTA}3. LISTADO{RESET}")
            print(f"  {BOLD}4. VOLVER AL MENÚ PRINCIPAL{RESET}")
        else:
            print(f"  {MAGENTA}1. LISTADO{RESET}")
            print(f"  {BOLD}2. VOLVER AL MENÚ PRINCIPAL{RESET}")

    print("=" * 40)
        

def mostrar_submenu_estadistica(titulo="ESTADÍSTICAS"):
    '''
    pre: recibe opcionalmente el título del submenú de estadísticas. 
         Si no se recibe un título, utiliza "ESTADÍSTICAS" por defecto.
    pos: muestra por pantalla el submenú de estadísticas generales o 
         particulares según el título recibido.
    '''
    print()
    print("=" * 40)

    if titulo == "ESTADÍSTICAS":
        print(f'{BOLD}{MAGENTA}{"MENÚ ESTADÍSTICAS":^40}{RESET}')
        print("=" * 40)
        print(f"  {AZUL}1. MATERIAS{RESET}")
        print(f"  {VERDE}2. ESTUDIANTES{RESET}")
        print(f"  {BOLD}3. VOLVER AL MENÚ PRINCIPAL{RESET}")
    else:
        print(f'{BOLD}{MAGENTA}{"ESTADÍSTICAS " + titulo:^40}{RESET}')
        print("=" * 40)
        print(f"  {VERDE}1. GENERALES{RESET}")
        print(f"  {CELESTE}2. PARTICULARES{RESET}")
        print(f"  {BOLD}3. VOLVER AL MENÚ ESTADÍSTICAS{RESET}")

    print("=" * 40)

#------------------ Menu Estudiantes ---------------------
def menu_estudiantes(estudiantes, notas, usuario):
    '''
    pre: recibe una lista de diccionarios de estudiantes, una matriz de
         calificaciones y el usuario que utiliza el sistema.
    pos: muestra y ejecuta las opciones del menú de estudiantes según el
         tipo de usuario. Permite realizar altas, bajas, modificaciones
         y listados cuando el usuario es Admin, y consultas si no lo es.
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
        match opcion:
            case 1:
                Estudiantes.altas_estudiantes(estudiantes)
                menu_estudiantes(estudiantes, notas, usuario)
            case 2:
                if len(estudiantes) > 0:
                    if len(estudiantes_totales ^ estudiantes_con_notas) != 0:
                        Estudiantes.bajas_estudiantes(estudiantes, notas)
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
    pre: recibe una matriz de materias, una matriz de calificaciones y el
         usuario que utiliza el sistema.
    pos: muestra y ejecuta las opciones del menú de materias según el tipo
         de usuario. Permite realizar altas, bajas, modificaciones y
         listados cuando el usuario es Admin, y consultas si no lo es.
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
                        Materias.bajas_materias(materias, notas)
                    else:
                        print(f"{ROJO}ERROR: todas las materias tienen una calificación registrada, no se pueden eliminar.{RESET}") 
                else:
                    print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
                menu_materias(materias, notas, usuario)
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
    pre: recibe una matriz de calificaciones, una lista de diccionarios de
         estudiantes, una matriz de materias y el usuario que utiliza el sistema.
    pos: muestra y ejecuta las opciones del menú de calificaciones según
         el tipo de usuario. Permite realizar altas, bajas, modificaciones y
         listados cuando el usuario es Admin, y altas, modificaciones y listados si no lo es.
    '''
    mostrar_submenu("CALIFICACIONES", usuario)
    if usuario == "Admin": 
        opcion = validar_rango(1, 5)
        match opcion:
            case 1:
                if len(estudiantes) > 0 and len(materias) > 0:
                    calificaciones.altas_calificaciones(notas, estudiantes, materias)
                    menu_calificaciones(notas, estudiantes, materias, usuario)
                else:
                    if len(materias) == 0:
                        print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
                    else:
                        print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}") 
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
                if len(estudiantes) > 0 and len(materias) > 0:
                    calificaciones.altas_calificaciones(notas, estudiantes, materias)
                    menu_calificaciones(notas, estudiantes, materias, usuario)
                else:
                    if len(materias) == 0:
                        print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
                    else:
                        print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}") 
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
    '''
    pre: recibe las matrices de calificaciones, estudiantes y materias, y el título que indica
         si se trabaja sobre estudiantes o sobre materias.
    pos: muestra y ejecuta las opciones del submenú de estadísticas generales o particulares
         correspondiente al título recibido.
    '''
    mostrar_submenu_estadistica(titulo)
    opcion = validar_rango(1, 3)
    match opcion:
        case 1:
            if titulo == "ESTUDIANTES":
                estadisticas.estadisticas_estudiantes(notas, estudiantes)
            else:
                estadisticas.estadisticas_materias(notas, materias)
            estadisticas_estudiantes_materias(notas, estudiantes, materias, titulo)
        case 2:
            if titulo == "ESTUDIANTES":
                if len(materias) > 0:
                    estadisticas.estadisticas_particulares(notas, estudiantes, materias, titulo)
                else:
                    print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
            else:
                if len(estudiantes) > 0:
                    estadisticas.estadisticas_particulares(notas, estudiantes, materias, titulo)
                else:
                    print(f"{ROJO}ERROR: no hay estudiantes cargadas.{RESET}")
            estadisticas_estudiantes_materias(notas, estudiantes, materias, titulo)


def mostrar_menu_principal():
    '''
    pre: no recibe parámetros.
    pos: muestra por pantalla el menú principal del programa.
    '''
    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"MENÚ PRINCIPAL":^40}{RESET}')
    print("=" * 40)
    print(f"  1. ESTUDIANTES")
    print(f"  2. MATERIAS")
    print(f"  3. CALIFICACIONES")
    print(f"  4. ESTADÍSTICAS")
    print(f"  {ROJO}5. SALIR DEL PROGRAMA{RESET}")
    print("=" * 40)
 
 
def menu_principal(estudiantes, materias, notas, usuario):
    '''
    pre: recibe el diccionario de estudiantes, las matrices de 
         materias y calificaciones y el usuario.
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