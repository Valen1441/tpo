import utilidades
import CRUD_calificaciones
import CRUD_materias
import CRUD_estudiantes
import Estadisticas

usuarios = ("Admin", "Nardone")
contrasenias = ("123", "321")

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

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
        print(f"  {NARANJA}3. RESUMEN GENERAL{RESET}")
        print(f"  {BOLD}4. VOLVER AL MENÚ PRINCIPAL{RESET}")
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
    pre: recibe las rutas de los archivos de estudiantes, de notas
         y de materias y el usuario que utiliza el sistema.
    pos: muestra y ejecuta las opciones del menú de estudiantes según el
         tipo de usuario. Permite realizar altas, bajas, modificaciones
         y listados cuando el usuario es Admin, y consultas si no lo es.
    '''
    if usuario == "Admin":
        opciones = ("ALTA", "BAJA", "MODIFICACION", "LISTADO")
    else:
        opciones = ("LISTADO",)
    salir = len(opciones) + 1

    opcion = 0    
    while opcion != salir:
        mostrar_submenu("ESTUDIANTES", usuario)  
        opcion = utilidades.validar_rango(1, salir)
        if opcion != salir:
            accion = opciones[opcion - 1]
            estudiantes_totales = utilidades.crear_conjunto_json(estudiantes, "legajo")
            if accion != "ALTA" and len(estudiantes_totales) == 0:
                print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}")
            else:
                match accion:
                    case "ALTA":
                        CRUD_estudiantes.altas_estudiantes(estudiantes)
                    case "BAJA":
                        estudiantes_con_notas = utilidades.crear_conjunto_planos(notas, 2)
                        if len(estudiantes_totales ^ estudiantes_con_notas) != 0:
                            CRUD_estudiantes.bajas_estudiantes(estudiantes, notas)
                        else:
                            print(f"{ROJO}ERROR: todos los estudiantes tienen una calificación registrada, no se pueden eliminar.{RESET}")
                    case "MODIFICACION":
                        CRUD_estudiantes.modificar_estudiantes(estudiantes)
                    case "LISTADO":
                        CRUD_estudiantes.mostrar_estudiantes(estudiantes)


#------------------ Menu Masterias ---------------------
def menu_materias(materias, notas, usuario):
    '''
    pre: recibe las rutas de los archivos de materias y de notas y el
         usuario que utiliza el sistema.
    pos: muestra y ejecuta las opciones del menú de materias según el tipo
         de usuario. Permite realizar altas, bajas, modificaciones y
         listados cuando el usuario es Admin, y consultas si no lo es.
    '''
    if usuario == "Admin":
        opciones = ("ALTA", "BAJA", "MODIFICACION", "LISTADO")
    else:
        opciones = ("LISTADO",)
    salir = len(opciones) + 1

    opcion = 0
    while opcion != salir:
        mostrar_submenu("MATERIAS", usuario)
        opcion = utilidades.validar_rango(1, salir)
        if opcion != salir:
            accion = opciones[opcion - 1]
            materias_totales = utilidades.crear_conjunto_planos(materias, 0)
            if accion != "ALTA" and len(materias_totales) == 0:
                print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
            else:
                match opciones[opcion - 1]:
                    case "ALTA":
                        CRUD_materias.altas_materias(materias)
                    case "BAJA":
                        materias_con_notas = utilidades.crear_conjunto_planos(notas, 3)
                        if len(materias_totales ^ materias_con_notas) != 0:     
                            CRUD_materias.bajas_materias(materias, notas)
                        else:
                            print(f"{ROJO}ERROR: todas las materias tienen una calificación registrada, no se pueden eliminar.{RESET}") 
                    case "MODIFICACION":
                        CRUD_materias.modificar_materias(materias)
                    case "LISTADO":
                        CRUD_materias.mostrar_materias(materias)


#------------------ Menu Calificaciones ---------------------
def menu_calificaciones(notas, estudiantes, materias, usuario):
    '''
    pre: recibe las rutas de los archivos de notas, de estudiantes y de materias
         y el usuario que utiliza el sistema.
    pos: muestra y ejecuta las opciones del menú de calificaciones según
         el tipo de usuario. Permite realizar altas, bajas, modificaciones y
         listados cuando el usuario es Admin, y altas, modificaciones y listados si no lo es.
    '''
    if usuario == "Admin":
        opciones = ("ALTA", "BAJA", "MODIFICACION", "LISTADO")
    else:
        opciones = ("ALTA", "MODIFICACION", "LISTADO")
    salir = len(opciones) + 1

    opcion = 0
    while opcion != salir:
        mostrar_submenu("CALIFICACIONES", usuario)
        opcion = utilidades.validar_rango(1, salir)
        if opcion != salir:
            accion = opciones[opcion - 1]
            notas_totales = utilidades.crear_conjunto_planos(notas, 0)
            estudiantes_totales = utilidades.crear_conjunto_json(estudiantes, "legajo")
            materias_totales = utilidades.crear_conjunto_planos(materias, 0)
            if accion != "ALTA" and len(notas_totales) == 0:
                print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
            elif accion in ("ALTA", "MODIFICACION") and (len(estudiantes_totales) == 0 or len(materias_totales) == 0):
                print(f"{ROJO}ERROR: no hay estudiantes o materias cargados.{RESET}")
            else:
                match accion:
                    case "ALTA":
                        CRUD_calificaciones.altas_calificaciones(notas, estudiantes, materias)
                    case "BAJA":
                        CRUD_calificaciones.bajas_calificaciones(notas)
                    case "MODIFICACION":
                        CRUD_calificaciones.modificar_calificaciones(notas, estudiantes, materias)
                    case "LISTADO":
                        CRUD_calificaciones.mostrar_calificaciones(notas, estudiantes, materias)


#------------------ Menu Estadisticas ---------------------
def menu_estadisticas(notas, estudiantes, materias):
    '''
    pre: recibe las rutas de los archivos de notas, de estudiantes y de materias.
    pos: muestra y ejecuta las opciones disponibles del menú de estadísticas.
    '''
    opcion = 0
    while opcion != 4:
        mostrar_submenu_estadistica()
        opcion = utilidades.validar_rango(1, 4)
        match opcion:
            case 1:
                estadisticas_estudiantes_materias(notas, estudiantes, materias, "MATERIAS")
            case 2:
                estadisticas_estudiantes_materias(notas, estudiantes, materias, "ESTUDIANTES")
            case 3:
                if len(utilidades.crear_conjunto_planos(notas, 0)) == 0:
                    print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
                else:
                    Estadisticas.resumen_general(notas)


def estadisticas_estudiantes_materias(notas, estudiantes, materias, titulo):
    '''
    pre: recibe las rutas de los archivos de notas, de estudiantes y de materias, 
         y el título que indica si se trabaja sobre estudiantes o sobre materias.
    pos: muestra y ejecuta las opciones del submenú de estadísticas generales o particulares
         correspondiente al título recibido.
    '''
    opcion = 0
    while opcion != 3:
        mostrar_submenu_estadistica(titulo)
        opcion = utilidades.validar_rango(1, 3)
        if opcion != 3:
            notas_totales = utilidades.crear_conjunto_planos(notas, 0)
            estudiantes_totales = utilidades.crear_conjunto_json(estudiantes, "legajo")
            materias_totales = utilidades.crear_conjunto_planos(materias, 0)
            if len(notas_totales) == 0:
                print(f"{ROJO}ERROR: no hay calificaciones cargadas.{RESET}")
            elif (titulo == "ESTUDIANTES" or opcion == 2) and len(estudiantes_totales) == 0:
                print(f"{ROJO}ERROR: no hay estudiantes cargados.{RESET}")
            elif (titulo == "MATERIAS" or opcion == 2) and len(materias_totales) == 0:
                print(f"{ROJO}ERROR: no hay materias cargadas.{RESET}")
            else:
                match opcion:
                    case 1:
                        if titulo == "ESTUDIANTES":
                            Estadisticas.estadisticas_estudiantes(notas, estudiantes)
                        else:
                            Estadisticas.estadisticas_materias(notas, materias)
                    case 2:
                        Estadisticas.estadisticas_particulares(notas, estudiantes, materias, titulo)

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
 
 
def menu_principal(usuario):
    '''
    pre: recibe el usuario que esta utilizando el programa.
    pos: muestra el menú principal, solicita una opción válida y ejecuta la función correspondiente 
         a la opción seleccionada con sus respectivas rutas de los archivos.
    '''
    notas = r'notas.txt'
    materias = r'materias.txt'
    estudiantes = r'estudiantes.json'
    
    opcion = 0
    while opcion != 5:
        mostrar_menu_principal()
        opcion = utilidades.validar_rango(1, 5)
        match opcion:
            case 1:
                menu_estudiantes(estudiantes, notas, usuario)
            case 2:
                menu_materias(materias, notas, usuario)
            case 3:
                menu_calificaciones(notas, estudiantes, materias, usuario)
            case 4:
                menu_estadisticas(notas, estudiantes, materias)
            case 5:
                print("Saliste del programa.")


def principal():
    '''
    pre: no recibe parámetros.
    pos: realiza el inicio de sesión y, si las credenciales son válidas, inicia el menú principal.
    '''

    cont = 4 #Cantidad de intentos de login
    lgin = login(usuarios, contrasenias)

    while cont > 0 and lgin == -1:
        print(f"{ROJO}Usuario o contraseña inválidos. Intentos restantes: {cont}{RESET}")
        lgin = login(usuarios, contrasenias)
        cont -= 1

    if lgin != -1:
        menu_principal(lgin)
    else:
        print("Intentos superados, vuelva a intentar más tarde")


principal()