import utilidades
from functools import reduce
import json

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def estadisticas_estudiantes(arch_notas, arch_estudiantes):
    '''
    pre: recibe la matriz de notas y la lista de diccionarios de estudiantes.
    pos: muestra por pantalla la cantidad de notas, el promedio y la cantidad de aprobadas,
         promocionadas y desaprobadas de cada estudiante, e informa el/los estudiante/s con
         mejor promedio (hasta 3, considerando empates) y el/los de peor promedio.
    '''
    try:
        with open(arch_estudiantes, 'r', encoding="UTF-8") as datos:
                estudiantes = json.load(datos)
    except OSError as error:
        print(f'No se pudo leer el archivo: {error}')
    else:    
        
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
            matriz_notas = []

            with open(arch_notas, "rt", encoding="UTF-8") as notas:
                for linea2 in notas:
                    datos2 = linea2.strip().split(";")
                    if int(datos2[2]) == legajo:
                        matriz_notas.append(datos2)

            lista_notas = list(int(fila[1]) for fila in matriz_notas)
            cantidad = len(lista_notas)

            if cantidad > 0:
                suma = reduce(lambda cal1, cal2: int(cal1) + int(cal2), lista_notas)
                aprobados = len(list(filter(lambda nota: int(nota[4]) == 1, matriz_notas)))
                promocionados = len(list(filter(lambda nota: int(nota[4]) == 2, matriz_notas)))
                desaprobados = len(list(filter(lambda nota: int(nota[4]) == 3, matriz_notas)))
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