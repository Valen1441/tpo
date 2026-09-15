from functools import reduce
import re

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"

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

def estadisticas_materias(notas, materias):
    '''
    pre: recibe la matriz de notas y la matriz de materias.
    pos: muestra por pantalla las estadísticas de cada materia, incluyendo la cantidad de notas, 
         el promedio y la cantidad de alumnos aprobados, promocionados y desaprobados.
    '''

    '''
    pre: Recibe una lista de notas y una lista de materias.
    pos: Imprime en pantalla las estadísticas de cada materia, incluyendo la cantidad de notas, el promedio de las notas, la cantidad de aprobados, promocionados y desaprobados.
    '''

    aprueba = f"{VERDE}Aprobados{RESET}"
    promociona = f"{AZUL}Promocionados{RESET}"
    desaprueba = f"{ROJO}Desaprobados{RESET}"

    print("="*102)
    print(f'{BOLD}{MAGENTA}{"ESTADÍSTICAS POR MATERIA":^102}{RESET}')
    print("="*102)
    print(f"{BOLD}{'ID Materia':<15}{'Nombre':<15}{'Notas':^13}{'Promedio':^13}{aprueba:^24}{promociona:^28}{desaprueba:^27}{RESET}")
    print("-" * 102)

    codigos = [fila[0] for fila in materias]
    lista_codigo = list(map(lambda fila: str(fila[3]) + "Pri" + str(fila[0]) if fila[2] == 1 else str(fila[3]) + "Seg" + str(fila[0]), materias))
    for fila in range(len(materias)):
        materias[fila][0] = lista_codigo[fila]

    lista_cuat1 = []
    lista_cuat2 = []
  
    for materia in range(len(materias)):
        id_materia = codigos[materia]
        nombre = materias[materia][1]
        if len(nombre) > 15:
            nombre = nombre[:12] + "..."

        suma = 0
        aprobados = 0
        promocionados = 0
        desaprobados = 0
        promedio = 0

        lista_notas = list(filter(lambda nota: nota[3] == id_materia, notas))
        cantidad = len(lista_notas)

        if cantidad > 0:
            suma = reduce(lambda suma, cal: suma + cal[1], lista_notas, 0)
            aprobados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 1, notas)))
            promocionados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 2, notas)))
            desaprobados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 3, notas)))
            promedio = (lambda a,b: a / b)(suma, cantidad)

        id_materia = materias[materia][0]
        if re.findall(".Pri", id_materia):
            lista_cuat1.append([materias[materia][1], promedio, aprobados + promocionados, desaprobados])
        else:
            lista_cuat2.append([materias[materia][1], promedio, aprobados + promocionados, desaprobados])
        print(f"{id_materia:<15}{nombre:<15}{cantidad:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")


    for fila in range(len(materias)):
        materias[fila][0] = codigos[fila]

    if reduce(lambda suma, fila: suma + fila[2] + fila[3], lista_cuat1, 0) != 0:
        print()
        print(f'{BOLD}{NARANJA}MATERIAS (PRIMER CUATRIMESTRE){RESET}')
        lista_cuat1.sort(key=lambda fila: fila[1])
        mejor_promedio = lista_cuat1[-1]
        lista_empates = list(filter(lambda promedio: promedio[1] == mejor_promedio[1], lista_cuat1))
        cadena = ""
        for promedio in lista_empates:
            cadena = cadena + f"{promedio[0]}, "

        print(f"- Mejor promedio: {cadena[:-2]} ({mejor_promedio[1]})")

        if reduce(lambda suma, fila: suma + fila[2], lista_cuat1, 0) != 0:
            lista_cuat1.sort(key=lambda fila: fila[2])
            mas_aprobados = lista_cuat1[-1]
            lista_empates = list(filter(lambda fila: fila[2] == mas_aprobados[2], lista_cuat1))
            cadena = ""
            for fila in lista_empates:
                cadena = cadena + f"{fila[0]}, "

            print(f"- Más estudiantes aprobados: {cadena[:-2]} ({mas_aprobados[2]})")
        else:
            print(f"- Más estudiantes aprobados: -")

        if reduce(lambda suma, fila: suma + fila[3], lista_cuat1, 0) != 0:
            lista_cuat1.sort(key=lambda fila: fila[3])
            mas_desaprobados = lista_cuat1[-1]
            lista_empates = list(filter(lambda fila: fila[3] == mas_desaprobados[3], lista_cuat1))
            cadena = ""
            for fila in lista_empates:
                cadena = cadena + f"{fila[0]}, "

            print(f"- Más estudiantes desaprobados: {cadena[:-2]} ({mas_desaprobados[3]})")
        else:
            print(f"- Más estudiantes deaprobados: -")
            

    if reduce(lambda suma, fila: suma + fila[2] + fila[3], lista_cuat2, 0) != 0:
        print()
        print(f'{BOLD}{NARANJA}MATERIAS (SEGUNDO CUATRIMESTRE){RESET}')
        lista_cuat2.sort(key=lambda fila: fila[1])
        mejor_promedio = lista_cuat2[-1]
        lista_empates = list(filter(lambda promedio: promedio[1] == mejor_promedio[1], lista_cuat2))
        cadena = ""
        for promedio in lista_empates:
            cadena = cadena + f"{promedio[0]}, "

        print(f"- Mejor promedio: {cadena[:-2]} ({mejor_promedio[1]})")

        if reduce(lambda suma, fila: suma + fila[2], lista_cuat2, 0) != 0:
            lista_cuat2.sort(key=lambda fila: fila[2])
            mas_aprobados = lista_cuat2[-1]
            lista_empates = list(filter(lambda fila: fila[2] == mas_aprobados[2], lista_cuat2))
            cadena = ""
            for fila in lista_empates:
                cadena = cadena + f"{fila[0]}, "

            print(f"- Más estudiantes aprobados: {cadena[:-2]} ({mas_aprobados[2]})")
        else:
            print(f"- Más estudiantes aprobados: -")

        if reduce(lambda suma, fila: suma + fila[3], lista_cuat2, 0) != 0:
            lista_cuat2.sort(key=lambda fila: fila[3])
            mas_desaprobados = lista_cuat2[-1]
            lista_empates = list(filter(lambda fila: fila[3] == mas_desaprobados[3], lista_cuat2))
            cadena = ""
            for fila in lista_empates:
                cadena = cadena + f"{fila[0]}, "

            print(f"- Más estudiantes desaprobados: {cadena[:-2]} ({mas_desaprobados[3]})")
        else:
            print(f"- Más estudiantes deaprobados: -")


