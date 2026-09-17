from functools import reduce
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


def boletin_completo(estudiantes, estudiante, notas, materias):
    '''
    pre: recibe las listas de estudiantes, notas y materias, y el legajo del estudiante.
    pos: muestra por pantalla el boletín del estudiante con sus materias, notas y resultados.
    '''
    # ==============================
    # REPORTE / BOLETÍN DEL ALUMNO
    # ==============================

    # Buscar nombre del alumno
    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)
    posicion_estudiante = lista_legajos.index(estudiante)
    nombre_alumno = estudiantes[posicion_estudiante]["nombre"]

    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"BOLETÍN":^40}{RESET}')
    print("=" * 40)
    print(f"Alumno: {nombre_alumno}")
    print(f"Legajo: {estudiante}")
    print("-" * 40)
    suma = 0
    total = 0

    for registro in notas:
        if registro[2] == estudiante:

            nota_alumno = registro[1]
            codigo_materia = registro[3]
            suma += nota_alumno
            total += 1

            # Buscar la materia
            posicion_materia = utilidades.busqueda_secuencial(materias, 0, codigo_materia)
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

    if total > 0:
        promedio = (lambda a, b: a / b)(suma, total)
        promedio = f"{promedio:.1f}"
        print(f"{"Promedio: ":>36}{promedio}")


def reporte_materia(materias, materia, notas, estudiantes):
    '''
    pre: recibe las matrices de materias y notas, la lista de diccionarios de estudiantes
         y el código de la materia a reportar.
    pos: muestra por pantalla el reporte de la materia con todos los estudiantes que la
         cursaron, su nota y su resultado (promocionada, aprobada o desaprobada).
    '''
    # ==============================
    # REPORTE DE LA MATERIA
    # ==============================

    # Buscar nombre de la materia
    posicion_materia = utilidades.busqueda_secuencial(materias, 0, materia)
    nombre_materia = materias[posicion_materia][1]

    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)

    # Se guardan los códigos originales para restaurarlos después.
    codigos = [fila[0] for fila in materias]

    # Se genera temporalmente un código con el año y el cuatrimestre.
    lista_codigo = list(map(lambda fila: str(fila[3]) + "Pri" + str(fila[0]) if fila[2] == 1 else str(fila[3]) + "Seg" + str(fila[0]), materias))
    for fila in range(len(materias)):
        materias[fila][0] = lista_codigo[fila]

    print()
    print("=" * 40)
    print(f'{BOLD}{MAGENTA}{"REPORTE":^40}{RESET}')
    print("=" * 40)
    print(f"Materia: {nombre_materia}")
    print(f"Código: {materias[posicion_materia][0]}")
    print("-" * 40)
    suma = 0
    total = 0

    for registro in notas:
        if registro[3] == materia:

            nota_alumno = registro[1]
            legajo_alumno = registro[2]
            suma += nota_alumno
            total += 1

            # Buscar la materia
            posicion_alumno = lista_legajos.index(legajo_alumno)
            nombre_alumno = estudiantes[posicion_alumno]["nombre"]

            if nota_alumno >= 8:
                resultado = f"{AZUL}PROMOCIONADA{RESET}"
            elif nota_alumno >= 4:
                resultado = f"{VERDE}APROBADA{RESET}"
            else:
                resultado = f"{ROJO}DESAPROBADA{RESET}"

            print(f"Alumno: {nombre_alumno}")
            print(f"Nota: {nota_alumno}")
            print(f"Resultado: {resultado}")
            print("-" * 40)

    # Se restauran los códigos originales para no modificar la matriz.
    for fila in range(len(materias)):
        materias[fila][0] = codigos[fila]

    if total > 0:
        promedio = (lambda a, b: a / b)(suma, total)
        promedio = f"{promedio:.1f}"
        print(f"{"Promedio: ":>36}{promedio}")


