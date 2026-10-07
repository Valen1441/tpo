import utilidades

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"


#------------------------ MATERIAS ---------------------

#------------------ ALTAS MATERIAS ---------------------
def altas_materias(materias):
    '''
    pre: recibe la matriz de materias.
    pos: agrega una nueva materia a la matriz con un código,
         nombre, cuatrimestre, año y carga horaria válidos.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS MATERIAS{RESET} ====================")

    # Pedir nombre
    nombre = input("Ingrese el nombre de la nueva materia: ").title()

    
    # Pedir cuatrimestre
    while True:
        try:
            cuatrimestre = utilidades.leerentero("Ingrese el cuatrimestre de la nueva materia (1-2): ")
            assert cuatrimestre >= 1 and cuatrimestre <= 2
            break
        except AssertionError:
            print(f"{ROJO}Cuatimestre invalido: rango perimitido de 1 a 2{RESET}")
            print("Intente nuevamente.")


    # Pedir año de la materia
    while True:
        try:
            anio = utilidades.leerentero("Ingrese el año de la nueva materia (1-5): ")
            assert anio >= 1 and anio <= 5
            break
        except AssertionError:
            print(f"{ROJO}Año inválido: rango perimitido de 1 a 5 años{RESET}")
            print("Intente nuevamente.")


    # Pedir carga horaria 
    while True:
        try:
            horaria = utilidades.leerentero("Ingrese la carga horaria de la nueva materia (1-12): ")
            assert horaria >= 1 and horaria <= 12
            break
        except AssertionError:
            print(f"{ROJO}Carga horaria invalida: rango perimitido de 1 a 12 horas{RESET}")
            print("Intente nuevamente.")


    # Genera el código de la nueva materia tomando el último código y sumando 1.
    if len(materias) > 0:
        codigo = materias[len(materias) - 1][0] + 1
    else:
        codigo = 100

    # Agregar la nueva materia a la matriz.
    materias.append([codigo, nombre, cuatrimestre, anio, horaria])

    print(f"{VERDE}Materia {codigo} agreagada.{RESET}")
    

#------------------ BAJAS MATERIAS ---------------------
def bajas_materias(materias, notas):
    '''
    pre: recibe la matriz de materias y la de notas.
    pos: solicita el código de una materia y elimina el registro correspondiente, 
         siempre que exista y no tenga una calificación registrada.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS MATERIAS{RESET} ====================")

    # Pedir el código a eliminar
    while True:
        try:
            codigo = utilidades.leerentero("Ingrese el código de la materia a eliminar (Formato: 100): ")
            esta_en_calificaciones = utilidades.busqueda_secuencial(notas, 3, codigo)
            registrado = utilidades.busqueda_secuencial(materias, 0, codigo)
            assert esta_en_calificaciones == -1
            assert registrado != -1
            break
        except AssertionError:
            if registrado == -1:
                print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            else:
                print(f"{ROJO}ERROR: Esa materia tiene una calificaión registrada, no se puede eliminar{RESET}")
            print("Intente nuevamente.")


    # Elimina la materia de la matriz. 
    materias.pop(registrado)
    
    print(f"{NARANJA}Materia {codigo} eliminada.{RESET}")
    