def estadisticas_estudiantes_generales(notas, estudiantes):
    aprueba = f"{VERDE}Aprobados{RESET}"
    promociona = f"{AZUL}Promocionados{RESET}"
    desaprueba = f"{ROJO}Desaprobados{RESET}"

    print("="*102)
    print(f'{BOLD}{MAGENTA}{"ESTADÍSTICAS POR ESTUDIANTE":^102}{RESET}')
    print("="*102)
    print(f"{BOLD}{'Legajo':<15}{'Nombre':<15}{'Notas':^13}{'Promedio':^13}{aprueba:^24}{promociona:^28}{desaprueba:^27}{RESET}")
    print("-" * 102)

    lista_promedios = []

    for estudiante in range(len(estudiantes)):
        legajo = estudiantes[estudiante]["legajo"]
        nombre = estudiantes[estudiante]["nombre"]
        if len(nombre) > 15:
            nombre = nombre[:12] + "..."

        suma = 0
        aprobados = 0
        promocionados = 0
        desaprobados = 0
        promedio = 0

        lista_notas = list(filter(lambda nota: nota[2] == legajo, notas))
        cantidad = len(lista_notas)

        if cantidad > 0:
            suma = reduce(lambda suma, cal: suma + cal[1], lista_notas, 0)
            aprobados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 1, notas)))
            promocionados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 2, notas)))
            desaprobados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 3, notas)))
            promedio = (lambda a,b: a / b)(suma, cantidad)
            lista_promedios.append([estudiantes[estudiante]["nombre"], promedio])

        print(f"{legajo:<15}{nombre:<15}{cantidad:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")

    lista_promedios.sort(key=lambda fila: fila[1])
    if len(lista_promedios) > 3:
        ult_promedio = lista_promedios[-3]
        mejores_promedios = lista_promedios[-2:]
        lista_promedios = lista_promedios[:-3] 
        lista_empates = list(filter(lambda promedio: promedio[1] == ult_promedio[1], lista_promedios))
        lista_empates.append(ult_promedio)
        lista_empates.sort(key=lambda fila: fila[0], reverse=True)
        if len(lista_empates) > 0:
            for i in range(len(lista_empates)-1, -1, -1):
                mejores_promedios.insert(0, lista_empates[i])
    else:
        mejores_promedios = lista_promedios

    print()
    print(f'{BOLD}{NARANJA}MEJORES PROMEDIOS{RESET}')
    cont = 1
    for i in range(len(mejores_promedios) -1, -1, -1):
        print(f"{cont}. {mejores_promedios[i][0]} ({mejores_promedios[i][1]})")
        cont += 1


def estadisticas_estudiantes_particulares(notas, estudiantes, materias):
    
    lista_legajos = obtener_lista_legajos(estudiantes)

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


    boletin(estudiantes, estudiante, notas, materias)