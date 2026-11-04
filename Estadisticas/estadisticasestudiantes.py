import utilidades
import json
 
# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()
 
 
def mostrar_mejores_y_peor(lista_promedios):
    '''
    pre: recibe una lista no vacía de filas [nombre, promedio], una por cada
         estudiante que tiene notas.
    pos: muestra los mejores promedios (los tres primeros puestos, incluyendo a
         todos los empatados) y el peor promedio, siempre que el peor no esté ya
         entre los mejores. Los empates se ordenan alfabéticamente por nombre.
    '''
    # De mayor a menor promedio; si empatan, por nombre de la A a la Z
    lista_promedios.sort(key=lambda fila: (-fila[1], fila[0]))
    mejor = lista_promedios[0][1]
    peor = lista_promedios[-1][1]
 
    if len(lista_promedios) > 3:
        # El corte es el promedio del tercer puesto: entran todos los que lo igualan o superan
        corte = lista_promedios[2][1]
        mejores = list(filter(lambda fila: fila[1] >= corte, lista_promedios))
    elif mejor == peor:
        # Todos empatados: todos son "mejores" y no hay peor
        mejores = lista_promedios
    else:
        # Con 3 o menos se separa al peor para que no figure también entre los mejores
        mejores = list(filter(lambda fila: fila[1] > peor, lista_promedios))
 
    print()
    if len(mejores) > 1:
        print(f"{BOLD}{VERDE}MEJORES PROMEDIOS{RESET}")
        for i in range(len(mejores)):
            print(f"{i + 1}. {mejores[i][0]} ({mejores[i][1]})")
    else:
        print(f"{BOLD}{VERDE}MEJOR PROMEDIO:{RESET} {mejores[0][0]} ({mejores[0][1]})")
 
    # El peor solo se informa si su promedio es menor que el del último de los mejores
    if peor < mejores[-1][1]:
        print()
        print(f"{BOLD}{ROJO}PEOR PROMEDIO:{RESET} {utilidades.nombres_con_valor(lista_promedios, 1, peor)} ({peor})")
 
 
def estadisticas_estudiantes(arch_notas, arch_estudiantes):
    '''
    pre: recibe las rutas de los archivos de notas y de estudiantes.
    pos: muestra por pantalla la cantidad de notas, el promedio y la cantidad de aprobadas,
         promocionadas y desaprobadas de cada estudiante, e informa el/los estudiante/s con
         mejor promedio (hasta 3 puestos, considerando empates) y el/los de peor promedio.
    '''
    try:
        with open(arch_estudiantes, "r", encoding="UTF-8") as datos:
            estudiantes = json.load(datos)
    except (OSError, json.JSONDecodeError) as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_estudiantes}: {error}{RESET}")
    else:
        aprueba = f"{VERDE}Aprobadas{RESET}"
        promociona = f"{AZUL}Promocionadas{RESET}"
        desaprueba = f"{ROJO}Desaprobadas{RESET}"
 
        print("=" * 102)
        print(f'{BOLD}{MAGENTA}{"ESTADÍSTICAS POR ESTUDIANTE":^102}{RESET}')
        print("=" * 102)
        print(f"{BOLD}{'Legajo':<15}{'Nombre':<15}{'Notas':^13}{'Promedio':^13}{aprueba:^24}{promociona:^28}{desaprueba:^27}{RESET}")
        print("-" * 102)
 
        lista_promedios = []
 
        for est in estudiantes:
            legajo = est["legajo"]
            nombre = est["nombre"]
            nombre_corto = nombre
            # Si el nombre tiene más de 15 caracteres se corta en el 12 y se agregan "..."
            if len(nombre) > 15:
                nombre_corto = nombre[:12] + "..."
 
            # Matriz solo con las notas de este estudiante (columna 2 = legajo)
            matriz_notas = utilidades.filtrar_notas(arch_notas, 2, legajo)
            lista_notas = list(map(lambda fila: int(fila[1]), matriz_notas))
            cantidad = len(lista_notas)
 
            aprobados = 0
            promocionados = 0
            desaprobados = 0
            promedio = 0
 
            if cantidad > 0:
                suma = utilidades.suma_recursiva(lista_notas)
                aprobados = utilidades.contar_en_columna(matriz_notas, 4, 1)
                promocionados = utilidades.contar_en_columna(matriz_notas, 4, 2)
                desaprobados = utilidades.contar_en_columna(matriz_notas, 4, 3)
                promedio = round(suma / cantidad, 1)
                lista_promedios.append([nombre, promedio])
 
            print(f"{legajo:<15}{nombre_corto:<15}{cantidad:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")
 
        if lista_promedios:
            mostrar_mejores_y_peor(lista_promedios)
        else:
            print()
            print("Ningún estudiante tiene notas registradas.")