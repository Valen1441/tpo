from calificaciones import altas_calificaciones
from calificaciones import bajas_calificaciones
from calificaciones import modificar_calificaciones

usuario = "Admin"
contrasenia = "123"


def validar_rango(desde, hasta):
    numero = int(input("Ingrese una opción: " ))
    while numero < desde or numero > hasta:
        print("Opción inválida. Ingrese una opcion que se encuentre en el rango")
        numero = int(input("Ingrese de nuevo una opción: "))
    return numero


def login(usuario_almacenado, contraseña_almacenada):
    usuario_login = input("Ingrese un usuario: ")
    contrasena_login = input("Ingrese una contraseña: ")
    return usuario_login == usuario_almacenado and contrasena_login == contraseña_almacenada


#------------------------ Submenu ---------------------
def mostrar_submenu(titulo):
    print("""
    === MENÚ""",titulo,"""===
    1. ALTA
    2. BAJA
    3. MODIFICACIÓN
    4. LISTADO
    5. VOLVER AL MENÚ PRINCIPAL
    """)

#------------------ Menu Calificaciones ---------------------
def menu_calificaciones(notas, estudiantes, materias):
    mostrar_submenu("CALIFICACIONES")
    opcion = validar_rango(1, 5)
    match opcion:
        case 1:
            altas_calificaciones(notas, estudiantes, materias)
            menu_calificaciones(notas, estudiantes, materias)
        case 2:
            bajas_calificaciones(notas, estudiantes, materias)
            menu_calificaciones(notas, estudiantes, materias)
        case 3:
            modificar_calificaciones(notas, estudiantes, materias)
            menu_calificaciones(notas, estudiantes, materias)
        case 4:
            print(notas)
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
            ...
        case 2:
            ...
        case 3:
            menu_calificaciones(notas, estudiantes, materias)
        case 4:
            ...
        case 5:
            print("Saliste del programa.")
 
 
def menu_principal(estudiantes, materias, notas):
    mostrar_menu_principal()
    opcion = validar_rango(1, 5)
    ejecutar_menu_principal(opcion, estudiantes, materias, notas)


def principal():

    # Matriz estudiantes: nombre, legajo, edad, año de cursada
    estudiantes = [
    ["Ares", 100, 18, 2],
    ["Lucas", 101, 19, 3],
    ["Marcos", 102, 18, 1],
    ["Diomid", 103, 22, 2],
    ["Valentino", 104, 18, 1]
    ]

    # Matriz materias: nombre, id, cuatrimestre, carga horaria
    materias = [
        ["Prog.", 100, 2, 6],
        ["Alg.", 101, 2, 4],
        ["Sist. Inf.", 102, 1, 6],
        ["Quim.", 103, 2, 4],
        ["Ingl.", 104, 1, 3]
    ]

    # Matriz notas: id nota, nota, legajo estudiante, id materia, condicion: 1(aprobado), 2(promocionada), 3(desaprobado)
    notas = [
        [100, 8, 103, 101, 2],
        [101, 6, 101, 101, 1],
        [102, 7, 100, 104, 1],
        [103, 3, 103, 103, 3],
        [104, 9, 104, 102, 2]
    ]


    if login(usuario, contrasenia) == True:
        menu_principal(estudiantes, materias, notas)
    else:
        print("Usuario o contraseña inválidos.")


principal()