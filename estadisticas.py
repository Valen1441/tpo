from functools import reduce

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"

def estadisticas_materias(notas, materias):

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

        if len(lista_notas) > 0:
            suma = reduce(lambda suma, cal: suma + cal[1], lista_notas, 0)
            aprobados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 1, notas)))
            promocionados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 2, notas)))
            desaprobados = len(list(filter(lambda nota: nota[3] == id_materia and nota[4] == 3, notas)))
            promedio = (lambda a,b: a / b)(suma, cantidad)

        id_materia = materias[materia][0]
        print(f"{id_materia:<15}{nombre:<15}{cantidad:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")


    for fila in range(len(materias)):
        materias[fila][0] = codigos[fila]
    
def estadisticas_estudiantes(notas, estudiantes, materias):
    aprueba = f"{VERDE}Aprobados{RESET}"
    promociona = f"{AZUL}Promocionados{RESET}"
    desaprueba = f"{ROJO}Desaprobados{RESET}"

    print("="*102)
    print(f'{BOLD}{MAGENTA}{"ESTADÍSTICAS POR ESTUDIANTE":^102}{RESET}')
    print("="*102)
    print(f"{BOLD}{'Legajo':<15}{'Nombre':<15}{'Notas':^13}{'Promedio':^13}{aprueba:^24}{promociona:^28}{desaprueba:^27}{RESET}")
    print("-" * 102)

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

        if len(lista_notas) > 0:
            suma = reduce(lambda suma, cal: suma + cal[1], lista_notas, 0)
            aprobados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 1, notas)))
            promocionados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 2, notas)))
            desaprobados = len(list(filter(lambda nota: nota[2] == legajo and nota[4] == 3, notas)))
            promedio = (lambda a,b: a / b)(suma, cantidad)

        calificaciones = ""
        for nota in lista_notas:
            calificaciones = calificaciones + str(nota[1]) + ", "

        calificaciones = calificaciones[:-2]

        print(f"{legajo:<15}{nombre:<15}{calificaciones:^13}{promedio:^13}{aprobados:^13}{promocionados:^17}{desaprobados:^17}")