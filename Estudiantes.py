import re

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"


#------------------------ ESTUDIANTES ---------------------
def busqueda_secuencial(matriz, columna, dato):
    '''
    pre: recibe una matriz, el número de columna donde buscar y el dato a buscar.
    pos: devuelve la posición de la fila donde se encuentra el dato o -1 si no lo encuentra.
    '''
    i = 0
    while i < len(matriz) and matriz[i][columna] != dato:
        i += 1
    if i < len(matriz):
        return i
    else:
        return -1

def obtener_lista_legajos(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: devuelve una lista con los legajos de todos los estudiantes.
    '''
    lista_legajos = []
    for i in estudiantes:
        lista_legajos.append(i["legajo"])
    return lista_legajos

#------------------ ALTAS ESTUDIANTES ---------------------
def altas_estudiantes(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: solicita y valida los datos de un nuevo estudiante y lo agrega un diccionario
         y luego a la lista de estudiantes.
    '''
    print()
    print(f" == ALTAS ESTUDIANTES ==")

    # Pedir nombre del estudiante
    nombre = input("Ingrese el nombre y apellido del nuevo estudiante: ").title()

    if len(nombre.split()) != 2:
        print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
        nombre = input("Ingrese otra vez el nombre y apellido del nuevo estudiante: ").title()

    nombre = nombre.split()
    nombre = nombre[0] + " " + nombre[1]
    
    
    # Pedir edad
    edad = input("Ingrese la edad del nuevo estudiante: ")

    while edad.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        edad = input("Ingrese otra vez la edad del nuevo estudiante: ")
    edad = int(edad)

    while edad < 17 or edad > 100:
        print(f"{ROJO}Edad invalida: rango perimitido de 17 a 100 años{RESET}")
        edad = input("Ingrese otra vez la edad del nuevo estudiante: ")

        while edad.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            edad = input("Ingrese otra vez la edad del nuevo estudiante: ")
        edad = int(edad)


    # Pedir año de cursada
    anio = input("Ingrese el año de cursada del nuevo estudiante (1-9): ")

    while anio.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        anio = input("Ingrese otra vez el año de cursada del nuevo estudiante (1-9): ")
    anio = int(anio)

    while anio < 1 or anio > 9:
        print(f"{ROJO}Año de cursada invalido: rango perimitido de 1 a 9{RESET}")
        anio = input("Ingrese otra vez el año de cursada del nuevo estudiante (1-9): ")

        while anio.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            anio = input("Ingrese otra vez el año de cursada del nuevo estudiante (1-9): ")
        anio = int(anio)


    # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
    usuario = nombre.split()
    cont = 1
    numero = 0
    for i in range(len(estudiantes)):
        if re.search(nombre, estudiantes[i]["nombre"], re.IGNORECASE):
            # Si re repite el nombre entre los estudiantes se suma una letra del nombre al usuario
            if cont < len(usuario[0]):
                cont += 1
            # Si se completó el nombre se le suma un número al usuario 
            else: 
                numero += 1
    if numero == 0:
        usuario = (usuario[0][:cont] + usuario[1]).lower()
    else:
        usuario = (usuario[0][:cont] + usuario[1] + str(numero)).lower()


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
    print(f" == BAJAS ESTUDIANTES ==")

    lista_legajos = obtener_lista_legajos(estudiantes)

    # Pedir legajo a eliminar
    legajo = input("Ingrese el legajo del estudiante a eliminar (Formato: 100): ")

    while legajo.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        legajo = input("Ingrese de nuevo el legajo del estudiante a eliminar (Formato: 100): ")

    legajo = int(legajo)
    esta_en_calificaciones = busqueda_secuencial(notas, 2, legajo)


    while legajo not in lista_legajos == -1 or esta_en_calificaciones != -1:
        if legajo not in lista_legajos:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
        else:
            print(f"{ROJO}ERROR: Ese estudiante tiene una calificaión registrada, no se puede eliminar{RESET}")
        

        legajo = input("Ingrese el legajo del estudiante a eliminar (Formato: 100): ")

        while legajo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            legajo = input("Ingrese de nuevo el legajo del estudiante a eliminar (Formato: 100): ")

        legajo = int(legajo)
        esta_en_calificaciones = busqueda_secuencial(notas, 2, legajo)


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
    print(f" == MODIFICACIÓN ESTUDIANTES ==")

    lista_legajos = obtener_lista_legajos(estudiantes)
    
    # Pedir el legajo a modificar
    legajo = input("Ingrese el legajo del estudiante a modificar (Formato: 100): ")

    while legajo.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        legajo = input("Ingrese de nuevo el legajo del estudiante a modificar (Formato: 100): ")

    legajo = int(legajo)


    while legajo not in lista_legajos:
        print(f"{ROJO}ERROR: Ese legajo no está registrado{RESET}")

        legajo = input("Ingrese de nuevo el legajo del estudiante a modificar (Formato: 100): ")

        while legajo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el legajo.{RESET}")
            legajo = input("Ingrese de nuevo el legajo del estudiante a modificar (Formato: 100): ")

        legajo = int(legajo)

                
                
    # Pedir nombre del estudiante
    nombre = input("Ingrese el nombre y apellido del estudiante: ").title()

    if len(nombre.split()) != 2:
        print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
        nombre = input("Ingrese otra vez el nombre y apellido del estudiante: ").title()

    nombre = nombre.split()
    nombre = nombre[0] + " " + nombre[1]
    
    
    #Pedir edad
    edad = input("Ingrese la edad del estudiante: ")

    while edad.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        edad = input("Ingrese de nuevo la edad del estudiante: ")
    edad = int(edad)
    
    while edad < 17 or edad > 100:
        print(f"{ROJO}Edad invalida: rango perimitido de 17 a 100 años{RESET}")
        edad = input("Ingrese de nuevo la edad del estudiante: ")

        while edad.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            edad = input("Ingrese de nuevo la edad del estudiante: ")
        edad = int(edad)


    # Pedir año de cursada
    anio = input("Ingrese el año de cursada del estudiante (1-9): ")

    while anio.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        anio = input("Ingrese de nuevo el año de cursada del estudiante (1-9): ")
    anio = int(anio)

    while anio < 1 or anio > 9:
        print(f"{ROJO}Año de cursada invalido: rango perimitido de 1 a 9{RESET}")
        anio = input("Ingrese de nuevo el año de cursada del estudiante (1-9): ")

        while anio.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            anio = input("Ingrese de nuevo el año de cursada del estudiante (1-9): ")
        anio = int(anio)


    # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
    usuario = nombre.split()
    cont = 1
    numero = 0
    for i in range(len(estudiantes)):
        if re.search(nombre, estudiantes[i]["nombre"], re.IGNORECASE):
            # Si re repite el nombre entre los estudiantes se suma una letra del nombre al usuario
            if cont < len(usuario[0]):
                cont += 1
            # Si se completó el nombre se le suma un número al usuario 
            else: 
                numero += 1
    if numero == 0:
        usuario = (usuario[0][:cont] + usuario[1]).lower()
    else:
        usuario = (usuario[0][:cont] + usuario[1] + str(numero)).lower()
 

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

    '''
    pre: Recibe una lista de estudiantes.
    pos: Imprime los datos de todos los estudiantes en una tabla modificada con el codigo ANSI.
    '''

    print("="*82)
    print(f'{BOLD}{MAGENTA}{"ESTUDIANTES":^82}{RESET}')
    print("="*82)
    print(f"{BOLD}{'Legajo':<13}{'Nombre':<17}{'Edad':^18}{'Año Cursada':^13}{"Usuario":>19}{RESET}")
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
        estudiantes.sort(key=lambda fila: fila[clave])
    else:
        estudiantes.sort(key=lambda fila: fila[clave], reverse=True)



def mostrar_estudiantes(estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: solicita la columna y el tipo de orden, ordena los estudiantes y los muestra por pantalla.
    '''
    columna = input("Ingrese el número de la columna para ordenar (1-5): ")

    while columna.isnumeric() == False:
        print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 5{RESET}")
        columna = input("Ingrese el número de la columna para ordenar (1-5): ")
    columna = int(columna) - 1

    while columna < 0 or columna > 4:
        print(f"{ROJO}Número inválido, la matriz posee 5 columnas{RESET}")
        columna = input("Ingrese de nuevo el número de la columna para ordenar (1-5): ")

        while columna.isnumeric() == False:
            print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 5{RESET}")
            columna = input("Ingrese el número de la columna para ordenar (1-5): ")
        columna = int(columna) - 1

    
    reversa = input("Ingrese 0 = ascendente, 1 = descendente: ")

    while reversa.isnumeric() == False:
        print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 2{RESET}")
        reversa = input("Ingrese 0 = ascendente, 1 = descendente: ")
    reversa = int(reversa)
    
    while reversa < 0 or reversa > 1:
        print(f"{ROJO}Número inválido, rango valido de 0 a 1{RESET}")
        reversa = input("Ingrese 0 = ascendente, 1 = descendente: ")

        while reversa.isnumeric() == False:
            print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 2{RESET}")
            reversa = input("Ingrese 0 = ascendente, 1 = descendente: ")
        reversa = int(reversa)

    
    ordenar_estudiantes(estudiantes, columna, reversa)
    imprimir_estudiantes(estudiantes)