import utilidades
import json

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def bajas_estudiantes(arch_estudiantes, notas):
    '''
    pre: recibe la lista de diccionarios de estudiantes y la matriz de notas.
    pos: solicita un legajo y elimina el estudiante si existe y no tiene calificaciones registradas.
    '''
    try:
        with open(arch_estudiantes, 'r', encoding="UTF-8") as datos:
            estudiantes = json.load(datos)

        print()
        print(f"       ==================== {NARANJA}BAJAS ESTUDIANTES{RESET} ====================")
        legajos = [est["legajo"] for est in estudiantes]

        # Pedir legajo a eliminar
        while True:
            try:
                legajo = utilidades.leerentero("Ingrese el legajo del estudiante a eliminar (Formato: 100) (0 para cancelar): ")
                if legajo == 0:
                    print("Operación cancelada.")
                    return
                esta_en_calificaciones = utilidades.devolver_dato_plano(notas, 2, legajo)
                assert legajo in legajos
                assert esta_en_calificaciones == -1
                break
            except AssertionError:
                if legajo not in legajos:
                    print(f"{ROJO}ERROR: Ese legajo no está registrado{RESET}")
                else:
                    print(f"{ROJO}ERROR: Ese estudiante tiene una calificación registrada, no se puede eliminar{RESET}")
                print("Intente nuevamente.")

        indice = legajos.index(legajo)
        estudiantes.pop(indice)  # Elimina el estudiante por índice

        with open(arch_estudiantes, 'w', encoding="UTF-8") as datos:
            json.dump(estudiantes, datos, ensure_ascii=False, indent=4)
        print(f"Estudiante con legajo {legajo} eliminado.")

    except FileNotFoundError:
        print(f"{ROJO}ERROR: no se encontró el archivo {arch_estudiantes}.{RESET}")
    except json.JSONDecodeError:
        print(f"{ROJO}ERROR: el archivo {arch_estudiantes} está vacío o dañado.{RESET}")
    except OSError as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_estudiantes}: {error}{RESET}")