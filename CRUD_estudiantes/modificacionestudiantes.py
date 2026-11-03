import utilidades
import json

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def modificar_estudiantes(arch_estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: solicita el legajo de un estudiante y modifica sus datos validando la información ingresada.
    '''
    try:
        with open(arch_estudiantes, 'r', encoding="UTF-8") as datos:
            estudiantes = json.load(datos)

        print()
        print(f"       ==================== {AZUL}MODIFICACIÓN ESTUDIANTES{RESET} ====================")
        legajos = [est["legajo"] for est in estudiantes]
        
        # Pedir el legajo a modificar
        while True:
            try:
                legajo = utilidades.leerentero("Ingrese el legajo del estudiante a modificar (Formato: 100) (0 para cancelar): ")
                if legajo == 0:
                    print("Operación cancelada.")
                    return
                assert legajo in legajos
                break
            except AssertionError:
                print(f"{ROJO}ERROR: Ese legajo no está registrado{RESET}")
                print("Intente nuevamente.")
                
        nombre, edad, anio = utilidades.pedir_datos_estudiante()

        # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
        otros = [est for est in estudiantes if est["legajo"] != legajo]
        usuario = utilidades.generar_usuarios(nombre, otros)


        # Obtener índice del estudiante y modificar
        indice = legajos.index(legajo)
        estudiantes[indice]["nombre"] = nombre
        estudiantes[indice]["edad"] = edad
        estudiantes[indice]["año cursada"] = anio
        estudiantes[indice]["usuario"] = usuario
        with open(arch_estudiantes, 'w', encoding="UTF-8") as datos:
            json.dump(estudiantes, datos, ensure_ascii=False, indent=4)
        print(f"Estudiante con legajo {legajo} modificado")

    except FileNotFoundError:
        print(f"{ROJO}ERROR: no se encontró el archivo {arch_estudiantes}.{RESET}")
    except json.JSONDecodeError:
        print(f"{ROJO}ERROR: el archivo {arch_estudiantes} está vacío o dañado.{RESET}")
    except OSError as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_estudiantes}: {error}{RESET}")