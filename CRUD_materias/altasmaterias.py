import utilidades

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def obtener_ultimo_codigo(archivo):
    ultimo_codigo = "000"
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                datos = linea.strip().split(";")
                ultimo_codigo = datos[0]
    except FileNotFoundError:
        pass  # Si no existe el archivo, empezamos desde cero
    return ultimo_codigo

def siguiente_codigo(codigo_actual):
    numero = int(codigo_actual) + 1
    return str(numero)


def altas_materias(materias):
    '''
    pre: recibe la matriz de materias.
    pos: agrega una nueva materia a la matriz con un código,
         nombre, cuatrimestre, año y carga horaria válidos.
    '''
    print()
    print(f"       ==================== {VERDE}ALTAS MATERIAS{RESET} ====================")

    ultimo = obtener_ultimo_codigo(materias)
    nuevo_codigo = siguiente_codigo(ultimo)

    # Pedir nombre
    nombre = input("Ingrese el nombre de la nueva materia: ").title()
    
    # Pedir cuatrimestre
    while True:
        try:
            cuatrimestre = utilidades.leerentero("Ingrese el cuatrimestre de la nueva materia (1-2): ")
            assert cuatrimestre >= 1 and cuatrimestre <= 2
            break
        except AssertionError:
            print(f"{ROJO}Cuatimestre invalido: rango perimitido de 1 a 2{RESET}")
            print("Intente nuevamente.")


    # Pedir año de la materia
    while True:
        try:
            anio = utilidades.leerentero("Ingrese el año de la nueva materia (1-5): ")
            assert anio >= 1 and anio <= 5
            break
        except AssertionError:
            print(f"{ROJO}Año inválido: rango perimitido de 1 a 5 años{RESET}")
            print("Intente nuevamente.")


    # Pedir carga horaria 
    while True:
        try:
            horaria = utilidades.leerentero("Ingrese la carga horaria de la nueva materia (1-12): ")
            assert horaria >= 1 and horaria <= 12
            break
        except AssertionError:
            print(f"{ROJO}Carga horaria invalida: rango perimitido de 1 a 12 horas{RESET}")
            print("Intente nuevamente.")

    try:
        arch = open(materias, "a", encoding="UTF-8") #Importar archivo
        nueva_materia = f'{nuevo_codigo};{nombre};{cuatrimestre};{anio};{horaria}\n'
        arch.write(nueva_materia)

        print(f"{VERDE}Materia {nuevo_codigo} agregada.{RESET}")

    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass