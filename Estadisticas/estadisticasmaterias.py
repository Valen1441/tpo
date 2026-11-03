import utilidades
from functools import reduce
import re

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def estadisticas_materias(arch_notas, arch_materias):
    '''
    pre: recibe la matriz de notas y la matriz de materias.
    pos: muestra por pantalla las estadísticas de cada materia (cantidad de notas, promedio,
         y cantidad de alumnos aprobados, promocionados y desaprobados), y por cada cuatrimestre
         que tenga notas cargadas informa la materia con mejor y peor promedio, la de más
         aprobados, la de más desaprobados, y el porcentaje total de aprobados y desaprobados.
    '''
    try:
        materias = open(arch_materias, "rt", encoding="UTF-8") 
    except OSError as error:
        print(f'No se pudo leer el archivo: {error}')
    else:  

        aprueba = f"{VERDE}Aprobados{RESET}"
        promociona = f"{AZUL}Promocionados{RESET}"
        desaprueba = f"{ROJO}Desaprobados{RESET}"

        print("="*102)
        print(f'{BOLD}{MAGENTA}{"ESTADÍSTICAS POR MATERIA":^102}{RESET}')
        print("="*102)
        print(f"{BOLD}{'ID Materia':<15}{'Nombre':<15}{'Notas':^13}{'Promedio':^13}{aprueba:^24}{promociona:^28}{desaprueba:^27}{RESET}")
        print("-" * 102)

        codigos = utilidades.codigo_temporal(arch_materias)

        lista_cuat1 = []
        lista_cuat2 = []
        cont = 0

        for linea in materias:
            datos = linea.strip().split(";")
            id_materia = int(datos[0])
            nombre = datos[1]
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
                    if int(datos2[3]) == id_materia:
                        matriz_notas.append(datos2)

            lista_notas = list(int(fila[1]) for fila in matriz_notas)
            cantidad = len(lista_notas)

            if cantidad > 0:
                suma = reduce(lambda cal1, cal2: cal1 + cal2, lista_notas)
                aprobados = len(list(filter(lambda nota: int(nota[4]) == 1, matriz_notas)))
                promocionados = len(list(filter(lambda nota: int(nota[4]) == 2, matriz_notas)))
                desaprobados = len(list(filter(lambda nota: int(nota[4]) == 3, matriz_notas)))
                promedio = (lambda a,b: a / b)(suma, cantidad)
                promedio = f"{promedio:.1f}"
                promedio = float(promedio)

            id_materia = codigos[cont]
            cont += 1
            if re.findall(".Pri", id_materia) and suma > 0:
                lista_cuat1.append([nombre, promedio, aprobados + promocionados, desaprobados])
            elif re.findall(".Seg", id_materia) and suma > 0:
                lista_cuat2.append([nombre, promedio, aprobados + promocionados, desaprobados])
            print(f"{id_materia:<15}{nombre:<15}{cantidad:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")


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
                print(f"- Más estudiantes desaprobados: -")

            porcentaje_aprobados = (aprobados / total) * 100
            porcentaje_desaprobados = (desaprobados / total) * 100
        
            print(f"- Porcentaje total de aprobados: {porcentaje_aprobados:.1f}%")
            print(f"- Porcentaje total de desaprobados: {porcentaje_desaprobados:.1f}%")

    finally:
        try:
            notas.close()
        except NameError:
            pass