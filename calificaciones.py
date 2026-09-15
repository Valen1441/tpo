# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"


#------------------------ CALIFICACIONES ---------------------
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
    pos: devuelve una lista que contiene los legajos de todos los estudiantes.
    '''
    lista_legajos = []
    for i in estudiantes:
        lista_legajos.append(i["legajo"])
    return lista_legajos

def boletin(estudiantes, estudiante, notas, materias):
    '''
    pre: recibe las listas de estudiantes, notas y materias, y el legajo del estudiante.
    pos: muestra por pantalla el boletín del estudiante con sus materias, notas y resultados.
    '''
    # ==============================
    # REPORTE / BOLETÍN DEL ALUMNO
    # ==============================

    # Buscar nombre del alumno
    lista_legajos = obtener_lista_legajos(estudiantes)
    posicion_estudiante = lista_legajos.index(estudiante)
    nombre_alumno = estudiantes[posicion_estudiante]["nombre"]

    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"BOLETÍN":^40}{RESET}')
    print("=" * 40)
    print(f"Alumno: {nombre_alumno}")
    print(f"Legajo: {estudiante}")
    print("-" * 40)

    for registro in notas:
        if registro[2] == estudiante:

            nota_alumno = registro[1]
            codigo_materia = registro[3]

            # Buscar la materia
            posicion_materia = busqueda_secuencial(materias, 0, codigo_materia)
            nombre_materia = materias[posicion_materia][1]

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

#------------------ ALTAS CALIFICACIONES ---------------------
def altas_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita los datos necesarios, valida la información y agrega una nueva calificación.
    '''
    print()
    print(" == ALTAS CALIFICACIONES ==")

    lista_legajos = obtener_lista_legajos(estudiantes)

    # Pedir legajo del estudiante 
    estudiante = input("Ingrese el legajo del estudiante a calificar (Formato: 100): ")

    while estudiante.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el legajo.{RESET}")
        estudiante = input("Ingrese de nuevo el legajo del estudiante a calificar (Formato: 100): ")
    estudiante = int(estudiante)

            
    while estudiante not in lista_legajos:
        print(f"{ROJO}ERROR: Ese legajo no está registrado.{RESET}")
        
        estudiante = input("Ingrese de nuevo el legajo del estudiante a calificar (Formato: 100): ")

        while estudiante.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el legajo.{RESET}")
            estudiante = input("Ingrese de nuevo el legajo del estudiante a calificar (Formato: 100): ")
        estudiante = int(estudiante)
    
    
    # Pedir id de la materia
    materia = input("Ingrese el código de la materia (Formato: 100): ")

    while materia.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        materia = input("Ingrese de nuevo el código de la materia (Formato: 100): ")
    materia = int(materia)
    
    registrado = busqueda_secuencial(materias, 0, materia)
            
    while registrado == -1:
        print(f"{ROJO}ERROR: Ese código de materia no está registrado.{RESET}")
        
        materia = input("Ingrese de nuevo el código de la materia (Formato: 100): ")

        while materia.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            materia = input("Ingrese de nuevo el código de la materia (Formato: 100): ")
        materia = int(materia)
    
        registrado = busqueda_secuencial(materias, 0, materia)
        
    
    # Pedir la nota
    nota = input("Ingrese la nota: ")

    while nota.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        nota = input("Ingrese de nuevo la nota: ")
    nota = int(nota)

    while nota <= 0 or nota > 10:
        print(f"{ROJO}ERROR: La nota debe ser mayor a 0 y menor o igual a 10.{RESET}")
            
        nota = input("Ingrese de nuevo la nota: ")

        while nota.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            nota = input("Ingrese de nuevo la nota: ")
        nota = int(nota)


    # Genera el código de la nueva calificación tomando el último código y sumando 1.
    if len(notas) > 0:
        codigo = notas[len(notas) - 1][0] + 1
    else: 
        codigo = 100


    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3


    # Agrega la nueva calificación a la matriz.
    notas.append([codigo, nota, estudiante, materia, condicion])

    print(f"{VERDE}Nota {codigo} agreagada.{RESET}")

    boletin(estudiantes, estudiante, notas, materias)
    

#------------------ BAJAS CALIFICACIONES ---------------------
def bajas_calificaciones(notas):
    '''
    pre: recibe la matriz de calificaciones.
    pos: solicita el código de una calificación y elimina el registro correspondiente.
    '''
    print()
    print(" == BAJAS CALIFICACIONES ==")

    # Pedir el codigo a eliminar
    codigo = input("Ingrese el código de la nota a eliminar (Formato: 100): ")

    while codigo.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        codigo = input("Ingrese de nuevo el código de la nota a eliminar (Formato: 100): ")
    codigo = int(codigo)

    registrado = busqueda_secuencial(notas, 0, codigo)

    
    while registrado == -1:
        print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
        
        codigo = input("Ingrese de nuevo el código de la nota a eliminar (Formato: 100): ")

        while codigo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            codigo = input("Ingrese de nuevo el código de la nota a eliminar (Formato: 100): ")
        codigo = int(codigo)
    
        registrado = busqueda_secuencial(notas, 0, codigo)

                    
    # Elimina de la matriz la fila encontrada.
    notas.pop(registrado)
    
    print(f"{NARANJA}Nota {codigo} eliminada.{RESET}")
    

