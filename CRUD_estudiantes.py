import utilidades
import json
import re

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def generar_usuarios(nombre, estudiantes):
    '''
    pre: recibe un nombre completo ("Nombre Apellido") y la lista de diccionarios de estudiantes.
    pos: devuelve un usuario único: la primera letra del nombre más el apellido, en minúsculas.
         Si ya existe un estudiante con el mismo nombre se suman letras del nombre y, si se
         completó el nombre, un número. Si coinciden la inicial y el apellido se suma un número.
    '''
    usuario = nombre.split()
    nombre_usuario = usuario[0]
    apellido_usuario = usuario[1]
    cont = 1
    numero = 0
    primera_letra = nombre_usuario[0]
    for est in estudiantes:
        alumno = est["nombre"].split()
        if re.search(f"^{re.escape(nombre)}$", est["nombre"], re.IGNORECASE):
            # Si re repite el nombre entre los estudiantes se suma una letra del nombre al usuario
            if cont < len(nombre_usuario):
                cont += 1
            # Si se completó el nombre se le suma un número al usuario 
            else: 
                numero += 1
        elif re.search(f"^{re.escape(primera_letra)}", alumno[0], re.IGNORECASE) and re.search(f"^{re.escape(apellido_usuario)}$", alumno[1], re.IGNORECASE):
            # Si se repite el apellido y la primera letra entre los estudiantes se suma un número al usuario
                numero += 1
    if numero == 0:
        usuario = (nombre_usuario[:cont] + apellido_usuario).lower()
    else:
        usuario = (nombre_usuario[:cont] + apellido_usuario + str(numero)).lower()
    return usuario


def pedir_datos_estudiante():
    '''
    pre: no recibe parámetros.
    pos: solicita y valida nombre y apellido, edad y año de cursada.
         Devuelve la tupla (nombre, edad, anio).
    '''
    patron = r"^[A-Za-zÁÉÍÓÚÑáéíóúñ]+ +[A-Za-zÁÉÍÓÚÑáéíóúñ]+$"
    nombre = input("Ingrese el nombre y apellido del estudiante: ").strip().title()
    while not re.search(patron, nombre):
        print(f"{ROJO}ERROR: ingrese solo un nombre y un apellido, con letras.{RESET}")
        nombre = input("Ingrese otra vez el nombre y apellido: ").strip().title()
    nombre = " ".join(nombre.split())
    edad = utilidades.validar_rango(17, 100, "Ingrese la edad (17-100): ", "Edad inválida: ")
    anio = utilidades.validar_rango(1, 9, "Ingrese el año de cursada (1-9): ", "Año de cursada inválido: ")
    return nombre, edad, anio


# =========================================== ALTAS ====================================
def altas_estudiantes(arch_estudiantes):
    '''
    pre: recibe la ruta del archivo de estudiantes.
    pos: solicita y valida los datos de un nuevo estudiante y lo agrega un diccionario
         y luego al archivo de estudiantes.
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

        nombre, edad, anio = pedir_datos_estudiante()

        # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
        usuario = generar_usuarios(nombre, estudiantes)

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


# =========================================== Bajas ====================================
def bajas_estudiantes(arch_estudiantes, notas):
    '''
    pre: recibe las rutas de los archivos de estudiantes y de notas.
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


# =========================================== MODIFICACION ====================================
def modificar_estudiantes(arch_estudiantes):
    '''
    pre: recibe la ruta del archivo de estudiantes.
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
                
        nombre, edad, anio = pedir_datos_estudiante()

        # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
        otros = [est for est in estudiantes if est["legajo"] != legajo]
        usuario = generar_usuarios(nombre, otros)


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


# =========================================== LISTADO ====================================
def mostrar_estudiantes(arch_estudiantes):
    '''
    pre: recibe la ruta del archivo de estudiantes.
    pos: muestra por pantalla el listado de estudiantes en forma de tabla, recortando los
         nombres y usuarios largos. Si el archivo no se puede leer, informa el error.
    '''
    try:
        with open(arch_estudiantes, "r", encoding="UTF-8") as datos:
            estudiantes = json.load(datos)
    
        print("="*82)
        print(f'{BOLD}{MAGENTA}{"ESTUDIANTES":^82}{RESET}')
        print("="*82)
        print(f"{BOLD}{'Legajo':<13}{'Nombre':<17}{'Edad':^18}{'Año Cursada':^13}{'Usuario':>19}{RESET}")
        print("-" * 82)
        for est in estudiantes:
            legajo = est["legajo"]

            nombre = est["nombre"]
            # Si el nombre tiene mas de 15 caracteres se corta en el 12 y se le agregan "..."
            if len(nombre) > 15:
                nombre = nombre[:12] + "..."

            edad = est["edad"]
            anio = est["año cursada"]

            usuario = est["usuario"]
            # Si el usuario tiene mas de 15 caracteres se corta en el 12 y se le agregan "..."
            if len(usuario) > 15:
                usuario = usuario[:12] + "..."

            print(f"{legajo:<13}{nombre:<17}{edad:^18}{anio:^13}{usuario:>19}")

    except FileNotFoundError:
        print(f"{ROJO}ERROR: no se encontró el archivo {arch_estudiantes}.{RESET}")
    except json.JSONDecodeError:
        print(f"{ROJO}ERROR: el archivo {arch_estudiantes} está vacío o dañado.{RESET}")
    except OSError as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_estudiantes}: {error}{RESET}")