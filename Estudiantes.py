import re
import utilidades

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"


#------------------------ ESTUDIANTES ---------------------

#------------------ ALTAS ESTUDIANTES ---------------------
def altas_estudiantes(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: solicita y valida los datos de un nuevo estudiante y lo agrega un diccionario
         y luego a la lista de estudiantes.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS ESTUDIANTES{RESET} ====================")

    # Pedir nombre del estudiante
    nombre = input("Ingrese el nombre y apellido del nuevo estudiante: ").title()

    while len(nombre.split()) != 2:
        print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
        nombre = input("Ingrese otra vez el nombre y apellido del nuevo estudiante: ").title()

    nombre = nombre.split()
    nombre = nombre[0] + " " + nombre[1]
    
    
    # Pedir edad
    while True:
        try:
            edad = utilidades.leerentero("Ingrese la edad del nuevo estudiante: ")
            assert edad >= 17 and edad <= 100
            break
        except AssertionError:
            print(f"{ROJO}Edad invalida: rango perimitido de 17 a 100 años{RESET}")
            print("Intente nuevamente.")


    # Pedir año de cursada
    while True:
        try:
            anio = utilidades.leerentero("Ingrese el año de cursada del nuevo estudiante (1-9): ")
            assert anio > 0 and anio < 10
            break
        except AssertionError:
            print(f"{ROJO}Año de cursada invalido: rango perimitido de 1 a 9{RESET}")
            print("Intente nuevamente.")


    # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
    usuario = nombre.split()
    nombre_usuario = usuario[0]
    apellido_usuario = usuario[1]
    cont = 1
    numero = 0
    primera_letra = nombre_usuario[0]
    for i in range(len(estudiantes)):
        alumno = estudiantes[i]["nombre"].split()
        if re.search(f"^{nombre}$", estudiantes[i]["nombre"], re.IGNORECASE):
            # Si re repite el nombre entre los estudiantes se suma una letra del nombre al usuario
            if cont < len(usuario[0]):
                cont += 1
            # Si se completó el nombre se le suma un número al usuario 
            else: 
                numero += 1
        elif re.search(f"^{primera_letra}", alumno[0], re.IGNORECASE) and re.search(f"^{apellido_usuario}$", alumno[1], re.IGNORECASE):
            # Si re repite el apellido y la primera letra entre los estudiantes se suma un número al usuario
                numero += 1
    if numero == 0:
        usuario = (nombre_usuario[:cont] + apellido_usuario).lower()
    else:
        usuario = (nombre_usuario[:cont] + apellido_usuario + str(numero)).lower()


    # Genera el legajo del nuevo estudiante tomando el último legajo y sumando 1.
    if len(estudiantes) > 0:
        legajo = estudiantes[len(estudiantes) - 1]["legajo"] + 1
    else:
        legajo = 100

    # Agrega el nuevo estudiante a un diccionario diccionario.
    estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "edad": edad,
        "año cursada": anio,
        "usuario": usuario
    }

    # Agrega el diccionario a la lista de estudiantes
    estudiantes.append(estudiante)

    print(f"{VERDE}Estudiante {legajo} agreagado.{RESET}")
    