#------------------ MODIFICACION CALIFICACIONES ---------------------
def modificar_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita una calificación existente y modifica sus datos, validando la información ingresada.
    '''
    print()
    print(" == MODIFICACIÓN CALIFICACIONES ==")

    lista_legajos = obtener_lista_legajos(estudiantes)
    
    # Pedir el codigo a modificar
    codigo = input("Ingrese el código de la nota a modificar (Formato: 100): ")

    while codigo.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        codigo = input("Ingrese de nuevo el código de la nota a modificar (Formato: 100): ")
    codigo = int(codigo)
    
    nota_modificar = busqueda_secuencial(notas, 0, codigo)

    while nota_modificar == -1:
        print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
        
        codigo = input("Ingrese de nuevo el código de la nota a modificar (Formato: 100): ")

        while codigo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            codigo = input("Ingrese de nuevo el código de la nota a modificar (Formato: 100): ")
        codigo = int(codigo)
    
        nota_modificar = busqueda_secuencial(notas, 0, codigo)
                
                
    # Pedir el nuevo legajo
    legajo = input("Ingrese el nuevo legajo del estudiante de la nota (Formato: 100): ")

    while legajo.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el legajo.{RESET}")
        legajo = input("Ingrese otra vez el nuevo legajo del estudiante de la nota (Formato: 100): ")
    legajo = int(legajo)


    while legajo not in lista_legajos:
        print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
        
        legajo = input("Ingrese otra vez el nuevo legajo del estudiante de la nota (Formato: 100): ")

        while legajo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el legajo.{RESET}")
            legajo = input("Ingrese otra vez el nuevo legajo del estudiante de la nota (Formato: 100): ")
        legajo = int(legajo)

        
    # Pedir el nuevo codigo de materia
    materia = input("Ingrese el nuevo código de la materia de la nota (Formato: 100): ")

    while materia.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        materia = input("Ingrese otra vez el nuevo código de la materia de la nota (Formato: 100): ")
    materia = int(materia)

    registrado = busqueda_secuencial(materias, 0, materia)

    while registrado == -1:
        print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
        
        materia = input("Ingrese otra vez el nuevo código de la materia de la nota (Formato: 100): ")
        while materia.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            materia = input("Ingrese otra vez el nuevo código de la materia de la nota (Formato: 100): ")
        materia = int(materia)

        registrado = busqueda_secuencial(materias, 0, materia)

    
    # Pedir la nueva nota
    nota = input("Ingrese la nota: ")

    while nota.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        nota = input("Ingrese de nuevo la nota: ")
    nota = int(nota)

    while nota <= 0 or nota > 10:
        print(f"{ROJO}ERROR: La nota debe ser mayor a 0 y menor o igual a 10.{RESET}")
            
        nota = input("Ingrese de nuevo la nota: ")

        while nota.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            nota = input("Ingrese de nuevo la nota: ")
        nota = int(nota)
        

    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3

    # Reemplaza los datos de la calificación seleccionada.
    notas[nota_modificar][0] = codigo
    notas[nota_modificar][1] = nota
    notas[nota_modificar][2] = legajo
    notas[nota_modificar][3] = materia
    notas[nota_modificar][4] = condicion
    
    print(f"{AZUL}Nota {codigo} modificada.{RESET}")
    
    boletin(estudiantes, legajo, notas, materias)
        

#------------------ MOSTRAR CALIFICACIONES ---------------------
def clasificar_nota(nota):
    '''
    pre: recibe una nota numérica.
    pos: devuelve una cadena que indica si la nota es promocionada, aprobada o desaprobada.
    '''
    if nota >= 8:
        cadena = f"{AZUL}Promocionada{RESET}"
    elif nota >= 4:
        cadena = f"{VERDE}Aprobada{RESET}"
    else:
        cadena = f"{ROJO}Desaprobada{RESET}"
    return cadena
    
def imprimir_calificacion(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: muestra por pantalla todas las calificaciones en formato de tabla.
    '''
    # Encabezado
    print("="*80)
    print(f'{BOLD}{MAGENTA}{"CALIFICACIONES":^80}{RESET}')
    print("="*80)
    print(f"{BOLD}{'ID Nota':<7}{'Nota':^16}{'Estudiante':<21}{'Materia':<15}{'Condición':^24}{RESET}")
    print("-" * 80)

    lista_legajos = obtener_lista_legajos(estudiantes)

    # Datos
    for i in range(len(notas)):
        id_nota = notas[i][0]
        nota = notas[i][1]

        estudiante = notas[i][2]
        pos = lista_legajos.index(estudiante)
        estudiante = estudiantes[pos]["nombre"]
        if len(estudiante) > 15:
            estudiante = estudiante[:12] + "..."

        materia = notas[i][3]
        pos = busqueda_secuencial(materias, 0, materia)
        materia = materias[pos][1]
        if len(materia) > 15:
            materia = materia[:12] + "..."
        
        condicion = clasificar_nota(nota)
        print(f"{id_nota:^7}{nota:^16}{estudiante:<21}{materia:<15}{condicion:^36}")

def ordenar_matriz(matriz, columna, reversa):
    '''
    pre: recibe una matriz, el número de columna por la cual ordenar y un indicador de orden.
    pos: ordena la matriz por la columna indicada, de forma ascendente o descendente.
    '''
    if reversa == 0: 
        matriz.sort(key=lambda fila: fila[columna])
    else:
        matriz.sort(key=lambda fila: fila[columna], reverse=True)

def mostrar_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita la columna y el tipo de orden, ordena las calificaciones y las muestra por pantalla.
    '''
    columna = input("Ingrese el número de la columna para ordenar (1-5): ")

    while columna.isnumeric() == False:
        print(f"{ROJO}Opción inválida, ingrese un número entre 1 y 5{RESET}")
        columna = input("Ingrese el número de la columna para ordenar (1-5): ")
    columna = int(columna) - 1

    while columna < 0 or columna > 3:
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


    ordenar_matriz(notas, columna, reversa)
    imprimir_calificacion(notas, estudiantes, materias)