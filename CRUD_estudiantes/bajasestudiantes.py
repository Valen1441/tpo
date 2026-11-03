import utilidades
import json

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def bajas_estudiantes(arch_estudiantes, notas):
    '''
    pre: recibe la lista de diccionarios de estudiantes y la matriz de notas.
    pos: solicita un legajo y elimina el estudiante si existe y no tiene calificaciones registradas.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS ESTUDIANTES{RESET} ====================")

    try:
        with open(arch_estudiantes, 'r', encoding="UTF-8") as datos:
            estudiantes = json.load(datos)

        legajos = [est["legajo"] for est in estudiantes]

        # Pedir legajo a eliminar
        while True:
            try:
                legajo = utilidades.leerentero("Ingrese el legajo del estudiante a eliminar (Formato: 100): ")
                esta_en_calificaciones = utilidades.devolver_dato_plano(notas, 2, legajo)
                assert legajo in legajos
                assert esta_en_calificaciones == -1
                break
            except AssertionError:
                if legajo not in legajos:
                    print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
                else:
                    print(f"{ROJO}ERROR: Ese estudiante tiene una calificaión registrada, no se puede eliminar{RESET}")
                print("Intente nuevamente.")

        if legajo in legajos:
            indice = legajos.index(legajo)
            estudiantes.pop(indice)  # Elimina el empleado por índice

            with open(arch_estudiantes, 'w', encoding="UTF-8") as datos:
                json.dump(estudiantes, datos, ensure_ascii=False, indent=4)
            print(f"Estudiante con legajo {legajo} eliminado.")
        else:
            print(f"Estudiante con legajo {legajo} no encontrado.")
    except (FileNotFoundError, OSError, json.JSONDecodeError) as error:
        print(f'Error! {error}')