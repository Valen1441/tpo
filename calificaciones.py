#------------------------ CALIFICACIONES ---------------------
def busqueda_secuencial(matriz, columna, dato):

    '''
    pre: Recibe una matriz, un índice de columna y un dato a buscar.
    pos: Devuelve el índice de la fila donde se encuentra el dato en la columna especificada, o -1 si no se encuentra.
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
    pre: Recibe una lista de estudiantes.
    pos: Devuelve una lista con los legajos de todos los estudiantes.
    '''

    lista_legajos = []
    for i in estudiantes:
        lista_legajos.append(i["legajo"])
    return lista_legajos

def boletin(estudiantes, estudiante, notas, materias):

    '''
    pre: Recibe una lista de estudiantes, un legajo de estudiante, una lista de notas y una lista de materias.
    pos: Imprime en pantalla el boletín del estudiante especificado, mostrando las materias cursadas, las notas obtenidas y la condición de cada materia (aprobada, promocionada o desaprobada).
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
    pre: Recibe una lista de notas, una lista de estudiantes y una lista de materias.
    pos: Solicita al usuario el legajo del estudiante, el código de la materia y la nota obtenida, valida los datos ingresados y agrega la calificación a la lista de notas.
    '''

    print()
    print(" == ALTAS CALIFICACIONES ==")

    lista_legajos = obtener_lista_legajos(estudiantes)

    #Pedir legajo del estudiante 
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
    
    
    #Pedir id de la materia
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
        
    
    #Pedir la nota
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

        
    codigo = notas[len(notas) - 1][0] + 1
    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3


    #Agregar
    notas.append([codigo, nota, estudiante, materia, condicion])

    print(f"{VERDE}Nota {codigo} agreagada.{RESET}")

    boletin(estudiantes, estudiante, notas, materias)
    

#------------------ BAJAS CALIFICACIONES ---------------------
def bajas_calificaciones(notas):

    '''
    pre: Recibe una lista de notas.
    pos: Solicita al usuario el código de la nota a eliminar, valida que el código esté registrado y elimina la calificación de la lista de notas.
    '''

    print()
    print(" == BAJAS CALIFICACIONES ==")
    
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
                    
    #Eliminar
    notas.pop(registrado)
    
    print(f"{NARANJA}Nota {codigo} eliminada.{RESET}")
    

#------------------ MODIFICACION CALIFICACIONES ---------------------
def modificar_calificaciones(notas, estudiantes, materias):

    '''
    pre: Recibe una lista de notas, una lista de estudiantes y una lista de materias.
    pos: Solicita al usuario el código de la nota a modificar, valida que el código esté registrado, solicita los nuevos datos de la nota y actualiza la información en la lista de notas.
    '''

    print()
    print(" == MODIFICACIÓN CALIFICACIONES ==")

    lista_legajos = obtener_lista_legajos(estudiantes)
    
    #Pedir el codigo a modificar
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
                
                
    #Pedir el nuevo legajo
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

        
    #Pedir el nuevo codigo de materia
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

    
    #Pedir la nueva nota
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

    #Modificar
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
    pre: Recibe una nota.
    pos: Devuelve una cadena de texto que indica si la nota es promocionada, aprobada o desaprobada, utilizando códigos de color ANSI.
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
    pre: Recibe una lista de notas, una lista de estudiantes y una lista de materias.
    pos: Imprime en pantalla la lista de calificaciones con sus respectivos datos, incluyendo el nombre del estudiante y de la materia, y la condición de la nota (aprobada, promocionada o desaprobada) utilizando códigos de color ANSI.
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
    pre: Recibe una matriz, un índice de columna y un valor que indica si se debe ordenar en orden ascendente o descendente.
    pos: Ordena la matriz según la columna especificada y el orden indicado.
    '''

    if reversa == 0: 
        matriz.sort(key=lambda fila: fila[columna])
    else:
        matriz.sort(key=lambda fila: fila[columna], reverse=True)

def mostrar_calificaciones(notas, estudiantes, materias):

    '''
    pre: Recibe una lista de notas, una lista de estudiantes y una lista de materias.
    pos: Solicita al usuario el número de la columna por la cual desea ordenar la lista de calificaciones y el orden (ascendente o descendente), luego llama a la función para ordenar la lista y finalmente imprime la lista de calificaciones ordenada.
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


# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"