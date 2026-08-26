import calificaciones
import estudiantes_materias

usuario = "Admin"
contrasenia = "123"

RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"


def validar_rango(desde, hasta):
    numero = input("Ingrese una opción: " )
    while numero.isnumeric() == False:
        print(f"{ROJO}Opcion iválida. Ingrese un número dentro del ragno{RESET}")
        numero = input("Ingrese de nuevo una opción: " )

    numero = int(numero)
    while numero < desde or numero > hasta:
        print(f"{ROJO}Opción inválida. Ingrese una opcion que se encuentre en el rango{RESET}")
        numero = input("Ingrese de nuevo una opción: ")
        while numero.isnumeric() == False:
                print(f"{ROJO}Opcion iválida. Ingrese un número dentro del ragno{RESET}")
                numero = input("Ingrese de nuevo una opción: " )
        numero = int(numero)
    return numero


def login(usuario_almacenado, contrasenia_almacenada):
    usuario_login = input("Ingrese un usuario: ")
    contrasena_login = input("Ingrese una contraseña: ")
    return usuario_login == usuario_almacenado and contrasena_login == contrasenia_almacenada


#------------------------ Submenu ---------------------
def mostrar_submenu(titulo):
    print(f"""
    === MENÚ {titulo} ===
    1. ALTA
    2. BAJA
    3. MODIFICACIÓN
    4. LISTADO
    5. VOLVER AL MENÚ PRINCIPAL
    """)

#------------------ Menu Estudiantes ---------------------
def menu_estudiantes(estudiantes, notas):
    mostrar_submenu("ESTUDIANTES")
    opcion = validar_rango(1, 5)
    match opcion:
        case 1:
            estudiantes_materias.altas_estudiantes_materias(estudiantes, "ESTUDIANTES")
            menu_estudiantes(estudiantes, notas)
        case 2:
            estudiantes_materias.bajas_estudiantes_materias(estudiantes, notas, "ESTUDIANTES")
            menu_estudiantes(estudiantes, notas)
        case 3:
            estudiantes_materias.modificar_estudiantes_materias(estudiantes, "ESTUDIANTES")
            menu_estudiantes(estudiantes, notas)
        case 4:
            estudiantes_materias.mostrar_estudiantes_materias(estudiantes, "ESTUDIANTES")
            menu_estudiantes(estudiantes, notas)

#------------------ Menu Materias ---------------------
def menu_materias(materias, notas):
    mostrar_submenu("MATERIAS")
    opcion = validar_rango(1, 5)
    match opcion:
        case 1:
            estudiantes_materias.altas_estudiantes_materias(materias, "MATERIAS")
            menu_materias(materias, notas)
        case 2:
            estudiantes_materias.bajas_estudiantes_materias(materias, notas, "MATERIAS")
            menu_materias(materias, notas)
        case 3:
            estudiantes_materias.modificar_estudiantes_materias(materias, "MATERIAS")
            menu_materias(materias, notas)
        case 4:
            estudiantes_materias.mostrar_estudiantes_materias(materias, "MATERIAS")
            menu_materias(materias, notas)

#------------------ Menu Calificaciones ---------------------
def menu_calificaciones(notas, estudiantes, materias):
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


def mostrar_menu_principal():
    print("""
    ==== MENÚ PRINCIPAL ====

    1. ESTUDIANTES
    2. MATERIAS
    3. CALIFICACIONES
    4. ESTADISTICAS
    5. SALIR DEL PROGRAMA
    """)
 
 
def ejecutar_menu_principal(eleccion, estudiantes, materias, notas):
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
            ...
        case 5:
            print("Saliste del programa.")
 
 
def menu_principal(estudiantes, materias, notas):
    mostrar_menu_principal()
    opcion = validar_rango(1, 5)
    ejecutar_menu_principal(opcion, estudiantes, materias, notas)


def principal():

    # Matriz estudiantes: legajo, nombre, edad, año de cursada
    estudiantes = [
    [100, "Ares", 18, 2],
    [101, "Lucas", 19, 3],
    [102, "Marcos", 18, 1],
    [103, "Diomid", 22, 2],
    [104, "Valentino", 18, 1]
    ]

    # Matriz materias: id, nombre, cuatrimestre, carga horaria
    materias = [
    [100, "Prog.", 2, 6],
    [101, "Alg.", 2, 4],
    [102, "Sist. Inf.", 1, 6],
    [103, "Quim.", 2, 4],
    [104, "Ingl.", 1, 3]
    ]

    # Matriz notas: id nota, nota, legajo estudiante, id materia, condicion: 1(aprobado), 2(promocionada), 3(desaprobado)
    notas = [
    [100, 8, 103, 101, 2],
    [101, 6, 101, 101, 1],
    [102, 7, 102, 104, 1],
    [103, 3, 103, 103, 3],
    [104, 9, 104, 102, 2]
    ]

    cont = 1
    lgin = login(usuario, contrasenia)
    while cont < 5 and lgin == False:
        print(f"{ROJO}Usuario o contraseña inválidos. Intento: {cont}/5{RESET}")
        lgin = login(usuario, contrasenia)
        cont += 1

    if cont <= 5:
        menu_principal(estudiantes, materias, notas)
    else:
        print("Intentos superados, vuelva a intentar más tarde")


principal()