import utilidades
import json

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def modificar_estudiantes(arch_estudiantes):
    '''
    pre: recibe la lista de diccionarios de estudiantes.
    pos: solicita el legajo de un estudiante y modifica sus datos validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN ESTUDIANTES{RESET} ====================")

    try:
        with open(arch_estudiantes, 'r', encoding="UTF-8") as datos:
            estudiantes = json.load(datos)

        legajos = [emp["legajo"] for emp in estudiantes]
        
        # Pedir el legajo a modificar
        while True:
            try:
                legajo = utilidades.leerentero("Ingrese el legajo del estudiante a modificar (Formato: 100): ")
                assert legajo in legajos
                break
            except AssertionError:
                print(f"{ROJO}ERROR: Ese legajo no está registrado{RESET}")
                print("Intente nuevamente.")

                                
        # Pedir nombre del estudiante
        nombre = input("Ingrese el nombre y apellido del estudiante: ").title()

        while len(nombre.split()) != 2:
            print(f"{ROJO}ERROR: debe ingresar solo un nombre y apellido.{RESET}")
            nombre = input("Ingrese otra vez el nombre y apellido del estudiante: ").title()

        nombre = nombre.split()
        nombre = nombre[0] + " " + nombre[1]
        
        
        #Pedir edad
        while True:
            try:
                edad = utilidades.leerentero("Ingrese la edad del nuevo estudiante: ")
                assert edad > 17 and edad < 100
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


        # Verificar si el legajo existe usando 'in' en una lista de legajos
        if legajo in legajos:
            # Obtener índice del empleado y modificar
            indice = legajos.index(legajo)
            estudiantes[indice]["nombre"] = nombre
            estudiantes[indice]["edad"] = edad
            estudiantes[indice]["año cursada"] = anio
            estudiantes[indice]["usuario"] = usuario
            with open(arch_estudiantes, 'w', encoding="UTF-8") as datos:
                json.dump(estudiantes, datos, ensure_ascii=False, indent=4)
            print(f"Estudiante con legajo {legajo} modificado")
        else:
            print(f"Estudiante con legajo {legajo} no encontrado.")
    except (FileNotFoundError, OSError, json.JSONDecodeError) as error:
        print(f'Error! {error}')
