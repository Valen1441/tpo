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
    print()
    print(f"       ==================== {VERDE}ALTAS ESTUDIANTES{RESET} ====================")

    try:
        with open(arch_estudiantes, 'r', encoding="UTF-8") as datos:
            estudiantes = json.load(datos)  # Cargar el contenido existente del archivo JSON

        # Obtener el legajo más alto y sumar 1
        if estudiantes:
            nuevo_legajo = max(est["legajo"] for est in estudiantes) + 1
        else:
            nuevo_legajo = 1  # Si la lista está vacía, comenzamos desde 1

        # Pedir nombre del estudiante
        nombre = input("Ingrese el nombre y apellido del nuevo estudiante: ").title()

        while len(nombre.split()) != 2:
            print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
            nombre = input("Ingrese otra vez el nombre y apellido del nuevo estudiante: ").title()

        nombre = nombre.split()
        nombre = nombre[0] + " " + nombre[1]
        
        
        # Pedir edad
        while True:
            try:
                edad = utilidades.leerentero("Ingrese la edad del nuevo estudiante: ")
                assert edad >= 17 and edad <= 100
                break
            except AssertionError:
                print(f"{ROJO}Edad invalida: rango perimitido de 17 a 100 años{RESET}")
                print("Intente nuevamente.")


        # Pedir año de cursada
        while True:
            try:
                anio = utilidades.leerentero("Ingrese el año de cursada del nuevo estudiante (1-9): ")
                assert anio > 0 and anio < 10
                break
            except AssertionError:
                print(f"{ROJO}Año de cursada invalido: rango perimitido de 1 a 9{RESET}")
                print("Intente nuevamente.")


        # Genera el nombre de usuario tomando la primera letra del nombre y todo el apellido
        usuario = utilidades.generar_usuarios(nombre, estudiantes)

        # Crear nuevo empleado
        nuevo_estudiante = {"legajo": nuevo_legajo, "nombre": nombre, "edad": edad, "año cursada": anio, "usuario": usuario}
        estudiantes.append(nuevo_estudiante)

        # Sobrescribir el archivo con los datos actualizados
        with open(arch_estudiantes, 'w', encoding="UTF-8") as datos:
            json.dump(estudiantes, datos, ensure_ascii=False, indent=4) # ensure_ascii=False Permite conservar caracteres como á, é, í, ó, ú y ñ directamente en el archivo JSON, en lugar de representarlos mediante secuencias de escape Unicode.
        print(f'Se ha agregado a {nuevo_estudiante['nombre']}')

    except (FileNotFoundError, OSError, json.JSONDecodeError) as error:
        print(f'Error! {error}')
