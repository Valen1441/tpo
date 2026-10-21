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

def bajas_calificaciones(notas):
    '''
    pre: recibe la matriz de calificaciones.
    pos: solicita el código de una calificación y elimina el registro correspondiente.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS CALIFICACIONES{RESET} ====================")

    archivo=r'tpo/CRUD_calificaciones/notas.txt'

    # Pedir el codigo a eliminar
    while True:
        try:
            codigo_baja = utilidades.leerentero("Ingrese el código de la nota a eliminar (Formato: 100): ")
            registrado = utilidades.encontrar_dato(archivo, 0, codigo_baja)
            assert registrado != -1
            break
        except AssertionError:
            print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            print("Intente nuevamente.")

    temp = "temp.txt"
    encontrado = False

    try:
        arch = open(archivo, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = linea.strip().split(";")
            codigo = int(datos[0])
            if codigo != codigo_baja:
                aux.write(linea)
            else:
                encontrado = True

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
            os.remove(archivo)       # elimina el original
            os.rename(temp, archivo) # renombra el temporal
            print(f"Nota {codigo_baja} eliminada correctamente.")
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)  # eliminamos el temporal si no se usó
        print(f"No se encontró la nota {codigo_baja}.")