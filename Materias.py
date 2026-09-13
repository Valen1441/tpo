
#------------------------ MATERIAS ---------------------
def busqueda_secuencial(matriz, columna, dato):

    '''
    pre: Recibe una matriz, el índice de una columna y un dato a buscar.
    pos: Retorna el índice de la fila donde se encuentra el dato en la columna especificada, o -1 si no se encuentra.
    '''
    i = 0
    while i < len(matriz) and matriz[i][columna] != dato:
        i += 1
    if i < len(matriz):
        return i
    else:
        return -1

#------------------ ALTAS MATERIAS ---------------------
def altas_materias(materias):

    '''
    pre: Recibe una lista de materias.
    pos: Solicita los datos de una nueva materia al usuario, valida los datos ingresados y agrega la nueva materia a la lista de materias.
    '''
    print()
    print(f" == ALTAS MATERIAS ==")

    #Pedir nombre
    nombre = input("Ingrese el nombre de la nueva materia: ").title()

    
    #Pedir cuatrimestre
    cuatrimestre = input("Ingrese el cuatrimestre de la nueva materia (1-2): ")

    while cuatrimestre.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        cuatrimestre = input("Ingrese otra vez el cuatrimestre de la nueva materia (1-2): ")
    cuatrimestre = int(cuatrimestre)

    while cuatrimestre < 1 or cuatrimestre > 2:
        print(f"{ROJO}Cuatimestre invalido: rango perimitido de 1 a 2{RESET}")
        cuatrimestre = input("Ingrese otra vez el cuatrimestre de la nueva materia (1-2): ")

        while cuatrimestre.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            cuatrimestre = input("Ingrese otra vez el cuatrimestre de la nueva materia (1-2): ")
        cuatrimestre = int(cuatrimestre)


    #Pedir año de la materia
    anio = input("Ingrese el año de la nueva materia (1-5): ")

    while anio.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        anio = input("Ingrese otra vez el año de la nueva materia (1-5): ")
    anio = int(anio)

    while anio < 1 or anio > 5:
        print(f"{ROJO}Año inválido: rango perimitido de 1 a 5 años{RESET}")
        anio = input("Ingrese otra vez el año de la nueva materia (1-5): ")

        while anio.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            anio = input("Ingrese otra vez el año de la nueva materia (1-5): ")
        anio = int(anio)


    #Pedir carga horaria 
    horaria = input("Ingrese la carga horaria de la nueva materia (1-12): ")

    while horaria.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        horaria = input("Ingrese otra vez la carga horaria de la nueva materia (1-12): ")
    horaria = int(horaria)

    while horaria < 1 or horaria > 12:
        print(f"{ROJO}Carga horaria invalida: rango perimitido de 1 a 12 horas{RESET}")
        horaria = input("Ingrese otra vez la carga horaria de la nueva materia (1-12): ")

        while horaria.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            horaria = input("Ingrese otra vez la carga horaria de la nueva materia (1-12): ")
        horaria = int(horaria)


    codigo = materias[len(materias) - 1][0] + 1

    #Agregar
    materias.append([codigo, nombre, cuatrimestre, anio, horaria])

    print(f"{VERDE}Materia {codigo} agreagada.{RESET}")
    

#------------------ BAJAS MATERIAS ---------------------
def bajas_materias(materias, notas):

    '''
    pre: Recibe una lista de materias y una lista de notas.
    pos: Solicita al usuario el código de la materia a eliminar, valida que el código esté registrado y que no tenga calificaciones asociadas, y elimina la materia de la lista de materias.
    '''
    print()
    print(f" == BAJAS MATERIAS ==")


    codigo = input("Ingrese el código de la materia a eliminar (Formato: 100): ")

    while codigo.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        codigo = input("Ingrese de nuevo el código de la materia a eliminar (Formato: 100): ")

    codigo = int(codigo)
    esta_en_calificaciones = busqueda_secuencial(notas, 3, codigo)

    registrado = busqueda_secuencial(materias, 0, codigo)

    while registrado == -1 or esta_en_calificaciones != -1:
        if registrado == -1:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
        else:
            print(f"{ROJO}ERROR: Esa materia tiene una calificaión registrada, no se puede eliminar{RESET}")


        codigo = input("Ingrese el código de la materia a eliminar (Formato: 100): ")

        while codigo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            codigo = input("Ingrese de nuevo el código de la materia a eliminar (Formato: 100): ")

        codigo = int(codigo)
        esta_en_calificaciones = busqueda_secuencial(notas, 3, codigo)

        registrado = busqueda_secuencial(materias, 0, codigo)

                    
    materias.pop(registrado)
    
    print(f"{NARANJA}Materia {codigo} eliminada.{RESET}")
    