def estadisticas_materias(notas, materias):
    '''
    pre: recibe la matriz de notas y la matriz de materias.
    pos: muestra por pantalla las estadísticas de cada materia (cantidad de notas, promedio,
         y cantidad de alumnos aprobados, promocionados y desaprobados), y por cada cuatrimestre
         que tenga notas cargadas informa la materia con mejor y peor promedio, la de más
         aprobados, la de más desaprobados, y el porcentaje total de aprobados y desaprobados.
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
        lista_notas = list(fila[1] for fila in lista_notas)

        if cantidad > 0:
            suma = reduce(lambda cal1, cal2: cal1 + cal2, lista_notas)
            aprobados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 1, notas)))
            promocionados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 2, notas)))
            desaprobados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 3, notas)))
            promedio = (lambda a,b: a / b)(suma, cantidad)
            promedio = f"{promedio:.1f}"
            promedio = float(promedio)

        id_materia = materias[materia][0]
        if re.findall(".Pri", id_materia) and suma > 0:
            lista_cuat1.append([materias[materia][1], promedio, aprobados + promocionados, desaprobados])
        elif re.findall(".Seg", id_materia) and suma > 0:
            lista_cuat2.append([materias[materia][1], promedio, aprobados + promocionados, desaprobados])
        print(f"{id_materia:<15}{nombre:<15}{cantidad:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")


    for fila in range(len(materias)):
        materias[fila][0] = codigos[fila]


    if len(lista_cuat1) != 0:
        lista_aprobados = list(fila[2] for fila in lista_cuat1)
        lista_desaprobados = list(fila[3] for fila in lista_cuat1)
        aprobados = sum(lista_aprobados)
        desaprobados = reduce(lambda x, y: x + y, lista_desaprobados)
        total = aprobados + desaprobados
        print()
        print(f'{BOLD}{NARANJA}MATERIAS (PRIMER CUATRIMESTRE){RESET}')
        lista_cuat1.sort(key=lambda fila: fila[1])
        mejor_promedio = lista_cuat1[-1]
        lista_empates = list(filter(lambda promedio: promedio[1] == mejor_promedio[1], lista_cuat1))
        cadena = ""
        for promedio in lista_empates:
            cadena = cadena + f"{promedio[0]}, "

        print(f"- Mejor promedio: {cadena[:-2]} ({mejor_promedio[1]})")

        peor_promedio = lista_cuat1[0]
        if peor_promedio[1] != mejor_promedio[1] and (peor_promedio[2] + peor_promedio[3]) > 0:
            lista_empates = list(filter(lambda promedio: promedio[1] == peor_promedio[1], lista_cuat1))
            cadena = ""
            for promedio in lista_empates:
                cadena = cadena + f"{promedio[0]}, "

            print(f"- Peor promedio: {cadena[:-2]} ({peor_promedio[1]})")
        else:
            print(f"- Peor promedio: -")

        if aprobados != 0:
            lista_cuat1.sort(key=lambda fila: fila[2])
            mas_aprobados = lista_cuat1[-1]
            lista_empates = list(filter(lambda fila: fila[2] == mas_aprobados[2], lista_cuat1))
            cadena = ""
            for fila in lista_empates:
                cadena = cadena + f"{fila[0]}, "

            print(f"- Más estudiantes aprobados: {cadena[:-2]} ({mas_aprobados[2]})")
        else:
            print(f"- Más estudiantes aprobados: -")

        if desaprobados != 0:
            lista_cuat1.sort(key=lambda fila: fila[3])
            mas_desaprobados = lista_cuat1[-1]
            lista_empates = list(filter(lambda fila: fila[3] == mas_desaprobados[3], lista_cuat1))
            cadena = ""
            for fila in lista_empates:
                cadena = cadena + f"{fila[0]}, "

            print(f"- Más estudiantes desaprobados: {cadena[:-2]} ({mas_desaprobados[3]})")
        else:
            print(f"- Más estudiantes deaprobados: -")

        porcentaje_aprobados = (aprobados / total) * 100
        porcentaje_desaprobados = (desaprobados / total) * 100

        print(f"- Porcentaje total de aprobados: {porcentaje_aprobados:.1f}%")
        print(f"- Porcentaje total de desaprobados: {porcentaje_desaprobados:.1f}%")



    if len(lista_cuat2) != 0:
        lista_aprobados = list(fila[2] for fila in lista_cuat2)
        lista_desaprobados = list(fila[3] for fila in lista_cuat2)
        aprobados = reduce(lambda x, y: x + y, lista_aprobados)
        desaprobados = sum(lista_desaprobados)
        total = aprobados + desaprobados
        print()
        print(f'{BOLD}{NARANJA}MATERIAS (SEGUNDO CUATRIMESTRE){RESET}')
        lista_cuat2.sort(key=lambda fila: fila[1])
        mejor_promedio = lista_cuat2[-1]
        lista_empates = list(filter(lambda promedio: promedio[1] == mejor_promedio[1], lista_cuat2))
        cadena = ""
        for promedio in lista_empates:
            cadena = cadena + f"{promedio[0]}, "

        print(f"- Mejor promedio: {cadena[:-2]} ({mejor_promedio[1]})")

        peor_promedio = lista_cuat2[0]
        if peor_promedio[1] != mejor_promedio[1] and (peor_promedio[2] + peor_promedio[3]) > 0:
            lista_empates = list(filter(lambda promedio: promedio[1] == peor_promedio[1], lista_cuat2))
            cadena = ""
            for promedio in lista_empates:
                cadena = cadena + f"{promedio[0]}, "

            print(f"- Peor promedio: {cadena[:-2]} ({peor_promedio[1]})")
        else:
            print(f"- Peor promedio: -")

        if aprobados != 0:
            lista_cuat2.sort(key=lambda fila: fila[2])
            mas_aprobados = lista_cuat2[-1]
            lista_empates = list(filter(lambda fila: fila[2] == mas_aprobados[2], lista_cuat2))
            cadena = ""
            for fila in lista_empates:
                cadena = cadena + f"{fila[0]}, "

            print(f"- Más estudiantes aprobados: {cadena[:-2]} ({mas_aprobados[2]})")
        else:
            print(f"- Más estudiantes aprobados: -")

        if desaprobados != 0:
            lista_cuat2.sort(key=lambda fila: fila[3])
            mas_desaprobados = lista_cuat2[-1]
            lista_empates = list(filter(lambda fila: fila[3] == mas_desaprobados[3], lista_cuat2))
            cadena = ""
            for fila in lista_empates:
                cadena = cadena + f"{fila[0]}, "

            print(f"- Más estudiantes desaprobados: {cadena[:-2]} ({mas_desaprobados[3]})")
        else:
            print(f"- Más estudiantes deaprobados: -")

        porcentaje_aprobados = (aprobados / total) * 100
        porcentaje_desaprobados = (desaprobados / total) * 100
    
        print(f"- Porcentaje total de aprobados: {porcentaje_aprobados:.1f}%")
        print(f"- Porcentaje total de desaprobados: {porcentaje_desaprobados:.1f}%")


def estadisticas_estudiantes(notas, estudiantes):
    '''
    pre: recibe la matriz de notas y la lista de diccionarios de estudiantes.
    pos: muestra por pantalla la cantidad de notas, el promedio y la cantidad de aprobadas,
         promocionadas y desaprobadas de cada estudiante, e informa el/los estudiante/s con
         mejor promedio (hasta 3, considerando empates) y el/los de peor promedio.
    '''
    aprueba = f"{VERDE}Aprobadas{RESET}"
    promociona = f"{AZUL}Promocionadas{RESET}"
    desaprueba = f"{ROJO}Desaprobadas{RESET}"

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
        lista_notas = list(fila[1] for fila in lista_notas)

        if cantidad > 0:
            suma = reduce(lambda cal1, cal2: cal1 + cal2, lista_notas)
            aprobados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 1, notas)))
            promocionados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 2, notas)))
            desaprobados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 3, notas)))
            promedio = (lambda a,b: a / b)(suma, cantidad)
            promedio = f"{promedio:.1f}"
            promedio = float(promedio)
            lista_promedios.append([estudiantes[estudiante]["nombre"], promedio])

        print(f"{legajo:<15}{nombre:<15}{cantidad:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")

    lista_promedios.sort(key=lambda fila: (fila[1], fila[0]))
    if len(lista_promedios) > 3:
        ult_promedio = lista_promedios[-3]
        segundo_promedio = lista_promedios[-2]
        mejor_promedio = lista_promedios[-1]
        peor_promedio = lista_promedios[0]
        mejores_promedios = []

        lista_empates = list(filter(lambda promedio: promedio[1] == mejor_promedio[1], lista_promedios))
        for i in range(len(lista_empates)):
            mejores_promedios.insert(0, lista_empates[i])

        if segundo_promedio[1] != mejor_promedio[1]:
            lista_empates = list(filter(lambda promedio: promedio[1] == segundo_promedio[1], lista_promedios))
            for i in range(len(lista_empates)):
                mejores_promedios.insert(0, lista_empates[i])

        if ult_promedio[1] != segundo_promedio[1]:
            lista_empates = list(filter(lambda promedio: promedio[1] == ult_promedio[1], lista_promedios))
            for i in range(len(lista_empates)):
                mejores_promedios.insert(0, lista_empates[i])

        if peor_promedio[1] != ult_promedio[1]:
            lista_empates = list(filter(lambda promedio: promedio[1] == peor_promedio[1], lista_promedios))
            cadena = ""
            for promedio in lista_empates:
                cadena = cadena + f"{promedio[0]}, "
            cadena = cadena[:-2]
    else:
        peor_promedio = lista_promedios[0]
        ult_promedio = lista_promedios[-1]
        if peor_promedio[1] == ult_promedio[1]:
            mejores_promedios = lista_promedios
        else:
            lista_empates = list(filter(lambda promedio: promedio[1] == peor_promedio[1], lista_promedios))
            cadena = ""
            for promedio in lista_empates:
                cadena = cadena + f"{promedio[0]}, "
            cadena = cadena[:-2]
            if len(lista_empates) == 1:
                mejores_promedios = lista_promedios[1:]
            else:
                mejores_promedios = lista_promedios[2:]

    print()
    if len(mejores_promedios) > 1:
        print(f'{BOLD}{VERDE}MEJORES PROMEDIOS{RESET}')
        cont = 1
        for i in range(len(mejores_promedios) -1, -1, -1):
            print(f"{cont}. {mejores_promedios[i][0]} ({mejores_promedios[i][1]})")
            cont += 1
    else: 
        print(f'{BOLD}{VERDE}MEJOR PROMEDIO:{RESET} {mejores_promedios[0][0]} ({mejores_promedios[0][1]})')

    if peor_promedio[1] != ult_promedio[1]:
        print()
        print(f"{BOLD}{ROJO}PEOR PROMEDIO:{RESET} {cadena} ({peor_promedio[1]})")


def estadisticas_particulares(notas, estudiantes, materias, titulo):
    '''
    pre: recibe la matriz de notas, la lista de diccionarios de estudiantes, la matriz de
         materias y el título que indica si se busca un estudiante o una materia.
    pos: solicita y valida el legajo del estudiante o el código de la materia, y muestra por
         pantalla su boletín completo o su reporte de notas, según corresponda.
    '''

    if titulo == "ESTUDIANTES":
        lista_legajos = utilidades.obtener_lista_legajos(estudiantes)

        estudiante = input("Ingrese el legajo del estudiante para su boletín (Formato: 100): ")

        while estudiante.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el legajo.{RESET}")
            estudiante = input("Ingrese de nuevo el legajo del estudiante para su boletín (Formato: 100): ")
        estudiante = int(estudiante)

        while estudiante not in lista_legajos:
            print(f"{ROJO}ERROR: Ese legajo no está registrado.{RESET}")
            
            estudiante = input("Ingrese de nuevo el legajo del estudiante para su boletín (Formato: 100): ")

            while estudiante.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras en el legajo.{RESET}")
                estudiante = input("Ingrese de nuevo el legajo del estudiante para su boletín (Formato: 100): ")
            estudiante = int(estudiante)


        boletin_completo(estudiantes, estudiante, notas, materias)

    else:
        materia = input("Ingrese el códgio de la materia para su reporte (Formato: 100): ")
        
        while materia.isnumeric() == False:
            print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
            materia = input("Ingrese de nuevo el código de la materia para su reporte (Formato: 100): ")
        materia = int(materia)

        registrado = utilidades.busqueda_secuencial(materias, 0, materia)

        while registrado == -1:
            print(f"{ROJO}ERROR: Ese código no está registrado.{RESET}")
            
            materia = input("Ingrese de nuevo el código de la materia para su reporte (Formato: 100): ")

            while materia.isnumeric() == False:
                print(f"{ROJO}ERROR: No se admiten letras en el código.{RESET}")
                materia = input("Ingrese de nuevo el código de la materia para su reporte (Formato: 100): ")
            materia = int(materia)


        reporte_materia(materias, materia, notas, estudiantes)