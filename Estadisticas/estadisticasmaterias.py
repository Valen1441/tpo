import utilidades
from functools import reduce
import re
 
# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()
 
 
def mostrar_resumen_cuatrimestre(titulo, lista):
    '''
    pre: recibe el título del cuatrimestre y una lista no vacía de filas
         [nombre, promedio, notas aprobadas (incluye promocionadas), notas desaprobadas].
    pos: muestra la materia con mejor y peor promedio, la de más notas aprobadas,
         la de más notas desaprobadas y los porcentajes totales de aprobadas y
         desaprobadas. En los empates se informan todas las materias.
    '''
    aprobados = reduce(lambda a, b: a + b, map(lambda fila: fila[2], lista))
    desaprobados = reduce(lambda a, b: a + b, map(lambda fila: fila[3], lista))
    total = aprobados + desaprobados
 
    mejor = max(fila[1] for fila in lista)
    peor = min(fila[1] for fila in lista)
    mas_aprobadas = max(fila[2] for fila in lista)
    mas_desaprobadas = max(fila[3] for fila in lista)
 
    print()
    print(f"{BOLD}{NARANJA}{titulo}{RESET}")
    print(f"- Mejor promedio: {utilidades.nombres_con_valor(lista, 1, mejor)} ({mejor})")
 
    # Si todas tienen el mismo promedio no hay una "peor"
    if peor != mejor:
        print(f"- Peor promedio: {utilidades.nombres_con_valor(lista, 1, peor)} ({peor})")
    else:
        print("- Peor promedio: -")
 
    if mas_aprobadas > 0:
        print(f"- Más notas aprobadas: {utilidades.nombres_con_valor(lista, 2, mas_aprobadas)} ({mas_aprobadas})")
    else:
        print("- Más notas aprobadas: -")
 
    if mas_desaprobadas > 0:
        print(f"- Más notas desaprobadas: {utilidades.nombres_con_valor(lista, 3, mas_desaprobadas)} ({mas_desaprobadas})")
    else:
        print("- Más notas desaprobadas: -")
 
    print(f"- Porcentaje total de notas aprobadas: {aprobados / total * 100:.1f}%")
    print(f"- Porcentaje total de notas desaprobadas: {desaprobados / total * 100:.1f}%")
 
 
def estadisticas_materias(arch_notas, arch_materias):
    '''
    pre: recibe las rutas de los archivos de notas y de materias.
    pos: muestra por pantalla las estadísticas de cada materia (cantidad de notas, promedio,
         y cantidad de notas aprobadas, promocionadas y desaprobadas), y por cada cuatrimestre
         que tenga notas cargadas informa la materia con mejor y peor promedio, la de más
         notas aprobadas, la de más notas desaprobadas y los porcentajes totales.
    '''
    lista_cuat1 = []
    lista_cuat2 = []
 
    try:
        with open(arch_materias, "rt", encoding="UTF-8") as materias:
            aprueba = f"{VERDE}Aprobadas{RESET}"
            promociona = f"{AZUL}Promocionadas{RESET}"
            desaprueba = f"{ROJO}Desaprobadas{RESET}"
 
            print("=" * 102)
            print(f'{BOLD}{MAGENTA}{"ESTADÍSTICAS POR MATERIA":^102}{RESET}')
            print("=" * 102)
            print(f"{BOLD}{'ID Materia':<15}{'Nombre':<15}{'Notas':^13}{'Promedio':^13}{aprueba:^24}{promociona:^28}{desaprueba:^27}{RESET}")
            print("-" * 102)
 
            for linea in materias:
                datos = linea.strip().split(";")
                id_materia = int(datos[0])
                nombre = datos[1]
                codigo = utilidades.codigo_temporal(datos[0], datos[2], datos[3])
 
                nombre_corto = nombre
                # Si el nombre tiene más de 15 caracteres se corta en el 12 y se agregan "..."
                if len(nombre) > 15:
                    nombre_corto = nombre[:12] + "..."
 
                # Matriz solo con las notas de esta materia (columna 3 = código de materia)
                matriz_notas = utilidades.filtrar_notas(arch_notas, 3, id_materia)
                lista_notas = list(map(lambda fila: int(fila[1]), matriz_notas))
                cantidad = len(lista_notas)
 
                aprobados = 0
                promocionados = 0
                desaprobados = 0
                promedio = 0
 
                if cantidad > 0:
                    suma = reduce(lambda cal1, cal2: cal1 + cal2, lista_notas)
                    aprobados = len(list(filter(lambda fila: int(fila[4]) == 1, matriz_notas)))
                    promocionados = len(list(filter(lambda fila: int(fila[4]) == 2, matriz_notas)))
                    desaprobados = len(list(filter(lambda fila: int(fila[4]) == 3, matriz_notas)))
                    promedio = round(suma / cantidad, 1)
 
                    # Se guarda el nombre completo; solo se recorta al imprimir la tabla
                    fila_materia = [nombre, promedio, aprobados + promocionados, desaprobados]
                    if re.search("Pri", codigo):
                        lista_cuat1.append(fila_materia)
                    else:
                        lista_cuat2.append(fila_materia)
 
                print(f"{codigo:<15}{nombre_corto:<15}{cantidad:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")
 
    except (OSError, ValueError) as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_materias}: {error}{RESET}")
    else:
        if len(lista_cuat1) != 0:
            mostrar_resumen_cuatrimestre("MATERIAS (PRIMER CUATRIMESTRE)", lista_cuat1)
        if len(lista_cuat2) != 0:
            mostrar_resumen_cuatrimestre("MATERIAS (SEGUNDO CUATRIMESTRE)", lista_cuat2)