#------------------ MODIFICACION MATERIAS ---------------------
def modificar_materias(materias):

    '''
    pre: Recibe una lista de materias.
    pos: Solicita al usuario el código de la materia a modificar, valida que el código esté registrado, solicita los nuevos datos de la materia y actualiza la información en la lista de materias.
    '''
    print()
    print(f" == MODIFICACIÓN MATERIAS ==")
    
    #Pedir el codigo a modificar
    codigo = input("Ingrese el código de la materia a modificar (Formato: 100): ")

    while codigo.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
        codigo = input("Ingrese de nuevo el código de la materia a modificar (Formato: 100): ")

    codigo = int(codigo)

    modificar = busqueda_secuencial(materias, 0, codigo)

    while modificar == -1:
        print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")

        codigo = input("Ingrese de nuevo el código de la materia a modificar (Formato: 100): ")

        while codigo.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            codigo = input("Ingrese de nuevo el código de la materia a modificar (Formato: 100): ")

        codigo = int(codigo)

        modificar = busqueda_secuencial(materias, 0, codigo)
                
                
#Pedir nombre de la materia
    nombre = input("Ingrese el nombre de la materia: ").title()
    
    
#Pedir cuatrimestre
    cuatrimestre = input("Ingrese el cuatrimestre de la materia (1-2): ")

    while cuatrimestre.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        cuatrimestre = input("Ingrese de nuevo el cuatrimestre de la materia (1-2): ")
    cuatrimestre = int(cuatrimestre)

    while cuatrimestre < 1 or cuatrimestre > 2:
        print(f"{ROJO}Cuatimestre invalido: rango perimitido de 1 a 2{RESET}")
        cuatrimestre = input("Ingrese de nuevo el cuatrimestre de la materia (1-2): ")

        while cuatrimestre.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            cuatrimestre = input("Ingrese de nuevo el cuatrimestre de la materia (1-2): ")
        cuatrimestre = int(cuatrimestre)


    #Pedir año de la materia
    anio = input("Ingrese el año de la materia (1-5): ")

    while anio.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        anio = input("Ingrese de nuevo el año de la materia (1-5): ")
    anio = int(anio)

    while anio < 1 or anio > 5:
        print(f"{ROJO}Año invalido: rango perimitido de 1 a 5 años{RESET}")
        anio = input("Ingrese de nuevo el año de la materia (1-5): ")

        while anio.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            anio = input("Ingrese de nuevo el año de la materia (1-5): ")
        anio = int(anio)


    #Pedir carga horaria 
    horaria = input("Ingrese la carga horaria de la materia (1-12): ")

    while horaria.isnumeric() == False:
        print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
        horaria = input("Ingrese otra vez la carga horaria de la materia (1-12): ")
    horaria = int(horaria)

    while horaria < 1 or horaria > 12:
        print(f"{ROJO}Carga horaria invalida: rango perimitido de 1 a 12 horas{RESET}")
        horaria = input("Ingrese otra vez la carga horaria de la materia (1-12): ")

        while horaria.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras.{RESET}")
            horaria = input("Ingrese otra vez la carga horaria de la materia (1-12): ")
        horaria = int(horaria)

        

    #Modificar
    materias[modificar][0] = codigo
    materias[modificar][1] = nombre
    materias[modificar][2] = cuatrimestre
    materias[modificar][3] = anio
    materias[modificar][4] = horaria

    print(f"{AZUL}Materia {codigo} modificada.{RESET}")
        
        

#------------------ MOSTRAR MATERIAS ---------------------   
def imprimir_materias(materias):

    '''
    pre: Recibe una lista de materias.
    pos: Imprime en pantalla la lista de materias con sus respectivos datos, incluyendo un código único generado a partir del año y cuatrimestre de la materia.
    '''

    print("="*82)
    print(f'{BOLD}{MAGENTA}{"MATERIAS":^82}{RESET}')
    print("="*82)
    print(f"{BOLD}{'Id Materia':<16}{'Nombre':<21}{'Cuatrimestre':^12}{"Año":^17}{'Carga Horaria':^13}{RESET}")
    print("-" * 82)

    codigos = [fila[0] for fila in materias]
    lista_codigo = list(map(lambda fila: str(fila[3]) + "Pri" + str(fila[0]) if fila[2] == 1 else str(fila[3]) + "Seg" + str(fila[0]), materias))
    for fila in range(len(materias)):
        materias[fila][0] = lista_codigo[fila]

    # Datos
    for i in range(len(materias)):
        codigo = materias[i][0]

        nombre = materias[i][1]
        if len(nombre) > 15:
            nombre = nombre[:12] + "..."

        cuatrimestre = materias[i][2]
        anio = materias[i][3]

        horaria = materias[i][4]

        print(f"{codigo:<16}{nombre:<21}{cuatrimestre:^12}{anio:^17}{horaria:^13}")

    for fila in range(len(materias)):
        materias[fila][0] = codigos[fila]

def ordenar_materias(materias, columna, reversa):

    '''
    pre: Recibe una lista de materias, el índice de una columna y un valor que indica si se debe ordenar en orden ascendente o descendente.
    pos: Ordena la lista de materias según la columna especificada y el orden indicado.
    '''
    if reversa == 0: 
        materias.sort(key=lambda fila: fila[columna])
    else:
        materias.sort(key=lambda fila: fila[columna], reverse=True)



def mostrar_materias(materias):

    '''
    pre: Recibe una lista de materias.
    pos: Solicita al usuario el número de la columna por la cual desea ordenar la lista de materias y el orden (ascendente o descendente), luego llama a la función para ordenar la lista y finalmente imprime la lista de materias ordenada.
    '''
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

    ordenar_materias(materias, columna, reversa)
    imprimir_materias(materias)



# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"