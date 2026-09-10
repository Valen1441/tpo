import re
#------------------------ ESTUDIANTES ---------------------
def busqueda_secuencial(matriz, columna, dato):
    i = 0
    while i < len(matriz) and matriz[i][columna] != dato:
        i += 1
    if i < len(matriz):
        return i
    else:
        return -1

def obtener_lista_legajos(estudiantes):
    lista_legajos = []
    for i in estudiantes:
        lista_legajos.append(i["legajo"])
    return lista_legajos

#------------------ ALTAS ESTUDIANTES ---------------------
def altas_estudiantes(estudiantes):
    print()
    print(f" == ALTAS ESTUDIANTES ==")

    #Pedir nombre del estudiante
    nombre = input("Ingrese el nombre y apellido del nuevo estudiante: ").title()

    if len(nombre.split()) != 2:
        print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
        nombre = input("Ingrese otra vez el nombre y apellido del nuevo estudiante: ").title()

    nombre = nombre.split()
    nombre = nombre[0] + " " + nombre[1]
    
    
    #Pedir edad
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


    #Pedir año de cursada
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


    #Nombre de usuario
    usuario = nombre.split()
    cont = 1
    numero = 0
    for i in range(len(estudiantes)):
        if re.search(nombre, estudiantes[i]["nombre"], re.IGNORECASE):
            if cont < len(usuario[0]):
                cont += 1
            else: 
                numero += 1
    if numero == 0:
        usuario = (usuario[0][:cont] + usuario[1]).lower()
    else:
        usuario = (usuario[0][:cont] + usuario[1] + str(numero)).lower()


    legajo = estudiantes[len(estudiantes) - 1]["legajo"] + 1

    #Agregar
    estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "edad": edad,
        "año cursada": anio,
        "usuario": usuario
    }

    estudiantes.append(estudiante)

    print(f"{VERDE}Estudiante {legajo} agreagado.{RESET}")
    

#------------------ BAJAS ESTUDIANTES ---------------------
def bajas_estudiantes(estudiantes, notas):
    print()
    print(f" == BAJAS ESTUDIANTES ==")

    lista_legajos = obtener_lista_legajos(estudiantes)

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


    indice = lista_legajos.index(legajo)
    estudiantes.pop(indice)
    lista_legajos.pop(indice)
    
    print(f"{NARANJA}Estudiante {legajo} eliminado.{RESET}")
    

#------------------ MODIFICACION ESTUDIANTES ---------------------
def modificar_estudiantes(estudiantes):
    print()
    print(f" == MODIFICACIÓN ESTUDIANTES ==")

    lista_legajos = obtener_lista_legajos(estudiantes)
    
    #Pedir el legajo a modificar
    legajo = input("Ingrese el legajo del estudiante a modificar (Formato: 100): ")

    while legajo.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        legajo = input("Ingrese de nuevo el legajo del estudiante a modificar (Formato: 100): ")

    legajo = int(legajo)


    while legajo not in lista_legajos:
        print(f"{ROJO}ERROR: Ese legajo no está registrado{RESET}")

        colegajodigo = input("Ingrese de nuevo el legajo del estudiante a modificar (Formato: 100): ")

        while legajo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el legajo.{RESET}")
            legajo = input("Ingrese de nuevo el legajo del estudiante a modificar (Formato: 100): ")

        legajo = int(legajo)

                
                
#Pedir nombre del estudiante
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


    #Pedir año de cursada
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


    #Nombre de usuario
    usuario = nombre.split()
    cont = 1
    numero = 0
    for i in range(len(estudiantes)):
        if re.search(nombre, estudiantes[i]["legajo"], re.IGNORECASE):
            if cont < len(usuario[0]):
                cont += 1
            else: 
                numero += 1
    if numero == 0:
        usuario = (usuario[0][:cont] + usuario[1]).lower()
    else:
        usuario = (usuario[0][:cont] + usuario[1] + str(numero)).lower()

        

    #Modificar
    indice = lista_legajos.index(legajo)
    estudiantes[indice]["id"] = legajo
    estudiantes[indice]["nombre"] = nombre
    estudiantes[indice]["edad"] = edad
    estudiantes[indice]["año cursada"] = anio
    estudiantes[indice]["usuario"] = usuario

    print(f"{AZUL}Estudiante {legajo} modificado.{RESET}")
           

#------------------ MOSTRAR ESTUDIANTES ---------------------   
def imprimir_estudiantes(estudiantes):

    print("="*82)
    print(f'{BOLD}{MAGENTA}{"ESTUDIANTES":^82}{RESET}')
    print("="*82)
    print(f"{BOLD}{'Legajo':<13}{'Nombre':<17}{'Edad':^18}{'Año Cursada':^13}{"Usuario":>19}{RESET}")
    print("-" * 82)

    # Datos
    for i in range(len(estudiantes)):
        legajo = estudiantes[i]["legajo"]

        nombre = estudiantes[i]["nombre"]
        if len(nombre) > 15:
            nombre = nombre[:12] + "..."

        edad = estudiantes[i]["edad"]
        anio = estudiantes[i]["año cursada"]

        usuario = estudiantes[i]["usuario"]
        if len(usuario) > 15:
            usuario = usuario[:12] + "..."

        print(f"{legajo:<13}{nombre:<17}{edad:^18}{anio:^13}{usuario:>19}")


def ordenar_estudiantes(estudiantes, columna, reversa):
    dict_keys = list(estudiantes[0].keys())
    clave = dict_keys[columna]

    if reversa == 0: 
        estudiantes.sort(key=lambda fila: fila[clave])
    else:
        estudiantes.sort(key=lambda fila: fila[clave], reverse=True)



def mostrar_estudiantes(estudiantes):
    columna = input("Ingrese el número de la columna para ordenar (1-4): ")

    while columna.isnumeric() == False:
        print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 4{RESET}")
        columna = input("Ingrese el número de la columna para ordenar (1-4): ")
    columna = int(columna) - 1

    while columna < 0 or columna > 3:
        print(f"{ROJO}Número inválido, la matriz posee 4 columnas{RESET}")
        columna = input("Ingrese de nuevo el número de la columna para ordenar (1-4): ")

        while columna.isnumeric() == False:
            print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 4{RESET}")
            columna = input("Ingrese el número de la columna para ordenar (1-4): ")
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



# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"