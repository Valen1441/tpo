import utilidades
import os

# Códigos ANSI
RESET = "\033[0m"
BOLD  = "\033[1m"
ROJO  = "\033[31;1m"
VERDE = "\033[32;1m"
AZUL  = "\033[34;1m"
MAGENTA  = "\033[35;1m"
NARANJA = "\033[33;1m"

def modificar_calificaciones(notas, estudiantes, materias):
    '''
    pre: recibe la lista de diccionarios de estudiantes y las matrices notas y materias.
    pos: solicita una calificación existente y modifica sus datos, validando la información ingresada.
    '''
    print()
    print(f"       ==================== {AZUL}MODIFICACIÓN CALIFICACIONES{RESET} ====================")

    lista_legajos = utilidades.obtener_lista_legajos(estudiantes)

    archivo=r'tpo/CRUD_calificaciones/notas.txt'
    
    # Pedir el codigo a modificar
    while True:
        try:
            codigo_modif = utilidades.leerentero("Ingrese el código de la nota a modificar (Formato: 100): ")
            nota_modificar = utilidades.busqueda_secuencial(notas, 0, codigo_modif)
            assert nota_modificar != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")
                
                
    # Pedir el nuevo legajo
    while True:
        try:
            legajo = utilidades.leerentero("Ingrese el legajo del estudiante a calificar (Formato: 100): ")
            assert legajo in lista_legajos
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese legajo no está registrado.{RESET}")
            print("Intente nuevamente.")

        
    # Pedir el nuevo codigo de materia
    while True:
        try:
            materia = utilidades.leerentero("Ingrese el código de la materia (Formato: 100): ")
            registrado = utilidades.busqueda_secuencial(materias, 0, materia)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código de materia no está registrado.{RESET}")
            print("Intente nuevamente.")

    
    # Pedir la nueva nota
    while True:
        try:
            nota = utilidades.leerentero("Ingrese la nota: ")
            assert nota > 0 and nota <= 10
            break
        except AssertionError:
            print(f"{ROJO}ERROR: La nota debe ser mayor a 0 y menor o igual a 10.{RESET}")
            print("Intente nuevamente.")
        

    if nota >= 8:
        condicion = 2
    elif nota >= 4:
        condicion = 1
    else:
        condicion = 3
    
    temp = "temp.txt"
    encontrado = False

    try:
        arch = open(archivo, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = linea.strip().split(";")
            codigo = int(datos[0])

            if codigo == codigo_modif:
                encontrado = True

                nueva_linea = f'{codigo_modif};{nota};{legajo};{materia};{condicion}\n'
                aux.write(nueva_linea)
                print(f"Nota {codigo_modif} modificada.")
            else:
                aux.write(linea)
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo:")

    if encontrado:
        try:
            os.remove(archivo)
            os.rename(temp, archivo)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)
        print(f"No se encontró la nota {codigo_modif}.")