#------------------ MODIFICACION MATERIAS ---------------------
def modificar_materias(materias):
    '''
    pre: recibe la matriz de materias.
    pos: solicita una materia existente y modifica sus datos, validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN MATERIAS{RESET} ====================")
    
    # Pedir el codigo a modificar
    while True:
        try:
            codigo = utilidades.leerentero("Ingrese el código de la materia a modificar (Formato: 100): ")
            modificar = utilidades.busqueda_secuencial(materias, 0, codigo)
            assert modificar != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")

                
    # Pedir nombre de la materia
    nombre = input("Ingrese el nombre de la materia: ").title()
    
    
    # Pedir el cuatrimestre
    while True:
        try:
            cuatrimestre = utilidades.leerentero("Ingrese el cuatrimestre de la nueva materia (1-2): ")
            assert cuatrimestre >= 1 and cuatrimestre <= 2
            break
        except AssertionError:
            print(f"{ROJO}Cuatimestre invalido: rango perimitido de 1 a 2{RESET}")
            print("Intente nuevamente.")


    # Pedir año de la materia
    while True:
        try:
            anio = utilidades.leerentero("Ingrese el año de la nueva materia (1-5): ")
            assert anio >= 1 and anio <= 5
            break
        except AssertionError:
            print(f"{ROJO}Año inválido: rango perimitido de 1 a 5 años{RESET}")
            print("Intente nuevamente.")


    # Pedir carga horaria 
    while True:
        try:
            horaria = utilidades.leerentero("Ingrese la carga horaria de la nueva materia (1-12): ")
            assert horaria >= 1 and horaria <= 12
            break
        except AssertionError:
            print(f"{ROJO}Carga horaria invalida: rango perimitido de 1 a 12 horas{RESET}")
            print("Intente nuevamente.")

    
    # Modificar los datos de la materia seleccionada.
    materias[modificar][0] = codigo
    materias[modificar][1] = nombre
    materias[modificar][2] = cuatrimestre
    materias[modificar][3] = anio
    materias[modificar][4] = horaria

    print(f"{AZUL}Materia {codigo} modificada.{RESET}")
        
        

#------------------ MOSTRAR MATERIAS ---------------------   
def imprimir_materias(materias):
    '''
    pre: recibe la matriz de materias.
    pos: muestra en pantalla todas las materias de la matriz, mostrando su código, nombre, cuatrimestre, año y carga horaria.
         El formato del código mostrado se modifica temporalmente para indicar el año y el cuatrimestre.
    '''
    print("="*82)
    print(f'{BOLD}{MAGENTA}{"MATERIAS":^82}{RESET}')
    print("="*82)
    print(f"{BOLD}{'Id Materia':<16}{'Nombre':<21}{'Cuatrimestre':^12}{'Año':^17}{'Carga Horaria':^13}{RESET}")
    print("-" * 82)

    # Se guardan los códigos originales para restaurarlos después.
    codigos = [fila[0] for fila in materias]

    # Se genera temporalmente un código con el año y el cuatrimestre.
    lista_codigo = list(map(lambda fila: str(fila[3]) + "Pri" + str(fila[0]) if fila[2] == 1 else str(fila[3]) + "Seg" + str(fila[0]), materias))
    for fila in range(len(materias)):
        materias[fila][0] = lista_codigo[fila]

    # Mostrar los datos de cada materia.
    for i in range(len(materias)):
        codigo = materias[i][0]

        nombre = materias[i][1]
        if len(nombre) > 15:
            nombre = nombre[:12] + "..."

        cuatrimestre = materias[i][2]
        anio = materias[i][3]

        horaria = materias[i][4]

        print(f"{codigo:<16}{nombre:<21}{cuatrimestre:^12}{anio:^17}{horaria:^13}")

    # Se restauran los códigos originales para no modificar la matriz.
    for fila in range(len(materias)):
        materias[fila][0] = codigos[fila]


def ordenar_materias(materias, columna, reversa):
    '''
    pre: recibe una matriz, el número de columna por la cual ordenar y un indicador de orden.
    pos: ordena la matriz por la columna indicada, de forma ascendente o descendente.
    '''
    if reversa == 0: 
        materias_ordenadas = sorted(materias, key=lambda fila: fila[columna])
    else:
        materias_ordenadas = sorted(materias, key=lambda fila: fila[columna], reverse=True)
    return materias_ordenadas


def mostrar_materias(materias):
    '''
    pre: recibe la matriz de materias.
    pos: solicita al usuario una columna y un tipo de ordenamiento,
         ordena la matriz según los datos ingresados y muestra las materias.
    '''

    while True:
        try:
            columna = utilidades.leerentero("""Ingrese el número de la columna para ordenar 
(1 = id, 2 = nombre, 3 = cuatrimestre, 4 = año, 5 = carga horaria): """) - 1
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


    materias_ordenadas = ordenar_materias(materias, columna, reversa)
    imprimir_materias(materias_ordenadas)
    