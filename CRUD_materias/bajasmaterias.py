import utilidades
import os

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

def bajas_materias(materias, notas):
    '''
    pre: recibe la matriz de materias y la de notas.
    pos: solicita el código de una materia y elimina el registro correspondiente, 
         siempre que exista y no tenga una calificación registrada.
    '''
    print()
    print(f"       ==================== {NARANJA}BAJAS MATERIAS{RESET} ====================")

    # Pedir el código a eliminar
    while True:
        try:
            codigo_baja = utilidades.leerentero("Ingrese el código de la materia a eliminar (Formato: 100): ")
            esta_en_calificaciones = utilidades.encontrar_dato(notas, 3, codigo_baja)
            registrado = utilidades.encontrar_dato(materias, 0, codigo_baja)
            assert esta_en_calificaciones == -1
            assert registrado != -1
            break
        except AssertionError:
            if registrado == -1:
                print(f"{ROJO}ERROR: Ese código no está registrado{RESET}")
            else:
                print(f"{ROJO}ERROR: Esa materia tiene una calificaión registrada, no se puede eliminar{RESET}")
            print("Intente nuevamente.")

    temp = "temp.txt"
    encontrado = False

    try:
        arch = open(materias, "rt", encoding="UTF-8")
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
            os.remove(materias)       # elimina el original
            os.rename(temp, materias) # renombra el temporal
            print(f"Materia {codigo_baja} eliminada correctamente.")
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)  # eliminamos el temporal si no se usó
        print(f"No se encontró la materia {codigo_baja}.")