#------------------ BAJAS ESTUDIANTES ---------------------
def bajas_estudiantes(estudiantes, notas):
    '''
    pre: recibe la lista de diccionarios de estudiantes y la matriz de notas.
    pos: solicita un legajo y elimina el estudiante si existe y no tiene calificaciones registradas.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS ESTUDIANTES{RESET} ====================")

    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)

    # Pedir legajo a eliminar
    while True:
        try:
            legajo = utilidades.leerentero("Ingrese el legajo del estudiante a eliminar (Formato: 100): ")
            esta_en_calificaciones = utilidades.busqueda_secuencial(notas, 2, legajo)
            assert legajo in lista_legajos
            assert esta_en_calificaciones == -1
            break
        except AssertionError:
            if legajo not in lista_legajos:
                print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            else:
                print(f"{ROJO}ERROR: Ese estudiante tiene una calificaión registrada, no se puede eliminar{RESET}")
            print("Intente nuevamente.")


    # Busca el indice del legajo en la lista de legajos y lo elimina de la misma y elimina el diccionario a la lista de estudiantes
    indice = lista_legajos.index(legajo)
    estudiantes.pop(indice)
    lista_legajos.pop(indice)
    
    print(f"{NARANJA}Estudiante {legajo} eliminado.{RESET}")
    

#------------------ MODIFICACION ESTUDIANTES ---------------------
def modificar_estudiantes(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: solicita el legajo de un estudiante y modifica sus datos validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN ESTUDIANTES{RESET} ====================")

    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)
    
    # Pedir el legajo a modificar
    while True:
        try:
            legajo = utilidades.leerentero("Ingrese el legajo del estudiante a modificar (Formato: 100): ")
            assert legajo in lista_legajos
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese legajo no está registrado{RESET}")
            print("Intente nuevamente.")

                             
    # Pedir nombre del estudiante
    nombre = input("Ingrese el nombre y apellido del estudiante: ").title()

    while len(nombre.split()) != 2:
        print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
        nombre = input("Ingrese otra vez el nombre y apellido del estudiante: ").title()

    nombre = nombre.split()
    nombre = nombre[0] + " " + nombre[1]
    
    
    #Pedir edad
    while True:
        try:
            edad = utilidades.leerentero("Ingrese la edad del nuevo estudiante: ")
            assert edad > 17 and edad < 100
            break
        except AssertionError:
            print(f"{ROJO}Edad invalida: rango perimitido de 17 a 100 años{RESET}")
            print("Intente nuevamente.")

    # Pedir año de cursada
    while True:
        try:
            anio = utilidades.leerentero("Ingrese el año de cursada del nuevo estudiante (1-9): ")
            assert anio > 0 and anio < 10
            break
        except AssertionError:
            print(f"{ROJO}Año de cursada invalido: rango perimitido de 1 a 9{RESET}")
            print("Intente nuevamente.")


    # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
    usuario = nombre.split()
    nombre_usuario = usuario[0]
    apellido_usuario = usuario[1]
    cont = 1
    numero = 0
    primera_letra = nombre_usuario[0]
    for i in range(len(estudiantes)):
        alumno = estudiantes[i]["nombre"].split()
        if re.search(f"^{nombre}$", estudiantes[i]["nombre"], re.IGNORECASE):
            # Si re repite el nombre entre los estudiantes se suma una letra del nombre al usuario
            if cont < len(usuario[0]):
                cont += 1
            # Si se completó el nombre se le suma un número al usuario 
            else: 
                numero += 1
        elif re.search(f"^{primera_letra}", alumno[0], re.IGNORECASE) and re.search(f"^{apellido_usuario}$", alumno[1], re.IGNORECASE):
            # Si re repite el apellido y la primera letra entre los estudiantes se suma un número al usuario
                numero += 1
    if numero == 0:
        usuario = (nombre_usuario[:cont] + apellido_usuario).lower()
    else:
        usuario = (nombre_usuario[:cont] + apellido_usuario + str(numero)).lower()
 

    # Modifica los datos del estudiante seleccionado.
    indice = lista_legajos.index(legajo)
    estudiantes[indice]["legajo"] = legajo
    estudiantes[indice]["nombre"] = nombre
    estudiantes[indice]["edad"] = edad
    estudiantes[indice]["año cursada"] = anio
    estudiantes[indice]["usuario"] = usuario

    print(f"{AZUL}Estudiante {legajo} modificado.{RESET}")
           

#------------------ MOSTRAR ESTUDIANTES ---------------------   
def imprimir_estudiantes(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: muestra por pantalla los datos de todos los estudiantes en formato de tabla.
    '''
    print("="*82)
    print(f'{BOLD}{MAGENTA}{"ESTUDIANTES":^82}{RESET}')
    print("="*82)
    print(f"{BOLD}{'Legajo':<13}{'Nombre':<17}{'Edad':^18}{'Año Cursada':^13}{'Usuario':>19}{RESET}")
    print("-" * 82)

    # Recorre los estudiantes para mostrar sus datos.
    for i in range(len(estudiantes)):
        legajo = estudiantes[i]["legajo"]

        nombre = estudiantes[i]["nombre"]
        # Si el nombre tiene mas de 15 caracteres se corta en el 12 y se le agregan "..."
        if len(nombre) > 15:
            nombre = nombre[:12] + "..."

        edad = estudiantes[i]["edad"]
        anio = estudiantes[i]["año cursada"]

        usuario = estudiantes[i]["usuario"]
        # Si el usuario tiene mas de 15 caracteres se corta en el 12 y se le agregan "..."
        if len(usuario) > 15:
            usuario = usuario[:12] + "..."

        print(f"{legajo:<13}{nombre:<17}{edad:^18}{anio:^13}{usuario:>19}")


def ordenar_estudiantes(estudiantes, columna, reversa):
    '''
    pre: recibe la lista de diccionarios de estudiantes, el número de columna por la cual ordenar y un indicador de orden.
    pos: ordena los estudiantes por la clave correspondiente, de forma ascendente o descendente.
    '''
    # Obtiene las claves del diccionario para relacionarlas con la columna elegida.
    dict_keys = list(estudiantes[0].keys())
    clave = dict_keys[columna]

    if reversa == 0: 
        estudiantes_ordenados = sorted(estudiantes, key=lambda fila: fila[clave])
    else:
        estudiantes_ordenados = sorted(estudiantes, key=lambda fila: fila[clave], reverse=True)
    return estudiantes_ordenados


def mostrar_estudiantes(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: solicita la columna y el tipo de orden, ordena los estudiantes y los muestra por pantalla.
    '''

    while True:
        try:
            columna = utilidades.leerentero("""Ingrese el número de la columna para ordenar 
(1 = legajo, 2 = nombre, 3 = edad, 4 = año de cursada, 5 = usuario): """) - 1
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

    
    estudiantes_ordenados = ordenar_estudiantes(estudiantes, columna, reversa)
    imprimir_estudiantes(estudiantes_ordenados)