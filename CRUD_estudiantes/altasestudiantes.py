import utilidades
import json

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()


# Agregar datos 
def altas_estudiantes(arch_estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: solicita y valida los datos de un nuevo estudiante y lo agrega un diccionario
         y luego a la lista de estudiantes.
    '''
    try:
        print()
        print(f"       ==================== {VERDE}ALTAS ESTUDIANTES{RESET} ====================")
        with open(arch_estudiantes, 'r', encoding="UTF-8") as datos:
            estudiantes = json.load(datos)  # Cargar el contenido existente del archivo JSON

        # Obtener el legajo más alto y sumar 1
        if estudiantes:
            nuevo_legajo = max(est["legajo"] for est in estudiantes) + 1
        else:
            nuevo_legajo = 100  # Si la lista está vacía, comenzamos desde 100

        nombre, edad, anio = utilidades.pedir_datos_estudiante()

        # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
        usuario = utilidades.generar_usuarios(nombre, estudiantes)

        # Crear nuevo estudiante
        nuevo_estudiante = {"legajo": nuevo_legajo, "nombre": nombre, "edad": edad, "año cursada": anio, "usuario": usuario}
        estudiantes.append(nuevo_estudiante)

        # Sobrescribir el archivo con los datos actualizados
        with open(arch_estudiantes, 'w', encoding="UTF-8") as datos:
            json.dump(estudiantes, datos, ensure_ascii=False, indent=4) # ensure_ascii=False Permite conservar caracteres como á, é, í, ó, ú y ñ directamente en el archivo JSON, en lugar de representarlos mediante secuencias de escape Unicode.
        print(f'Se ha agregado a {nuevo_estudiante['nombre']}')

    except FileNotFoundError:
        print(f"{ROJO}ERROR: no se encontró el archivo {arch_estudiantes}.{RESET}")
    except json.JSONDecodeError:
        print(f"{ROJO}ERROR: el archivo {arch_estudiantes} está vacío o dañado.{RESET}")
    except OSError as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_estudiantes}: {error}{RESET}")